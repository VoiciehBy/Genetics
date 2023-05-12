import gettersAndSetters as gAS
from objects import get_population_0
from horse_utils import generate_horses_array
from Game import Game

from constants import HORSES_JSON_FILE_NAME

from logging import jsonify_last_generation

from generateAIPopulation import generate_ai_population_randomly
from generateAIPopulation import generate_ai_population_by_min
from generateAIPopulation import generate_ai_population_by_max

def reset_parents():
    population_0 = get_population_0()
    pop_0 = population_0.get_pop()

    horses = generate_horses_array(pop_0)

    gAS.set_first_parent(horses[0])
    gAS.set_second_parent(horses[1])


def generate_player_population():
    population_0 = get_population_0()

    first_parent = gAS.get_first_parent()
    second_parent = gAS.get_second_parent()

    if(first_parent != second_parent):
        last_generation = population_0.cross_over(
            first_parent.genetics, second_parent.genetics)
        jsonify_last_generation(HORSES_JSON_FILE_NAME, last_generation)

        reset_parents()

        pop_size = len(population_0.get_pop())
        counter = 0
        for individual in last_generation:
            if (counter != pop_size and individual.fitness() == 0):
                counter += 1
            if (counter == pop_size):
                Game.end_game()


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
