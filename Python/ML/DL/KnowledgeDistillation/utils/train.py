import tensorflow as tf
from tqdm import tqdm

def train_step(train_db, model=None ):

    optimizer = tf.keras.optimizers.Adam(learning_rate=1e-3)
    criterion = tf.keras.losses.CategoricalCrossentropy(from_logits=True)

    for X, y in tqdm(train_db):
        with tf.GradientTape() as tape:
            logits = model(X, training=True)
            y_onehot = tf.one_hot(y, depth=10)

            print(f"y_onehot:{y_onehot.shape}")

            loss = criterion(y_onehot, logits)
            loss = tf.reduce_mean(loss)

        grads = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(grads, model.trainable_variables))


def test_step(test_db,model=None,total_num=0, total_correct=0):

    for x, y in tqdm(test_db):
        logits = model(x, training=False)
        prob = tf.nn.softmax(logits, axis=1)
        pred = tf.argmax(prob, axis=1)
        pred = tf.cast(pred, dtype=tf.int32)

        correct = tf.cast(tf.equal(pred, y), dtype=tf.int32)
        correct = tf.reduce_sum(correct)

        total_num += x.shape[0]
        total_correct += int(correct)
    acc = total_correct / total_num
    print('acc', acc)