import numpy as np

import painter
from circle import Circle
from display import *
from path import Path
from ship import *
from ga import *


# Uses: https://github.com/mcfletch/pyopengl
# Run:
#   pip install PyOpenGL PyOpenGL_accelerate


def update(delta):
    global demoTimer, demoShip, goal, asteroids

    # Draw the world
    painter.draw_goal(goal)
    for asteroid in asteroids:
        painter.draw_asteroid(asteroid)

    demoTimer += delta
    if demoTimer >= 10.0:
        demoTimer = 0.0
        demoShip.reset()

    # Advance test ship for demonstration purposes
    demoShip.update(delta)

    # Draw the ship
    painter.draw_ship(demoShip)


if __name__ == '__main__':
    global demoTimer, demoShip, goal, asteroids
    # Creates a test ship with a test (preset) path
    #   Path is a 2D array where each element is [time in seconds, boost direction in degrees]
    #   Boosts are executed in order of increasing time values, with the same acceleration for all boosts.
    #   Boosts only apply acceleration, ship speed is cumulative (more realistic).
    #demoShip = Ship([[0.0, -45],
    #             [3.5, -100],
    #             [1.5, 35]])

    goal = Circle(462, 200, 20)

    asteroids = [Circle(150, 100, 20),
                 Circle(300, 200, 40),
                 Circle(200, 450, 50),
                 Circle(350, 300, 60),
                 Circle(70, 80, 30)]

    #pop_size = 20
    #ga = GA(chr_size = grid_size)
    #g = ga.genPopulation(min = -5, max = 5,pop_size=pop_size)

    # TODO implement the evolutionary algorithm here
    #
    #   The visualization is only for demonstration purposes and we probably shouldn't visualize every single ship.
    #   Instead, run many generations here behind the scenes and only continue the program after the evolution algorithm
    #   is fully complete.
    #
    #   For every generation:
    #      1. Generate paths based on the previous generation and some randomness
    #      2. Create a ship for every path
    #      3. Loop:
    #      3a.   Run update(delta) for a while on every ship to let the program simulate ship flight
    #            ^^^ delta should be around 1/60 here, for a simulation resolution of 60 updates per second
    #      3b.   Accumulate the values produced by get_fitness for every ship
    #      3c.   Depending on the above delta, loop for the equivalent of ~5 seconds
    #            ^^^ (if delta = 1/60 then loop 300 times)
    #      4. Use the accumulated fitness of each ship to determine the best paths in the generation
    #
    #   Lastly assign the main ship to visualize the best path after a bunch of generations!

    simDelta = 1.0 / 20.0

    population = []
    for i in range(20):
        population.append(Path(8))
    population = np.array(population)

    for generation in range(500):
        print("Generation ", generation, " =======================")

        # Calculate fitness values for all agents
        fitness = np.zeros(len(population))
        for agentIndex in range(len(population)):
            ship = Ship(population[agentIndex])
            for time in np.arange(0.0, 10.0, simDelta):
                ship.update(simDelta)
                fitness[agentIndex] += ship.getCurrentFitness(goal, asteroids) * simDelta

        # Sort population by fitness
        indices = (-fitness).argsort()
        population = population[indices]
        print("Best fitness: ", fitness[indices[0]])

        # Perform crossover
        for i in range(1, len(population)):
            population[i].crossover(population[0])

    demoTimer = 0.0
    demoShip = Ship(population[0])

    # Start the visualization program
    Display(update, [512, 512], "Spaceship Pathfinding - Calvin Weaver / Abhishek Amberkar / Aakash Shukla")
