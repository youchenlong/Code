import os
import numpy as np
import tensorflow as tf
import tensorlayer as tl

def load_data():
    return tl.files.load_mnist_dataset(shape=(-1, 784), path=r'C:\Users\Lenovo\Desktop\data')

class CNN(tf.keras.Model):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = tf.keras.layers.Conv2D(32, (3,3))
        self.pool1 = tf.keras.layers.MaxPool2D((2,2))
        self.conv2 = tf.keras.layers.Conv2D(64, (3,3))
        self.pool2 = tf.keras.layers.MaxPool2D((2,2))
        self.conv3 = tf.keras.layers.Conv2D(64, (3,3))
        self.pool3 = tf.keras.layers.MaxPool2D((2,2))
        self.dense1 = tf.keras.layers.Flatten()
        self.dense2 = tf.keras.layers.Dense(64, activation='relu')
        self.dense2 = tf.keras.layers.Dense(64, activation='softmax')
    def call(self, inputs, training=False):
        x = self.conv1(inputs)
        x = self.pool1(x)
        x = self.conv2(x)
        x = self.pool2(x)
        x = self.conv3(x)
        x = self.pool3(x)
        x = self.dense1(x)
        x = self.dense2(x)
        outputs = self.dense3(x)
        return outputs

X_train, y_train, X_val, y_val, X_test, y_test = load_data()
model = CNN()

steps = 1000
batch_size = 32
