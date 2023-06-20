from type import Cube, scrambled_cube
import pickle
import numpy as np

with open(F"codes\Projects\Rubix-cube\G1000.adofai", "rb") as f:
    MODEL = pickle.load(f)

def AI_score(x: Cube) -> float:
    prediction = MODEL.predict(np.asarray([x.arr[1:]]), verbose=0)
    return prediction[0, 0]