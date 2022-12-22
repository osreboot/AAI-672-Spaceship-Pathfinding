import numpy as np

from circle import Circle


def world_simple():
    start = [50.0, 256.0]
    goal = Circle(512.0 - 50.0, 256.0, 20)
    asteroids = [Circle(256.0, 256.0, 100)]
    return [start, goal, asteroids]

def world_difficult():
    start = [50.0, 512.0 - 50.0]
    goal = Circle(462, 200, 20)
    asteroids = [Circle(150, 100, 20),
                 Circle(300, 200, 40),
                 Circle(200, 450, 50),
                 Circle(350, 300, 60),
                 Circle(70, 80, 30)]
    return [start, goal, asteroids]

def world_zigzag():
    start = [256.0, 512.0 - 50.0]
    goal = Circle(256.0, 50.0, 20)
    asteroids = []
    for x in np.arange(212.0, 512.0 - 10.0, 40.0):
        asteroids.append(Circle(x, 256.0 + 100.0, 20.0))
        asteroids.append(Circle(512.0 - x, 256.0 - 100.0, 20.0))

    return [start, goal, asteroids]

def world_precision():
    start = [50.0, 256.0]
    goal = Circle(512.0 - 50.0, 256.0, 20)
    asteroids = []
    for y in np.arange(20.0, 260.0, 60.0):
        asteroids.append(Circle(256.0, y, 40.0))
        asteroids.append(Circle(256.0, 512.0 - y, 40.0))

    return [start, goal, asteroids]