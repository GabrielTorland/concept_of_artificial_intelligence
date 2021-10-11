
from ikt111_games.flappy.bird import Bird
from ikt111_games.flappy.flappy import Flappy
from ikt111_games.flappy.utils import generate_random_force
from ikt111_games.flappy.config import *
import math, random, time

game = Flappy()

# generate_random_force(_min=-4, _max=4) : Generate a random force vector with x and y in the interval [_min, _max].
# calculate_euclidian_distance(p, q) : Calculate the euclidian distance between two positions.
# get_angle_between_points(d_x, d_y) : Helper function to calculate an angle between two points.
# calculate_rel_points(scale=0.5) : # List of (angle,radius) pairs.

@game.register_ai
def super_ai(birds):
    """ A super AI function!

    There is a 33% chance that:
        1. A bird is replaced by a new, randomly generated one!
        2. A bird has a random gene swapped with a new, randomly generated one!
        3. A bird survives, without changes.
    """

    # Loop through the index of all birds
    for i in range(len(birds)):

        # Generate a random float in the interval [0, 1)
        r = random.random()
        if r < 0.33:
            # Replace birds[i] with a new, random bird
            birds[i] = Bird()

        elif r < 0.66:
            # Generate a random integer in the interval [0, MAX_LIFE - 1]
            r_i = random.randint(0, MAX_LIFE - 1)

            # Replace a random gene in bird[i] with a new, random force vector
            birds[i].genes[r_i] = generate_random_force()

        else:
            # Don't do anything!
            pass
    
    return birds

game.start()
