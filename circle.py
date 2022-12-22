import numpy as np


class Circle:

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def collidesWith(self, x, y, radius):
        return np.sqrt(pow(self.x - x, 2) + pow(self.y - y, 2)) <= self.r + radius
