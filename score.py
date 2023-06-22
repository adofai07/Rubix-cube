from type import Cube, scrambled_cube
import pickle
import numpy as np
import tensorflow as tf
import os
from path import checkpoint_path, save_path

MODEL = tf.keras.models.load_model(save_path)

def AI_score(x: Cube) -> float:
    prediction = MODEL.predict(np.asarray([x.arr[1:]]), verbose=0)
    return prediction[0, 0]