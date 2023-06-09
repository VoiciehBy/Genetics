from GPopulation import GPopulation
from random import choices
from numpy import zeros, array
from quest_objects import get_ai_population


def generate_ai_genetic_population():
    population_1: GPopulation = get_ai_population()
    pop_1: array = population_1.get_pop()
    pop_size: int = population_1.size()
    total_fitness: int = population_1.fitness()

    probabilities: array = zeros(pop_size)
    for i in range(pop_size):
        if total_fitness != 0:
            individual_fitness: int = pop_1[i].individual_fitness()
            probabilities[i] = individual_fitness / total_fitness
        else:
            probabilities[i] = 0

    ids = range(pop_size)

    first_parent_genetics = pop_1[choices(ids, weights=probabilities)[0]]
    second_parent_genetics = pop_1[choices(ids, weights=probabilities)[0]]
    third_parent_genetics = pop_1[choices(ids, weights=probabilities)[0]]
    fourth_parent_genetics = pop_1[choices(ids, weights=probabilities)[0]]

    # Python unpacking
    i_0, i_1 = GPopulation.cross_over(
        first_parent_genetics, second_parent_genetics)
    i_2, i_3 = GPopulation.cross_over(
        third_parent_genetics, fourth_parent_genetics)

    last_generation = [i_0, i_1, i_2, i_3]

    population_1.set_pop(last_generation)

    return last_generation
