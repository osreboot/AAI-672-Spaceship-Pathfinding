import numpy as np

import painter
from circle import Circle
from display import *
from path import Path
from ship import *
from ga import *
import worlds


# Uses: https://github.com/mcfletch/pyopengl
# Run:
#   pip install PyOpenGL PyOpenGL_accelerate


def update(delta):
    global deltaSim, demoTimer, demoShip, demoTrail, goal, asteroids

    # Draw the world i.e goal(end point)
    painter.draw_goal(goal)
    for asteroid in asteroids:
        painter.draw_asteroid(asteroid)

    demoTimer += deltaSim
    if demoTimer >= 10.0:
        demoTimer = 0.0
        demoShip.reset()

    # Advance test ship for demonstration purposes
    demoShip.update(deltaSim)

    # Draw the ship
    painter.draw_ship(demoShip)

    # Draw a ship trail
    painter.draw_trail(demoTrail, int(demoTimer / deltaSim))


if __name__ == '__main__':

    global deltaSim, demoTimer, demoShip, demoTrail, start, goal, asteroids
    # Creates a test ship with a test (preset) path
    

    #Creates Start Points, End Points and Obstacles (Asteroids)
    [start, goal, asteroids] = worlds.world_simple()

    #   Path is a 2D array where each element is [time in seconds, boost direction in degrees]
    #   Boosts are executed in order of increasing time values, with the same acceleration for all boosts.
    #   Boosts only apply acceleration, ship speed is cumulative (more realistic).

    deltaSim = 1.0 / 20.0
    population_size = 50

    population = []
    for i in range(population_size):
        population.append(Path(6))
    population = np.array(population)

    for generation in range(200):
        print("Generation ", generation, " =======================")

        # Calculate fitness values for all agents
        fitness = np.zeros(len(population))
        for agentIndex in range(len(population)):
            ship = Ship(start, population[agentIndex])
            for time in np.arange(0.0, 10.0, deltaSim):
                ship.update(deltaSim)
                fitness[agentIndex] += ship.getCurrentFitness(goal, asteroids) * deltaSim

        # Sort population by fitness
        indices = (-fitness).argsort()
        population = population[indices]
        print("Best fitness: ", fitness[indices[0]])

        # # Standard single dominant agent crossover (crossover happens with only top agent for all others)
        # for i in range(1, len(population)):
        #     population[i].crossover(population[0])

        # Cyclic crossover (each top agent has its own crossover batch further down the list)
        numParents = int(len(population) / 5)
        for i in range(numParents, len(population)):
            population[i].crossover(population[int((i - numParents) / 5)])

        # # Pairs crossover (1->2, 2->3, etc)
        # for i in range(len(population)):
        #     if i % 2 == 1:
        #         population[i].crossover(population[i - 1])

    demoTimer = 0.0
    demoShip = Ship(start, population[0])

    demoTrail = np.zeros([int(10.0 / deltaSim), 2])
    for i in range(0, int(10.0 / deltaSim)):
        demoShip.update(deltaSim)
        demoTrail[i] = [float(demoShip.x), float(demoShip.y)]

    demoShip.reset()

    #   Start the visualization program
    #   The visualization is only for demonstration purposes and we did't visualize every single ship.
    #   Instead, ran many generations here behind the scenes and only visulized the ship after the evolution algorithm
    #   is fully complete.
    Display(update, deltaSim, [512, 512], "Spaceship Pathfinding - Calvin Weaver / Abhishek Amberkar / Aakash Shukla")
