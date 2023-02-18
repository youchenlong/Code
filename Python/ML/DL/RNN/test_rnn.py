import tensorflow as tf

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.imdb.load_data(num_words=1000)
x_train = tf.keras.preprocessing.sequence.pad_sequences(x_train, maxlen=80)
x_test = tf.keras.preprocessing.sequence.pad_sequences(x_test, maxlen=80)

model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(input_dim=1000, output_dim=128),
    tf.keras.layers.LSTM(128),
    tf.keras.layers.Dense(1),
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# model.load_weights("./models/rnn")

model.fit(x_train, y_train, batch_size=32, epochs=10, validation_split=0.2)

model.evaluate(x_test, y_test, batch_size=32)

model.save_weights("./models/rnn")