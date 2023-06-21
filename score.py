from type import Cube, scrambled_cube
import pickle
import numpy as np
import tensorflow as tf
import os

checkpoint_path = os.getenv("APPDATA") + R"\cp.ckpt"

MODEL = tf.keras.Sequential([
    tf.keras.layers.Dense(3125, activation='sigmoid', input_shape=(54, )),
    tf.keras.layers.Dense(625, activation='sigmoid'),
    tf.keras.layers.Dense(125, activation='sigmoid'),
    tf.keras.layers.Dense(25, activation='sigmoid'),
    tf.keras.layers.Dense(5, activation='sigmoid'),
    tf.keras.layers.Dense(1, activation='linear')
])

MODEL.load_weights(checkpoint_path).expect_partial()

def AI_score(x: Cube) -> float:
    prediction = MODEL.predict(np.asarray([x.arr[1:]]), verbose=0)
    return prediction[0, 0]