import objects as o
from objects import get_population_0
from Population import Population
from horse_utils import generate_horses_array

from g_logging import jsonify_player_last_generation

from generateAIPopulation import generate_ai_genetic_population

from Game import Game


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

    first_parent = o.first_parents[0]
    second_parent = o.first_parents[1]
    third_parent = o.second_parents[0]
    fourth_parent = o.second_parents[1]

    # Python unpacking
    i_0, i_1 = Population.cross_over(first_parent.genetics, second_parent.genetics)
    i_2, i_3 = Population.cross_over(third_parent.genetics, fourth_parent.genetics)

    last_generation = [i_0, i_1, i_2, i_3]

    jsonify_player_last_generation(last_generation)

    reset_parents()

    population_0.set_pop(last_generation)

    pop_size = len(population_0.get_pop())
    counter = 0
    for individual in last_generation:
        b = counter != pop_size
        b = b and individual.individual_fitness() >= 4
        if b:
            counter += 1
        if(counter >= pop_size):
            Game.end_game()


def generate_horse_populations():
    generate_player_population()
    generate_ai_genetic_population()
