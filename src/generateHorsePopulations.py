import objects as o
from objects import get_population_0
from Population import Population
from horse_utils import generate_horses_array
from g_logging import jsonify_player_last_generation
from objects import get_population_1
from g_logging import jsonify_ai_last_generation
from random import choices
from numpy import zeros, array
from Game import Game
from constants import default_goal_evaluation_value as goal_value


def end_game_if_goal_population_is_present(last_generation, pop_size, is_ai_victorious=False):
    counter = 0
    for individual in last_generation:
        b = counter != pop_size
        b = b and individual.individual_fitness() == goal_value
        if b:
            counter += 1
        if (counter >= pop_size):
            Game.end_game(is_ai_victorious)


def generate_ai_genetic_population():
    population_1: Population = get_population_1()
    pop_1: array = population_1.get_pop()
    pop_size: int = population_1.size()
    total_fitness: int = population_1.fitness()

    probabilities: array = zeros(pop_size)
    for i in range(pop_size):
        if(total_fitness != 0):
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
    i_0, i_1 = Population.cross_over(
        first_parent_genetics, second_parent_genetics)
    i_2, i_3 = Population.cross_over(
        third_parent_genetics, fourth_parent_genetics)

    last_generation = [i_0, i_1, i_2, i_3]
    jsonify_ai_last_generation(last_generation)
    population_1.set_pop(last_generation)
    end_game_if_goal_population_is_present(last_generation, pop_size, True)


def reset_parents():
    population_0 = get_population_0()
    pop_0 = population_0.get_pop()

    horses = generate_horses_array(pop_0)

    o.set_first_parent(horses[0])
    o.set_second_parent(horses[1])
    o.set_third_parent(horses[2])
    o.set_fourth_parent(horses[3])


def generate_player_population():
    population_0 = get_population_0()
    pop_size: int = population_0.size()

    first_parent = o.first_parents[0]
    second_parent = o.first_parents[1]
    third_parent = o.second_parents[0]
    fourth_parent = o.second_parents[1]

    # Python unpacking
    i_0, i_1 = Population.cross_over(
        first_parent.genetics, second_parent.genetics)
    i_2, i_3 = Population.cross_over(
        third_parent.genetics, fourth_parent.genetics)

    reset_parents()

    last_generation = [i_0, i_1, i_2, i_3]
    jsonify_player_last_generation(last_generation)
    population_0.set_pop(last_generation)
    end_game_if_goal_population_is_present(last_generation, pop_size)


def generate_horse_populations():
    generate_player_population()
    generate_ai_genetic_population()
