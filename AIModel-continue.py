import tensorflow as tf
from type import Cube, scrambled_cube, initial_cube
import tqdm
import random
import numpy as np
import pickle
import os
import sys

print(tf.__version__)
print(tf.config.list_physical_devices('GPU'))

def save(data, thread=0):
    with open(FR"C:\SSHS\codes\Projects\Rubix-cube\G{thread}.adofai", "wb+") as f:
        pickle.dump(data, f)

checkpoint_path = os.getenv("APPDATA") + R"\cp.ckpt"

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

# model = tf.keras.Sequential([
#     tf.keras.layers.Dense(4500, activation='sigmoid', input_shape=(54, )),
#     tf.keras.layers.Dense(900, activation='sigmoid'),
#     tf.keras.layers.Dense(150, activation='sigmoid'),
#     tf.keras.layers.Dense(30, activation='sigmoid'),
#     tf.keras.layers.Dense(5, activation='sigmoid'),
#     tf.keras.layers.Dense(1, activation='linear')
# ])

model.compile(optimizer="Adam", loss="mse", metrics=[])
model.load_weights(checkpoint_path).expect_partial()

I_O = list()

for i in tqdm.trange(16, ascii=True, position=0):
    for j in tqdm.trange(1000000, ascii=True, position=1, leave=False):
        I_O.append((scrambled_cube(i).arr[1:], -i))

random.shuffle(I_O)

inputs = np.asarray([i[0] for i in I_O])
outputs = np.asarray([i[1] for i in I_O])

print(F"\nData: {sys.getsizeof(inputs)} bytes (input), {sys.getsizeof(outputs)} bytes (output)\n")

history = model.fit(inputs, outputs, epochs=1000, batch_size=1000, callbacks=[cp_callback])
