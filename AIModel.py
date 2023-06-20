import tensorflow as tf
from type import Cube, scrambled_cube, initial_cube
import tqdm
import random
import numpy as np
import pickle
import os

def save(data, thread=0):
    with open(F"C:/SSHS/codes/Data/G{thread}.adofai", "wb+") as f:
        pickle.dump(data, f)

def load(thread=0):
    while True:
        try:
            with open(F"C:/SSHS/codes/Data/G{thread}.adofai", "rb") as f:
                return pickle.load(f)
            
        except:
            ...

model = tf.keras.Sequential([
    tf.keras.layers.Dense(3125, activation='sigmoid', input_shape=(54, )),
    tf.keras.layers.Dense(625, activation='sigmoid'),
    tf.keras.layers.Dense(125, activation='sigmoid'),
    tf.keras.layers.Dense(25, activation='sigmoid'),
    tf.keras.layers.Dense(5, activation='sigmoid'),
    tf.keras.layers.Dense(1, activation='linear')
])

model.compile(optimizer="Adam", loss="mse", metrics=[])

I_O = list()

for i in tqdm.trange(16, ascii=True, position=0):
    for j in tqdm.trange(50000, ascii=True, position=1, leave=False):
        I_O.append((scrambled_cube(i).arr[1:], -i))

random.shuffle(I_O)

inputs = np.asarray([i[0] for i in I_O])
outputs = np.asarray([i[1] for i in I_O])

history = model.fit(inputs, outputs, epochs=50, batch_size=50)

save(model, 1000)
