import tensorflow as tf

def get_data():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
    x_train = x_train.reshape((-1, 28, 28, 1)).astype("float32")/255
    y_train = y_train.astype("int32")
    x_test = x_test.reshape((-1, 28, 28, 1)).astype("float32")/255
    y_test = y_test.astype("int32")
    return (x_train, y_train), (x_test, y_test)

def get_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(filters=6, kernel_size=5, activation='sigmoid', padding='same'),
        tf.keras.layers.AvgPool2D(pool_size=2, strides=2),
        tf.keras.layers.Conv2D(filters=16, kernel_size=5, activation='sigmoid'),
        tf.keras.layers.AvgPool2D(pool_size=2, strides=2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(120, activation='sigmoid'),
        tf.keras.layers.Dense(84, activation='sigmoid'),
        tf.keras.layers.Dense(10, activation="softmax")
    ])
    return model

(x_train, y_train), (x_test, y_test) = get_data()
model = get_model()
num_epochs, batch_size = 5, 128
model.compile(optimizer="adam", loss="SparseCategoricalCrossentropy", metrics=["accuracy"])
# model.load_weights("models/lenet")

tensorboard_callback = tf.keras.callbacks.TensorBoard("logs", histogram_freq=5)
model.fit(x_train, y_train, validation_split=0.2, epochs=num_epochs, batch_size=batch_size, callbacks=[tensorboard_callback])

model.evaluate(x_test, y_test, batch_size=batch_size)

model.save_weights("./models/lenet")