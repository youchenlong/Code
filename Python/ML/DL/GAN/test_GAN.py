import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

BATCH_SIZE = 300  # batch大小
BUFFER_SIZE = 60000  # 训练集有6w张图片
EPOCHS = 300  # 批次数量
noise_dim = 100  # 随机数的维度


def load_data():
    (train_images, train_labels), (_, _) = tf.keras.datasets.mnist.load_data()
    train_images = train_images.reshape(train_images.shape[0], 28, 28, 1).astype('float32')
    train_images = (train_images - 127.5) / 127.5
    train_images = tf.data.Dataset.from_tensor_slices(train_images).shuffle(BUFFER_SIZE).batch(BATCH_SIZE)
    return (train_images, train_labels), (_, _)


def generator_model():
    generator = keras.models.Sequential([
        keras.layers.Input(shape=(100,)),
        keras.layers.Dense(256),
        keras.layers.LeakyReLU(alpha=0.2),
        keras.layers.BatchNormalization(momentum=0.8),
        keras.layers.Dense(512),
        keras.layers.LeakyReLU(alpha=0.2),
        keras.layers.BatchNormalization(momentum=0.8),
        keras.layers.Dense(1024),
        keras.layers.LeakyReLU(alpha=0.2),
        keras.layers.BatchNormalization(momentum=0.8),
        keras.layers.Dense(np.prod((28, 28, 1)), activation='tanh'),
        keras.layers.Reshape((28, 28, 1))
    ])
    return generator


def discriminator_model():
    discriminator = keras.models.Sequential([
        keras.layers.Flatten(),
        keras.layers.Dense(512),
        keras.layers.LeakyReLU(alpha=0.2),
        keras.layers.Dense(256),
        keras.layers.LeakyReLU(alpha=0.2),
        keras.layers.Dense(1)
    ])
    return discriminator


def discriminator_loss(real_out, fake_out):
    cross_entropy = tf.keras.losses.BinaryCrossentropy(from_logits=True)
    real_loss = cross_entropy(tf.ones_like(real_out), real_out)
    fake_loss = cross_entropy(tf.zeros_like(fake_out), fake_out)
    return real_loss + fake_loss


def generator_loss(fake_out):
    cross_entropy = tf.keras.losses.BinaryCrossentropy(from_logits=True)
    fake_loss = cross_entropy(tf.ones_like(fake_out), fake_out)
    return fake_loss


(train_images, train_labels), (_, _) = load_data()

generator = generator_model()
discriminator = discriminator_model()

generator_opt = tf.keras.optimizers.Adam(2e-4, 0.5)
discriminator_opt = tf.keras.optimizers.Adam(2e-4, 0.5)


@tf.function
def train_step(images):
    noise = tf.random.normal([BATCH_SIZE, noise_dim])
    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
        real_out = discriminator(images, training=True)
        gen_image = generator(noise, training=True)
        fake_out = discriminator(gen_image, training=True)
        gen_loss = generator_loss(fake_out)
        disc_loss = discriminator_loss(real_out, fake_out)
    gradient_gen = gen_tape.gradient(gen_loss, generator.trainable_variables)
    gradient_disc = disc_tape.gradient(disc_loss, discriminator.trainable_variables)
    generator_opt.apply_gradients(zip(gradient_gen, generator.trainable_variables))
    discriminator_opt.apply_gradients(zip(gradient_disc, discriminator.trainable_variables))


num_example_to_generate = 6
seed = np.random.normal(0, 1, (num_example_to_generate, noise_dim))


def generate_plot_image(test_noise):
    pre_image = generator(test_noise, training=False)
    plt.figure(figsize=(16, 3))
    for i in range(pre_image.shape[0]):
        plt.subplot(1, 6, i + 1)
        plt.imshow((pre_image[i, :, :, :] + 1) / 2)
        plt.axis('off')
    plt.show()


def train(dataset, epochs):
    for epoch in range(1, epochs + 1):
        print("epoch:", epoch)
        for image_batch in dataset:
            train_step(image_batch)
        # generate_plot_image(seed)


generate_plot_image(seed)
train(train_images, EPOCHS)
generate_plot_image(seed)
