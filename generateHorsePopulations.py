import gettersAndSetters as gAS
from objects import getPopulation_0, getPopulation_1
from horse_utils import generateHorsesArray
from utils import generate_two_different_numbers


def reset_parents():
    population_0 = getPopulation_0()
    pop_0 = population_0.pop

    horses = generateHorsesArray(pop_0)

    gAS.setFirstParentId(0)
    gAS.setSecondParentId(1)

    gAS.setFirstParent(horses[0])
    gAS.setSecondParent(horses[1])


def generate_player_population():
    population_0 = getPopulation_0()

    first_parent = gAS.getFirstParent()
    second_parent = gAS.getSecondParent()

    if(first_parent != second_parent):
        population_0.cross_over(
            first_parent.genetics, second_parent.genetics)
        reset_parents()


def generate_ai_population_randomly():
    population_1 = getPopulation_1()

    ab = generate_two_different_numbers(0, population_1.size() - 1)
    pop_1 = population_1.pop
    first_parent_genetics = pop_1[ab[0]]
    second_parent_genetics = pop_1[ab[1]]
    population_1.cross_over(first_parent_genetics, second_parent_genetics)


def generate_ai_population_by_max():
    population_1 = getPopulation_1()
    pop_1 = population_1.pop

    fitnesses = []
    for individual in pop_1:
        fitnesses.append(individual.fitness())
    n = len(pop_1)
    first_max_id = -1
    second_max_id = -1
    for i in range(n):
        if(pop_1[i].fitness() == max(fitnesses)):
            first_max_id = i
            break

    fitnesses[first_max_id] = -1

    for i in range(n):
        if(i != first_max_id and pop_1[i].fitness() == max(fitnesses)):
            second_max_id = i
            break

    first_parent_genetics = pop_1[first_max_id]
    second_parent_genetics = pop_1[second_max_id]
    population_1.cross_over(first_parent_genetics, second_parent_genetics)


def generate_ai_population_by_min():
    population_1 = getPopulation_1()
    pop_1 = population_1.pop

    fitnesses = []
    for individual in pop_1:
        fitnesses.append(individual.fitness())

    n = len(pop_1)

    first_min_id = -1
    second_min_id = -1
    for i in range(n):
        if(pop_1[i].fitness() == min(fitnesses)):
            first_min_id = i
            break

    fitnesses[first_min_id] = 100000000

    for i in range(n):
        if(i != first_min_id and pop_1[i].fitness() == min(fitnesses)):
            second_min_id = i
            break

    first_parent_genetics = pop_1[first_min_id]
    second_parent_genetics = pop_1[second_min_id]
    population_1.cross_over(first_parent_genetics, second_parent_genetics)


def generate_horse_populations():
    generate_player_population()
    generate_ai_population_randomly()
    # generationAIPopulationByMax()
    # generationAIPopulationByMin()
