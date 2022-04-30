from hashlib import new
from ikt111_games.flappy.bird import Bird
from ikt111_games.flappy.flappy import Flappy
from ikt111_games.flappy.utils import generate_random_force
from ikt111_games.flappy.config import *
import math, random, time

REPRODUCING_PROSENT = 0.1
MUTATION_PROSENT = 1/MAX_POPULATION

game = Flappy()

# generate_random_force(_min=-4, _max=4) : Generate a random force vector with x and y in the interval [_min, _max].
# calculate_euclidian_distance(p, q) : Calculate the euclidian distance between two positions.
# get_angle_between_points(d_x, d_y) : Helper function to calculate an angle between two points.
# calculate_rel_points(scale=0.5) : # List of (angle,radius) pairs.


# Crossover between two parents in pool to generate new genetation.
def new_generation(birds, generation_size):
    # Birds doing the coitus.
    for i in range(generation_size):
        birds[i] = Bird()
        for j in range(MAX_LIFE):
            # Creatring random new genes, default range is -4 to 4 in "generate_random_force".
            birds[i].genes[j] = generate_random_force()

@game.register_ai
def super_ai(birds):
    new_generation(birds, MAX_POPULATION)
    return birds

game.start()
