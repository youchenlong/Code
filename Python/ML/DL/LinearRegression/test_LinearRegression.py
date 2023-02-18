import tensorflow as tf

tf.random.set_seed(2)

def get_data():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
    x_train = x_train.reshape(60000, 784).astype("float32") / 255
    x_test = x_test.reshape(10000, 784).astype("float32") / 255
    y_train = y_train.astype("int32")
    y_test = y_test.astype("int32")
    return (x_train, y_train), (x_test, y_test)

def get_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(units=10, activation="softmax")
    ])
    return model

(x_train, y_train), (x_test, y_test) = get_data()
model = get_model()

lr, epochs, batch_size = 0.1, 10, 256
model.compile(optimizer="adam", loss="SparseCategoricalCrossentropy", metrics=["accuracy"])
# model.load_weights("./models/LR")

tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir="logs")
model.fit(x_train, y_train, validation_split=0.2, epochs=epochs, batch_size=batch_size, callbacks=[tensorboard_callback])

model.evaluate(x_test, y_test, batch_size=batch_size)

model.save_weights("./models/LR")