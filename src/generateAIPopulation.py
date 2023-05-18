from objects import get_population_1
from Population import Population
from Game import Game
from utils import generate_two_different_numbers

from constants import AI_HORSES_JSON_FILE_NAME

from g_logging import jsonify_last_generation

from numpy import array


def look_for_terminal_individuals(last_generation: array, pop_size: int):
    counter = 0
    for individual in last_generation:
        if(counter != pop_size and individual.fitness() == 0):
            counter += 1
        if(counter == pop_size):
            Game.end_game()


def generate_ai_population_randomly():
    population_1 = get_population_1()

    ab = generate_two_different_numbers(0, population_1.size() - 1)
    cd = generate_two_different_numbers(0, population_1.size() - 1)
    pop_1 = population_1.get_pop()
    first_parent_genetics = pop_1[ab[0]]
    second_parent_genetics = pop_1[ab[1]]

    third_parent_genetics = pop_1[cd[0]]
    fourth_parent_genetics = pop_1[cd[1]]

    i_0 = Population.cross_over(first_parent_genetics, second_parent_genetics)
    i_1 = Population.cross_over(first_parent_genetics, second_parent_genetics)

    i_2 = Population.cross_over(third_parent_genetics, fourth_parent_genetics)
    i_3 = Population.cross_over(third_parent_genetics, fourth_parent_genetics)

    last_generation = [i_0, i_1, i_2, i_3]
    population_1.set_pop(last_generation)

    jsonify_last_generation(AI_HORSES_JSON_FILE_NAME, last_generation)

    pop_size = len(population_1.get_pop())
    look_for_terminal_individuals(last_generation, pop_size)


def generate_ai_population_by_max():
    # look here
    generate_ai_population_randomly()


def generate_ai_population_by_min():
    # look here
    generate_ai_population_randomly()
