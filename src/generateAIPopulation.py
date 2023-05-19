from objects import get_population_1
from Population import Population

from g_logging import jsonify_ai_last_generation
from random import choices
from numpy import zeros
from numpy import sum as numpy_sum

from Game import Game


def generate_ai_genetic_population():
    population_1 = get_population_1()
    pop_1 = population_1.get_pop()
    n = population_1.size()
    total_fitness = population_1.fitness()

    probabilities = zeros(n)
    for i in range(n):
        if(total_fitness != 0):
            probabilities[i] = pop_1[i].fitness() / total_fitness
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

    temp_probabilities = []
    temp_total_fitness = total_fitness - \
        pop_1[first_parent_genetics_pop_id].fitness()
    temp_ids = []

    for i in range(n):
        if(i != first_parent_genetics_pop_id):
            temp_ids.append(i)

    for i in temp_ids:
        if (temp_total_fitness != 0):
            temp_probabilities.append(pop_1[i].fitness() / temp_total_fitness)
        else:
            temp_probabilities.append(0)

    if(numpy_sum(temp_probabilities) == 0):
        temp_probabilities = []
        x = int(n - 1)
        for i in range(x):
            temp_probabilities.append(1/x)

    second_parent_genetics_pop_id = choices(
        temp_ids, weights=temp_probabilities)[0]
    third_parent_genetics_pop_id = choices(ids, weights=probabilities)[0]

    temp_probabilities = []
    temp_total_fitness = total_fitness - \
        pop_1[third_parent_genetics_pop_id].fitness()
    temp_ids = []

    for i in range(n):
        if (i != third_parent_genetics_pop_id):
            temp_ids.append(i)

    for i in temp_ids:
        if (temp_total_fitness != 0):
            temp_probabilities.append(pop_1[i].fitness() / temp_total_fitness)
        else:
            temp_probabilities.append(0)

    if (numpy_sum(temp_probabilities) == 0):
        temp_probabilities = []
        x = int(n - 1)
        for i in range(x):
            temp_probabilities.append(1/x)

    fourth_parent_genetics_pop_id = choices(
        temp_ids, weights=temp_probabilities)[0]

    first_parent_genetics = pop_1[first_parent_genetics_pop_id]
    second_parent_genetics = pop_1[second_parent_genetics_pop_id]
    third_parent_genetics = pop_1[third_parent_genetics_pop_id]
    fourth_parent_genetics = pop_1[fourth_parent_genetics_pop_id]

    i_0 = Population.cross_over(first_parent_genetics, second_parent_genetics)
    i_1 = Population.cross_over(first_parent_genetics, second_parent_genetics)

    i_2 = Population.cross_over(third_parent_genetics, fourth_parent_genetics)
    i_3 = Population.cross_over(third_parent_genetics, fourth_parent_genetics)

    last_generation = [i_0, i_1, i_2, i_3]
    population_1.set_pop(last_generation)

    jsonify_ai_last_generation(last_generation)

    pop_size = len(population_1.get_pop())
    counter = 0
    for individual in last_generation:
        if (counter != pop_size and individual.fitness() == 0):
            counter += 1
        if (counter == pop_size):
            Game.end_game()
