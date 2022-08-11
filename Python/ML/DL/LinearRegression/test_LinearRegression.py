import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split

tf.random.set_seed(2)

def load_data():
    np.random.seed(2)
    n = 1000
    X_data = np.linspace(0, 100, n).reshape(n, 1)
    y_data = 2*X_data+3+np.random.normal(size=X_data.size).reshape(n, 1)
    X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2)
    return tf.cast(X_train, tf.float32), \
           tf.cast(X_test, tf.float32), \
           tf.cast(y_train, tf.float32), \
           tf.cast(y_test, tf.float32)

class LinearRegression(tf.keras.Model):
    def __init__(self):
        super(LinearRegression, self).__init__()
        self.dense = tf.keras.layers.Dense(1)
    def call(self, input):
        output = self.dense(input)
        return output

X_train, X_test, y_train, y_test = load_data()
model = LinearRegression()
optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)
logdir = r'C:\Users\Lenovo\Desktop\Code\Python\ML\tensorflow_exercise\LinearRegression\logs'
writer = tf.summary.create_file_writer(logdir=logdir)
for step in range(1000):
    with tf.GradientTape() as tape:
        y_pred = model(X_train)
        loss = tf.reduce_mean(tf.square(y_pred-y_train))
        print('step: {}, loss: {}'.format(step, loss))
        with writer.as_default():
            tf.summary.scalar('loss', loss, step=step)
            writer.flush()
    grads = tape.gradient(loss, model.variables)
    optimizer.apply_gradients(zip(grads, model.variables))