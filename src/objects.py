from constants import default_population_size
from Population import Population
from horse_utils import generate_horses_array

population_0 = Population(default_population_size)
population_0.generate_initial_population(8, default_population_size)

population_1 = Population(default_population_size)
population_1.generate_initial_population(8, default_population_size)

pop_0 = population_0.get_pop()
horses = generate_horses_array(pop_0)


def get_population_0() -> Population:
    return population_0


def get_population_1() -> Population:
    return population_1
