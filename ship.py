from math import *


class Ship:

    def __init__(self, path):
        self.path = path
        self.x = 50.0
        self.y = 512.0 - 50.0
        self.xs = 0.0
        self.ys = 0.0
        self.dir = 0.0

    # Advances the ship's speed, direction and location forward by delta (seconds)
    def update(self, delta):
        # Update the path timings
        for n in self.path:
            n[0] -= delta

        # Update the ship's direction if a path node has reached time zero
        while len(self.path) > 0 and self.path[0][0] <= 0:
            self.dir = self.path.pop(0)[1]

        # Update the ship's speed
        self.xs += cos(radians(self.dir)) * 50.0 * delta
        self.ys += sin(radians(self.dir)) * 50.0 * delta

        # Update the ship's location
        self.x += self.xs * delta
        self.y += self.ys * delta

    # Returns a value representing the fitness of the ship's current state.
    #   This function should be called once every frame after calling update, and the returned values should be summed
    #   to produce the total fitness of the ship's assigned path.
    def get_fitness(self):
        # TODO implement this

        # TODO get asteroid and goal locations from a global value in main.py

        # TODO return a really low value if the ship is currently intersecting an asteroid

        # TODO return a really high value if the ship is currently intersecting the goal

        # TODO return a slightly higher value the closer the ship is to the goal, to give the evolutionary algorithm
        #   a gradient to follow for learning

        return 1.0
