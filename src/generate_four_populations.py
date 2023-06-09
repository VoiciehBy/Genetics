from numpy import array
from constants import default_wild_pop as wild_pop
from constants import default_population_size as pop
from constants import default_horse_name
from constants import default_chromosome_length

from objects import get_population_0, get_population_1
from GPopulation import GPopulation
from g_horse_utils import generate_horses_array, generate_horses_array_with_offset

from constants import horse_image_side as side
from constants import names, margin_x, margin_y

from g_logging import jsonify_player_last_generation, jsonify_ai_last_generation


def generate_four_populations() -> array:
    pop_0 = get_population_0().get_pop()
    pop_1 = get_population_1().get_pop()

    jsonify_player_last_generation(pop_0)
    jsonify_ai_last_generation(pop_1)

    population_2 = GPopulation(wild_pop)
    population_2.generate_initial_population(default_chromosome_length, wild_pop)

    population_3 = GPopulation(wild_pop)
    population_3.generate_initial_population(default_chromosome_length, wild_pop)

    pop_2 = population_2.get_pop()
    pop_3 = population_3.get_pop()

    horses = generate_horses_array(pop_0)
    ponies = generate_horses_array_with_offset(pop_1)

    horses_1 = generate_horses_array_with_offset(
        pop_2, wild_pop, margin_x=int(side), margin_y=0, offset=side*pop + margin_x, offset_1=margin_y/2)

    ponies_1 = generate_horses_array_with_offset(
        pop_3, wild_pop, margin_x=int(side/2), offset=side*pop + pop*margin_x)

    for i in range(pop):
        horses[i].set_name(default_horse_name)
        ponies[i].set_name(names[1])

        horses[i].set_ai(False)
        ponies[i].set_ai(True)

    for i in range(wild_pop):
        horses_1[i].set_name(names[2])
        ponies_1[i].set_name(names[3])

        horses_1[i].set_ai(False)
        ponies_1[i].set_ai(True)

    result = list(horses) + list(ponies) + list(horses_1) + list(ponies_1)
    return array(result)
