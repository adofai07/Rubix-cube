import tensorflow as tf
from type import Cube, scrambled_cube, initial_cube
import tqdm
import random
import numpy as np
import pickle
import os
import sys
from path import checkpoint_path, save_path, load_path, repo_path

print(tf.__version__)
print(tf.config.list_physical_devices('GPU'))

def save(data, thread=0):
    with open(FR"{repo_path}\G{thread}.adofai", "wb+") as f:
        pickle.dump(data, f)

def load(thread=0):
    while True:
        try:
            with open(FR"{repo_path}\G{thread}.adofai", "rb") as f:
                return pickle.load(f)
            
        except:
            ...

cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)


model = tf.keras.Sequential([
    tf.keras.layers.Dense(3125, activation='sigmoid', input_shape=(54, )),
    tf.keras.layers.Dense(625, activation='sigmoid'),
    tf.keras.layers.Dense(125, activation='sigmoid'),
    tf.keras.layers.Dense(25, activation='sigmoid'),
    tf.keras.layers.Dense(5, activation='sigmoid'),
    tf.keras.layers.Dense(1, activation='linear')
])

model = tf.keras.Sequential([
    tf.keras.layers.Dense(4096, activation='sigmoid', input_shape=(54, )),
    tf.keras.layers.Dense(512, activation='sigmoid'),
    tf.keras.layers.Dense(64, activation='sigmoid'),
    tf.keras.layers.Dense(8, activation='sigmoid'),
    tf.keras.layers.Dense(1, activation='linear')
])

model.compile(optimizer=tf.keras.optimizers.SGD(), loss="mse", metrics=[])

I_O = list()

for i in tqdm.trange(16, ascii=True, position=0):
    for j in tqdm.trange(20000, ascii=True, position=1, leave=False):
        I_O.append((scrambled_cube(i).arr[1:], -i))

random.shuffle(I_O)

inputs = np.asarray([i[0] for i in I_O])
outputs = np.asarray([i[1] for i in I_O])

print(F"\nData: {sys.getsizeof(inputs) :,} bytes (input), {sys.getsizeof(outputs) :,} bytes (output)\n")

history = model.fit(
    inputs,
    outputs,
    epochs=200,
    batch_size=200,
    callbacks=[tf.keras.callbacks.EarlyStopping(monitor="loss", min_delta=0.1, mode="min", restore_best_weights=True)]
)

model.compile(optimizer=tf.keras.optimizers.Adam(), loss="mse", metrics=[])

I_O = list()

for i in tqdm.trange(16, ascii=True, position=0):
    for j in tqdm.trange(20000, ascii=True, position=1, leave=False):
        I_O.append((scrambled_cube(i).arr[1:], -i))

random.shuffle(I_O)

inputs = np.asarray([i[0] for i in I_O])
outputs = np.asarray([i[1] for i in I_O])

print(F"\nData: {sys.getsizeof(inputs) :,} bytes (input), {sys.getsizeof(outputs) :,} bytes (output)\n")

history = model.fit(
    inputs,
    outputs,
    epochs=200,
    batch_size=200
)

if os.path.exists(save_path):
    os.remove(save_path)
    print("Deleted!")

tf.keras.models.save_model(model, save_path, overwrite=True, save_format="hdf5")