import painter
from display import *
from ship import *


# Uses: https://github.com/mcfletch/pyopengl
# Run:
#   pip install PyOpenGL PyOpenGL_accelerate


def update(delta):
    global ship

    # Draw the world
    painter.draw_goal(462, 50, 20)
    painter.draw_asteroid(150, 200, 20)
    painter.draw_asteroid(300, 200, 40)
    painter.draw_asteroid(200, 450, 50)
    painter.draw_asteroid(350, 300, 60)
    painter.draw_asteroid(70, 80, 30)

    # Advance test ship for demonstration purposes
    ship.update(delta)

    # Draw the ship
    painter.draw_ship(ship)


if __name__ == '__main__':
    global ship
    # Creates a test ship with a test (preset) path
    #   Path is a 2D array where each element is [time in seconds, boost direction in degrees]
    #   Boosts are executed in order of increasing time values, with the same acceleration for all boosts.
    #   Boosts only apply acceleration, ship speed is cumulative (more realistic).
    ship = Ship([[0.0, -45],
                 [2.5, -180],
                 [4.5, 35]])

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

    # Start the visualization program
    Display(update, [512, 512], "Spaceship Pathfinding - Calvin Weaver / Abhishek Amberkar / Aakash Shukla")
