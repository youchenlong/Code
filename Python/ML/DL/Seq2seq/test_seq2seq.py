import tensorflow as tf

class Encoder(tf.keras.models.Model):
    def __init__(self, vocab_size, embed_size, num_hiddens, num_layers, dropout=0):
        super().__init__()
        self.embedding = tf.keras.layers.Embedding(vocab_size, embed_size)
        self.rnn = tf.keras.layers.RNN(
            tf.keras.layers.StackedRNNCells(
                [tf.keras.layers.GRUCell(num_hiddens, dropout=dropout) for _ in range(num_layers)]),
            return_sequences=True, return_state=True)

    def call(self, X):
        X = self.embedding(X)
        encoder_outputs, state = self.rnn(X)
        return encoder_outputs, state


class Decoder(tf.keras.models.Model):
    def __init__(self, vocab_size, embed_size, num_hiddens, num_layers, dropout=0):
        super().__init__()
        self.embedding = tf.keras.layers.Embedding(vocab_size, embed_size)
        self.rnn = tf.keras.layers.RNN(
            tf.keras.layers.StackedRNNCells(
                [tf.keras.layers.GRUCell(num_hiddens, dropout=dropout) for _ in range(num_layers)]),
            return_sequences=True, return_state=True)
        self.attention = tf.keras.layers.Attention()
        self.dense = tf.keras.layers.Dense(vocab_size)

    def init_state(self, state):
        return state

    def call(self, X, state, encoder_outputs):
        X = self.embedding(X)
        context = tf.repeat(tf.expand_dims(state[-1], axis=1), repeats=X.shape[1], axis=1)
        X_and_context = tf.concat((X, context), axis=2)
        outputs, state = self.rnn(X_and_context, state)
        attention_outputs = self.attention([outputs, encoder_outputs])
        decoder_outputs = self.dense(attention_outputs)
        return decoder_outputs, state


def seq2seq(src_vocab, tgt_vocab, embed_size, num_hiddens, num_layers, dropout):
    enc_X = tf.keras.layers.Input(shape=(None,))
    dec_X = tf.keras.layers.Input(shape=(None,))
    encoder = Encoder(len(src_vocab), embed_size, num_hiddens, num_layers, dropout)
    decoder = Decoder(len(tgt_vocab), embed_size, num_hiddens, num_layers, dropout)
    encoder_outputs, state = encoder(enc_X)
    state = decoder.init_state(state)
    decoder_outputs, state = decoder(dec_X, state, encoder_outputs)
    model = tf.keras.models.Model([enc_X, dec_X], decoder_outputs)
    return model