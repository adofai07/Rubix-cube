import numpy as np

class Cube:
    def __init__(self):

        self.config = np.array([np.array([[i for _ in range(3)] for _ in range(3)]) for i in range(6)])

        print(self.config.shape)


