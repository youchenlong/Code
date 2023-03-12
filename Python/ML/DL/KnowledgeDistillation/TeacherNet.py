import tensorflow as tf

class TeacherNet(tf.keras.Model):
    def __init__(self):

        super(TeacherNet, self).__init__()
        self.conv1 = tf.keras.layers.Conv2D(32, (3,3),padding="same",activation="relu")
        self.conv2 = tf.keras.layers.Conv2D(32, (3,3),padding="same",activation="relu")
        self.maxpool1 = tf.keras.layers.MaxPooling2D((2,2))
        self.dropout1 = tf.keras.layers.Dropout(0.5)

        self.conv3 = tf.keras.layers.Conv2D(64,(3,3),padding="same",activation="relu")
        self.conv4 = tf.keras.layers.Conv2D(64,(3,3),padding="same",activation="relu")
        self.maxpool2 = tf.keras.layers.MaxPooling2D((2,2))
        self.dropout2 = tf.keras.layers.Dropout(0.5)

        self.conv5 = tf.keras.layers.Conv2D(128,(3,3),padding="same",activation="relu")
        self.conv6 = tf.keras.layers.Conv2D(128,(3,3),padding="same",activation="relu")
        self.maxpool3 = tf.keras.layers.MaxPooling2D((2,2))
        self.dropout3 = tf.keras.layers.Dropout(0.5)

        self.avgpool = tf.keras.layers.AveragePooling2D()
        self.flatten = tf.keras.layers.Flatten()

        self.d1 = tf.keras.layers.Dense(128, activation="relu")
        self.dropout4 = tf.keras.layers.Dropout(0.5)
        self.d2 = tf.keras.layers.Dense(10, name='logits')

    def call(self, input):
        x = self.conv1(input)
        x = self.conv2(x)
        x = self.maxpool1(x)
        x = self.dropout1(x)

        x = self.conv3(x)
        x = self.conv4(x)
        x = self.maxpool2(x)
        x = self.dropout2(x)

        x = self.conv5(x)
        x = self.conv6(x)
        x = self.maxpool3(x)
        x = self.dropout3(x)

        x = self.avgpool(x)

        x = self.flatten(x)
        x = self.d1(x)
        x = self.dropout4(x)
        out = self.d2(x) #这里的out输出的logits而非softmax

        return out

if __name__ == '__main__':
    model = TeacherNet()
    model.build(input_shape=[None,32,32,3])
    model.summary()