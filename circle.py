
class Circle:

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def isInside(self, x, y):
        return pow(self.x - x, 2) + pow(self.y - y, 2) <= self.r * self.r
