from objects import get_population_1
from Game import Game
from utils import generate_two_different_numbers

from constants import AI_HORSES_JSON_FILE_NAME

from g_logging import jsonify_last_generation

import numpy


def f(last_generation, pop_size):
    counter = 0
    for individual in last_generation:
        if(counter != pop_size and individual.fitness() == 0):
            counter += 1
        if(counter == pop_size):
            Game.end_game()


def generate_ai_population_randomly():
    population_1 = get_population_1()

    ab = generate_two_different_numbers(0, population_1.size() - 1)
    pop_1 = population_1.get_pop()
    first_parent_genetics = pop_1[ab[0]]
    second_parent_genetics = pop_1[ab[1]]
    last_generation = population_1.cross_over(
        first_parent_genetics, second_parent_genetics)

    jsonify_last_generation(AI_HORSES_JSON_FILE_NAME, last_generation)

    pop_size = len(population_1.get_pop())
    f(last_generation, pop_size)


def generate_ai_population_by_max():
    population_1 = get_population_1()
    pop_1 = population_1.get_pop()
    n = len(pop_1)

    fitnesse = numpy.zeros(n, dtype=numpy.uint8)

    for i in range(n):
        fitnesse[i] = pop_1[i].fitness()

    first_max_id = -1
    second_max_id = -1

    for i in range(n):
        if(pop_1[i].fitness() == numpy.max(fitnesse)):
            first_max_id = i
            break

    for i in range(n):
        if(i != first_max_id and pop_1[i].fitness() == numpy.max(fitnesse)):
            second_max_id = i
            break

    first_parent_genetics = pop_1[first_max_id]
    second_parent_genetics = pop_1[second_max_id]
    last_generation = population_1.cross_over(
        first_parent_genetics, second_parent_genetics)

    jsonify_last_generation(AI_HORSES_JSON_FILE_NAME, last_generation)

    pop_size = len(population_1.get_pop())
    f(last_generation, pop_size)


def generate_ai_population_by_min():
    population_1 = get_population_1()
    pop_1 = population_1.get_pop()
    n = len(pop_1)

    fitnesse = numpy.zeros(n, dtype=numpy.uint8)

    for i in range(n):
        fitnesse[i] = pop_1[i].fitness()

    first_min_id = -1
    second_min_id = -1

    for i in range(n):
        if(pop_1[i].fitness() == numpy.min(fitnesse)):
            first_min_id = i
            break

    for i in range(n):
        if(i != first_min_id and pop_1[i].fitness() == numpy.min(fitnesse)):
            second_min_id = i
            break

    first_parent_genetics = pop_1[first_min_id]
    second_parent_genetics = pop_1[second_min_id]
    last_generation = population_1.cross_over(
        first_parent_genetics, second_parent_genetics)
    jsonify_last_generation(AI_HORSES_JSON_FILE_NAME, last_generation)

    pop_size = len(population_1.get_pop())
    f(last_generation, pop_size)
