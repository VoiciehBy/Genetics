
from population import population
from horse_utils import generateHorsesArray

pop = 4

global population_0
global population_1

global population_2
global population_3

population_0 = population(pop)
population_0.generate_initial_population(8, pop)

population_1 = population(pop)
population_1.generate_initial_population(8, pop)

population_2 = population(pop)
population_2.generate_initial_population(8, pop)

population_3 = population(pop)
population_3.generate_initial_population(8, pop)

pop_0 = population_0.pop
horses = generateHorsesArray(pop_0)


def getPopulation_0() -> population:
    return population_0


def getPopulation_1() -> population:
    return population_1


def getPopulation_2() -> population:
    return population_2


def getPopulation_3() -> population:
    return population_3
