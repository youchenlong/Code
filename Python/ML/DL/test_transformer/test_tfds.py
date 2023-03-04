import tensorflow_datasets as tfds
import tensorflow as tf

# ds, info = tfds.load('mnist', as_supervised=True, with_info=True)
ds, info = tfds.load('imdb_reviews', as_supervised=True, with_info=True)
ds_train, ds_test = ds['train'], ds['test_transformer']
batch_size = 32
ds_train = ds_train.shuffle(batch_size).batch(batch_size)
ds_test = ds_test.shuffle(batch_size).batch(batch_size)


for (batch, (image, label)) in enumerate(ds_test):
    print(batch, image.shape, label.shape)
