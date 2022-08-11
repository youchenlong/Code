import os
import tensorflow as tf
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

tf.random.set_seed(2)

def load_data():
    data = load_boston()
    X_data, y_data = data.data, data.target
    y_data = y_data.reshape(y_data.shape[0], 1)
    X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2)
    return tf.cast(X_train, tf.float32), \
           tf.cast(X_test, tf.float32), \
           tf.cast(y_train, tf.float32), \
           tf.cast(y_test, tf.float32)

def load_weights(model, filepath):
    dirname = os.path.dirname(filepath)
    if not os.path.exists(dirname):
        os.mkdir(dirname)
        print("load weights failed")
        return False
    else:
        model.load_weights(filepath)
        print("load weights successfully")
        return True

class MLP(tf.keras.Model):
    def __init__(self):
        super(MLP, self).__init__()
        self.dense1 = tf.keras.layers.Dense(units=30, activation='relu', kernel_regularizer='l2')
        self.dropout1 = tf.keras.layers.Dropout(rate=0.5)
        self.dense2 = tf.keras.layers.Dense(units=20, activation='relu', kernel_regularizer='l2')
        self.dropout2 = tf.keras.layers.Dropout(rate=0.5)
        self.dense3 = tf.keras.layers.Dense(units=1, kernel_regularizer='l2')
    def call(self, inputs, training=False):
        x = self.dense1(inputs)
        if training:
            x = self.dropout1(x, training=training)
        x = self.dense2(x)
        if training:
            x = self.dropout2(x, training=training)
        outputs = self.dense3(x)
        return outputs

# 加载数据
X_train, X_test, y_train, y_test = load_data()
# 创建模型
model = MLP()
# 加载网络模型的权重
filepath = os.path.join(os.getcwd(), 'saved_models', 'mlp')
skip_train = load_weights(model, filepath)
# 优化器
optimizer = tf.keras.optimizers.Adam()
"""
======================================
train
======================================
"""
if skip_train:
    steps = 0
else:
    steps = 10000
    # tensorboard
    logdir = os.path.join(os.getcwd(), 'logs')
    writer = tf.summary.create_file_writer(logdir=logdir)
for step in range(1,steps+1):
    # 注意tape的作用域
    with tf.GradientTape() as tape:
        y_pred = model(X_train, training=True)
        loss = tf.reduce_mean(tf.square(y_pred - y_train))
        print('step: {}/{}, loss: {}'.format(step, steps, loss))
        with writer.as_default():
            tf.summary.scalar('loss', loss, step=step)
            writer.flush()
    grads = tape.gradient(loss, model.variables)
    optimizer.apply_gradients(zip(grads, model.variables))
"""
======================================
test
======================================
"""
y_pred = model(X_test)
loss = tf.reduce_mean(tf.square(y_pred-y_test))
print(loss)
"""
======================================
save weights
======================================
"""
model.save_weights(filepath, save_format="tf")