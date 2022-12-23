import copy
from math import *


class Ship:

    def __init__(self, start, path):
        self.radius = 6.0

        self.start = start
        self.path = copy.deepcopy(path)
        self.path.values.sort()
        self.pathInit = copy.deepcopy(self.path)
        self.x = self.start[0]
        self.y = self.start[1]
        self.xs = 0.0
        self.ys = 0.0
        self.dir = 0.0

    def reset(self):
        self.path = copy.deepcopy(self.pathInit)
        self.x = self.start[0]
        self.y = self.start[1]
        self.xs = 0.0
        self.ys = 0.0
        self.dir = 0.0

    # Advances the ship's speed, direction and location forward by delta (seconds)
    def update(self, delta):
        # Update the path timings
        for n in self.path.values:
            n[0] -= delta

        # Update the ship's direction if a path node has reached time zero
        while len(self.path.values) > 0 and self.path.values[0][0] <= 0:
            self.dir = self.path.values.pop(0)[1]

        # Update the ship's speed
        self.xs += cos(radians(self.dir)) * 50.0 * delta
        self.ys += sin(radians(self.dir)) * 50.0 * delta

        # Update the ship's location
        self.x += self.xs * delta
        self.y += self.ys * delta

    # Returns a value representing the fitness of the ship's current state.
    #   This function should be called once every frame after calling update, 
    #   and the returned values should be summed
    #   to produce the total fitness of the ship's assigned path.
    def getCurrentFitness(self, goal, asteroids):
        fitness = 0.0

        # Being offscreen hurts
        if (not self.radius < self.x < 512.0 - self.radius or
                not self.radius < self.y < 512.0 - self.radius):
            fitness -= 100000000.0

        # Asteroids hurt
        for asteroid in asteroids:
            if asteroid.collidesWith(self.x, self.y, self.radius):
                fitness -= 100000000.0

        # Reward for reaching the goal
        if goal.collidesWith(self.x, self.y, self.radius):
            fitness += 1000.0

        # Being far from the goal hurts a tiny bit
        fitness -= (pow(self.x - goal.x, 2) + pow(self.y - goal.y, 2)) * 0.001

        return fitness
