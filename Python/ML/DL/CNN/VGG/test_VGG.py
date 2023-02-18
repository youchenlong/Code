import tensorflow as tf

def load_data():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()
    x_train = x_train.reshape(-1, 28, 28, 1).astype("float32") / 255
    x_train = tf.pad(x_train, [[0, 0], [2, 2], [2, 2], [0, 0]])
    x_train = tf.image.grayscale_to_rgb(x_train)
    y_train = y_train.astype("int32")

    x_test = x_test.reshape(-1, 28, 28, 1).astype("float32") / 255
    x_test = tf.pad(x_test, [[0, 0], [2, 2], [2, 2], [0, 0]])
    x_test = tf.image.grayscale_to_rgb(x_test)
    y_test = y_test.astype("int32")
    return (x_train, y_train), (x_test, y_test)

def get_model():
    # 迁移学习--使用VGG16提取特征
    base_model = tf.keras.applications.VGG16(include_top=False, input_shape=(32, 32, 3))
    for layer in base_model.layers:
        layer.trainable = False
    model = tf.keras.models.Sequential([
        base_model,
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(units=120, activation="relu"),
        # tf.keras.layers.Dropout(rate=0.5),
        tf.keras.layers.Dense(units=84, activation="relu"),
        # tf.keras.layers.Dropout(rate=0.5),
        tf.keras.layers.Dense(10, activation="softmax")
    ])
    return model

(x_train, y_train), (x_test, y_test) = load_data()
model = get_model()
model.compile(optimizer="adam", loss="SparseCategoricalCrossentropy", metrics=["accuracy"])
# model.load_weights("./models/VGG")

epochs, batch_size = 5, 128
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir="logs")
model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=0.2, callbacks=[tensorboard_callback])
model.evaluate(x_test, y_test, batch_size=batch_size)
model.save_weights("./models/VGG")