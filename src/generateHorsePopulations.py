import objects as o
from objects import get_population_0
from Population import Population
from horse_utils import generate_horses_array
from Game import Game

from constants import HORSES_JSON_FILE_NAME

from g_logging import jsonify_last_generation

from generateAIPopulation import generate_ai_population_randomly
from generateAIPopulation import generate_ai_population_by_min
from generateAIPopulation import generate_ai_population_by_max


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

    if(first_parent != second_parent):

        i_0 = Population.cross_over(first_parent.genetics, second_parent.genetics)
        i_1 = Population.cross_over(first_parent.genetics, second_parent.genetics)

        i_2 = Population.cross_over(third_parent.genetics, fourth_parent.genetics)
        i_3 = Population.cross_over(third_parent.genetics, fourth_parent.genetics)

        last_generation = [i_0, i_1, i_2, i_3]

        jsonify_last_generation(HORSES_JSON_FILE_NAME, last_generation)

        reset_parents()

        population_0.set_pop(last_generation)

        pop_size = len(population_0.get_pop())
        counter = 0
        for individual in last_generation:
            if (counter != pop_size and individual.fitness() == 0):
                counter += 1
            if (counter == pop_size):
                Game.end_game(True)


def generate_ai_population():
    i = 0
    if(i == 0):
        generate_ai_population_randomly()
    elif(i == 1):
        generate_ai_population_by_min()
    else:
        generate_ai_population_by_max()


def generate_horse_populations():
    generate_player_population()
    generate_ai_population()
