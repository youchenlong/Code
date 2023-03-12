import os
from StudentNet import StudentNet
from utils.train import test_step
from utils.create_dataset import create_dataset


if __name__ == '__main__':
    (train_db, test_db) = create_dataset()
    student_model = StudentNet()
    student_checkpoint_save_path = "./checkpoints/student_checkpoint.ckpt"
    if os.path.exists(student_checkpoint_save_path + '.index'):
        student_model.load_weights(student_checkpoint_save_path)
        print("student checkpoint load success!")
    test_step(test_db, student_model)
