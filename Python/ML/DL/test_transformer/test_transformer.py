import tensorflow as tf
from model import Transformer, Mask

D_POINT_WISE_FF = 2048
D_MODEL = 512
ENCODER_COUNT = DECODER_COUNT = 6
ATTENTION_HEAD_COUNT = 8
DROPOUT_PROB = 0.1
BPE_VOCAB_SIZE = 32000

transformer = Transformer(
    inputs_vocab_size=BPE_VOCAB_SIZE,
    target_vocab_size=BPE_VOCAB_SIZE,
    encoder_count=ENCODER_COUNT,
    decoder_count=DECODER_COUNT,
    attention_head_count=ATTENTION_HEAD_COUNT,
    d_model=D_MODEL,
    d_point_wise_ff=D_POINT_WISE_FF,
    dropout_prob=DROPOUT_PROB
)

optimizer = tf.optimizers.Adam()
loss = tf.losses.CategoricalCrossentropy()

epochs = 10

for epoch in range(epochs):
    for (batch, (inputs, target)) in enumerate(dataset):
        target_include_start = target[:, :-1]
        target_include_end = target[:, 1:]
        encoder_padding_mask, look_ahead_mask, decoder_padding_mask = Mask.create_masks(inputs, target_include_start)
        with tf.GradientTape() as tape:
            pred = transformer.call(
                inputs=inputs,
                target=target_include_start,
                inputs_padding_mask=encoder_padding_mask,
                look_ahead_mask=look_ahead_mask,
                target_padding_mask=decoder_padding_mask,
                training=True
            )
            losses = loss(target_include_end, pred)
        gradients = tape.gradient(losses, transformer.trainable_variables)
        optimizer.apply_gradients(zip(gradients, transformer.trainable_variables))