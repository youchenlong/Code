import os
import tensorflow as tf
from TeacherNet import TeacherNet
from StudentNet import StudentNet
from utils.train import train_step
from utils.train import test_step
from utils.create_dataset import create_dataset
from tqdm import tqdm
from utils.losses import distillation_loss_fn, student_loss_fn


def main():
    # define dataset
    (train_db, test_db) = create_dataset()
    # define model
    # use gpu
    mirrored_strategy = tf.distribute.MirroredStrategy()
    with mirrored_strategy.scope():
        teacher_model = TeacherNet()
        student_model = StudentNet()

    # define parameters
    optimizer = tf.keras.optimizers.Adam(1e-3)
    alpha = 0.2
    EPOCHS = 20

    # load weights
    teacher_checkpoint_save_path = "./checkpoints/teacher_checkpoint.ckpt"
    student_checkpoint_save_path = "./checkpoints/student_checkpoint.ckpt"
    if os.path.exists(teacher_checkpoint_save_path + '.index'):
        teacher_model.load_weights(teacher_checkpoint_save_path)
        print("teacher checkpoint load success!")
    if os.path.exists(student_checkpoint_save_path + '.index'):
        student_model.load_weights(student_checkpoint_save_path)
        print("student checkpoint load success!")

    # train from scratch
    for epoch in range(EPOCHS):
        print('Epoch {}:', epoch+1)
        train_step(train_db, teacher_model)
        train_step(train_db, student_model)

    for epoch in range(EPOCHS):
        # 本实验采用的cifar10由于数据量过小,使用epoch可能并没有那么多意义，因此选用可以观察进度的tqdm
        # for step, (data, target) in enumerate(train_db):
        for data, target in tqdm(train_db):
            with tf.GradientTape() as tape:
                teacher_logits = teacher_model(data, training=False)
                student_logits = student_model(data, training=True)  # float32,(256,10)
                distillation_loss = distillation_loss_fn(student_logits, teacher_logits)

                target = tf.one_hot(target, depth=10)
                student_loss = student_loss_fn(student_logits, target)

                loss = alpha * student_loss + (1 - alpha) * distillation_loss

            grads = tape.gradient(loss, student_model.trainable_variables)
            optimizer.apply_gradients(zip(grads, student_model.trainable_variables))

        test_step(test_db, student_model)

    # save weights
    if os.path.exists('./checkpoints'):
        student_model.save_weights(student_checkpoint_save_path)
        print("student model checkpoint saved")


if __name__ == '__main__':
    main()


