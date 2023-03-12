import tensorflow as tf

class StudentNet(tf.keras.Model):
    def __init__(self):
        super(StudentNet, self).__init__()
        self.conv1 = tf.keras.layers.Conv2D(32, (3, 3), padding="same",activation="relu",name="this_is_conv1")
        self.conv2 = tf.keras.layers.Conv2D(32, (3, 3),padding="same",activation="relu")
        self.maxpool1 = tf.keras.layers.MaxPooling2D((2, 2))
        self.dropout1 = tf.keras.layers.Dropout(0.5, name="this_is_dropout1")

        self.conv3 = tf.keras.layers.Conv2D(64, (3, 3), padding="same", activation="relu")
        self.conv4 = tf.keras.layers.Conv2D(64, (3, 3), padding="same", activation="relu")
        self.maxpool2 = tf.keras.layers.MaxPooling2D((2, 2))
        self.dropout2 = tf.keras.layers.Dropout(0.5)

        self.avgpool = tf.keras.layers.GlobalAveragePooling2D()
        self.flatten = tf.keras.layers.Flatten(name="my_name_is_flatten")
        self.d1 = tf.keras.layers.Dense(40,activation="relu")
        self.dropout3 = tf.keras.layers.Dropout(0.5)
        self.d2 = tf.keras.layers.Dense(10, name='logits')

    def call(self, input, training=None):
        
        x = self.conv1(input)
        x = self.conv2(x)
        x = self.maxpool1(x)
        x = self.dropout1(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = self.maxpool2(x)
        x = self.dropout2(x)
        x = self.avgpool(x)
        x = self.flatten(x)
        x = self.d1(x)
        x = self.dropout3(x)
        output = self.d2(x)

        return output

if __name__ == '__main__':
    model = StudentNet()
    model.build(input_shape=[None,32,32,3])
    model.summary()