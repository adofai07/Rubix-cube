import tensorflow as tf
from type import Cube, scrambled_cube, initial_cube
import tqdm
import random
import numpy as np
import pickle
import os
import sys
from path import checkpoint_path, save_path

print(tf.__version__)
print(tf.config.list_physical_devices('GPU'))

def save(data, thread=0):
    with open(FR"C:\SSHS\codes\Projects\Rubix-cube\G{thread}.adofai", "wb+") as f:
        pickle.dump(data, f)


cp_callback = tf.keras.callbacks.ModelCheckpoint(filepath=checkpoint_path,
                                                 save_weights_only=False,
                                                 verbose=1)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(3125, activation='sigmoid', input_shape=(54, )),
    tf.keras.layers.Dense(625, activation='sigmoid'),
    tf.keras.layers.Dense(125, activation='sigmoid'),
    tf.keras.layers.Dense(25, activation='sigmoid'),
    tf.keras.layers.Dense(5, activation='sigmoid'),
    tf.keras.layers.Dense(1, activation='linear')
])

# Comment this line if this is your first time training
model = tf.keras.models.load_model(save_path)

model.compile(optimizer="Adam", loss="mse", metrics=[])

I_O = list()

for i in tqdm.trange(16, ascii=True, position=0):
    for j in tqdm.trange(10000, ascii=True, position=1, leave=False):
        I_O.append((scrambled_cube(i).arr[1:], -i))

random.shuffle(I_O)

inputs = np.asarray([i[0] for i in I_O])
outputs = np.asarray([i[1] for i in I_O])

print(F"\nData: {sys.getsizeof(inputs) :,} bytes (input), {sys.getsizeof(outputs) :,} bytes (output)\n")

history = model.fit(
    inputs,
    outputs,
    epochs=100,
    batch_size=100,
    # callbacks=[cp_callback]
)

os.remove(save_path)
model.save(save_path)