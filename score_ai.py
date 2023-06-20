import tensorflow as tf
from type import Cube, scrambled_cube, initial_cube
import tqdm
import random

model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(54, )),
    tf.keras.layers.Dense(4, activation='relu'),
    tf.keras.layers.Dense(1, activation='softmax')
])

model.compile(optimizer="Adam", loss="mse", metrics=["accuracy"])

I_O = [(initial_cube(), 1000)]

for i in tqdm.trange(1, 16, ascii=True, position=0):
    for j in tqdm.trange(100000, ascii=True, position=1, leave=False):
        I_O.append((scrambled_cube(i), -i))

random.shuffle(I_O)

