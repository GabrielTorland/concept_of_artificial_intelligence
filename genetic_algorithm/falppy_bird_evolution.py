
from hashlib import new
from ikt111_games.flappy.bird import Bird
from ikt111_games.flappy.flappy import Flappy
from ikt111_games.flappy.utils import generate_random_force
from ikt111_games.flappy.config import *
import math, random, time

REPRODUCING_PERCENT = 0.1 # 10 percent.
MUTATION_PERCENT = 1/MAX_POPULATION 

game = Flappy()

# generate_random_force(_min=-4, _max=4) : Generate a random force vector with x and y in the interval [_min, _max].
# calculate_euclidian_distance(p, q) : Calculate the euclidian distance between two positions.
# get_angle_between_points(d_x, d_y) : Helper function to calculate an angle between two points.
# calculate_rel_points(scale=0.5) : # List of (angle,radius) pairs.


# Crossover between two parents in pool to generate new genetation.
def new_generation(birds, parent_pool, generation_size):
    for i in range(generation_size):
        # Chosing parents
        father = random.choice(parent_pool)
        mother = random.choice(parent_pool)
        birds[i] = Bird()
        for j in range(MAX_LIFE):
            state = random.uniform(0, 1)
            # Randomly choosing between fathers genotype and mothers genortype.
            birds[i].genes[j] = random.choice([father.genes[j], mother.genes[j]])
            # Random mutation.
            if state < MUTATION_PERCENT:
                birds[i].genes[j] = generate_random_force()


# Pool for parents with highest fitness score.
def pool(birds):
    birds.sort(key=lambda x: x.fitness)
    length = len(birds)
    return birds[math.floor(length-length*REPRODUCING_PERCENT)::]


@game.register_ai
def super_ai(birds):
    parent_pool = pool(birds)
    new_generation(birds, parent_pool, MAX_POPULATION)
    
    return birds

game.start()
