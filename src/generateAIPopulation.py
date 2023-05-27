from objects import get_population_1
from Population import Population

from g_logging import jsonify_ai_last_generation
from random import choices
from numpy import zeros, array
from numpy import sum as numpy_sum

from Game import Game


def generate_ai_genetic_population():
    population_1: Population = get_population_1()
    pop_1: array = population_1.get_pop()
    n: int = population_1.size()
    total_fitness: int = population_1.fitness()

    probabilities: array = zeros(n)
    for i in range(n):
        if(total_fitness != 0):
            individual_fitness: int = pop_1[i].individual_fitness()
            probabilities[i] = individual_fitness / total_fitness
        else:
            probabilities[i] = 0

    ids = []
    for i in range(population_1.size()):
        ids.append(i)

    if (numpy_sum(probabilities) == 0):
        probabilities = []
        for i in range(n):
            probabilities.append(float(1 / n))

    first_parent_genetics_pop_id = choices(ids, weights=probabilities)[0]
    second_parent_genetics_pop_id = choices(ids, weights=probabilities)[0]
    third_parent_genetics_pop_id = choices(ids, weights=probabilities)[0]
    fourth_parent_genetics_pop_id = choices(ids, weights=probabilities)[0]

    first_parent_genetics = pop_1[first_parent_genetics_pop_id]
    second_parent_genetics = pop_1[second_parent_genetics_pop_id]
    third_parent_genetics = pop_1[third_parent_genetics_pop_id]
    fourth_parent_genetics = pop_1[fourth_parent_genetics_pop_id]

    # Python unpacking
    i_0, i_1 = Population.cross_over(
        first_parent_genetics, second_parent_genetics)
    i_2, i_3 = Population.cross_over(
        third_parent_genetics, fourth_parent_genetics)

    last_generation = [i_0, i_1, i_2, i_3]
    population_1.set_pop(last_generation)

    jsonify_ai_last_generation(last_generation)

    pop_size = len(population_1.get_pop())
    counter = 0
    for individual in last_generation:
        b = counter != pop_size
        b = b and individual.individual_fitness() >= 4
        if b:
            counter += 1
        if (counter >= pop_size):
            Game.end_game(True)
