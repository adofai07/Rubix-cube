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


act1 = "tanh"
act2 = "relu"
act3 = "linear"

model = tf.keras.Sequential([
    tf.keras.layers.Dense(7776, activation=act1, input_shape=(54, )),
    tf.keras.layers.Dense(1296, activation=act2),
    tf.keras.layers.Dense(216, activation=act1),
    tf.keras.layers.Dense(36, activation=act2),
    tf.keras.layers.Dense(6, activation=act1),
    tf.keras.layers.Dense(1, activation=act3)
])

model.compile(
    optimizer=tf.keras.optimizers.SGD(),
    loss="mse",
    metrics=[
            tf.keras.metrics.MeanAbsoluteError(name="MAerr"),
            tf.keras.metrics.MeanAbsolutePercentageError(name="MAPerr")
        ]
)

I_O = list()

for i in tqdm.trange(8, 19, ascii=True, position=0):
    for j in tqdm.trange(40000, ascii=True, position=1, leave=False):
        I_O.append((scrambled_cube(i).arr[1:], -i))

random.shuffle(I_O)

inputs = np.asarray([i[0] for i in I_O])
outputs = np.asarray([i[1] for i in I_O])

print(F"\nData: {sys.getsizeof(inputs) :,} bytes (input), {sys.getsizeof(outputs) :,} bytes (output)\n")

history = model.fit(
    inputs,
    outputs,
    epochs=5,
    batch_size=5
)

model.compile(
    optimizer=tf.keras.optimizers.Adam(),
    loss="mse",
    metrics=[
            tf.keras.metrics.MeanAbsoluteError(name="MAerr"),
            tf.keras.metrics.MeanAbsolutePercentageError(name="MAPerr")
        ]
)

print(model.optimizer)

I_O = list()

for i in tqdm.trange(8, 19, ascii=True, position=0):
    for j in tqdm.trange(400000, ascii=True, position=1, leave=False):
        I_O.append((scrambled_cube(i).arr[1:], -i))

random.shuffle(I_O)

inputs = np.asarray([i[0] for i in I_O])
outputs = np.asarray([i[1] for i in I_O])

print(F"\nData: {sys.getsizeof(inputs) :,} bytes (input), {sys.getsizeof(outputs) :,} bytes (output)\n")

history = model.fit(
    inputs,
    outputs,
    epochs=2000,
    batch_size=2000
)

if os.path.exists(save_path):
    os.remove(save_path)
    print("Deleted!")

tf.keras.models.save_model(model, save_path, overwrite=True, save_format="hdf5")