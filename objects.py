
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

global first_parent_id
global second_parent_id

first_parent_id = 0
second_parent_id = 1

global first_parent
global second_parent

pop_0 = population_0.pop
horses = generateHorsesArray(pop_0)

first_parent = horses[0]
second_parent = horses[1]
