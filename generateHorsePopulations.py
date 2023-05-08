import gettersAndSetters as gAS
from objects import getPopulation_0, getPopulation_1, getPopulation_2, getPopulation_3
from horse_utils import generateHorsesArray
from utils import generateTwoDifferentNumbers


def resetParents():
    population_0 = getPopulation_0()
    pop_0 = population_0.pop

    horses = generateHorsesArray(pop_0)

    gAS.setFirstParentId(0)
    gAS.setSecondParentId(1)

    gAS.setFirstParent(horses[0])
    gAS.setSecondParent(horses[1])


def generatePlayerPopulation():
    population_0 = getPopulation_0()

    first_parent = gAS.getFirstParent()
    second_parent = gAS.getSecondParent()

    if(first_parent != second_parent):
        population_0.cross_over(
            first_parent.genetics, second_parent.genetics)
        resetParents()


def generationAIPopulationRandomly():
    population_1 = getPopulation_1()

    ab = generateTwoDifferentNumbers(0, population_1.size()-1)
    pop_1 = population_1.pop
    first_parent_genetics = pop_1[ab[0]]
    second_parent_genetics = pop_1[ab[1]]
    population_1.cross_over(first_parent_genetics, second_parent_genetics)


def generationAIPopulationByMax():
    population_1 = getPopulation_1()
    pop_1 = population_1.pop

    fitnesses = []
    for individual in pop_1:
        fitnesses.append(individual.fitness())
    n = len(pop_1)
    first_max = -1
    first_max_id = -1
    second_max = -1
    second_max_id = -1
    for i in range(n):
        if(pop_1[i].fitness() == max(fitnesses)):
            first_max = pop_1[i].fitness()
            first_max_id = i
            break

    fitnesses[first_max_id] = -1

    for i in range(n):
        if(i != first_max_id and pop_1[i].fitness() == max(fitnesses)):
            second_max = pop_1[i].fitness()
            second_max_id = i
            break

    first_parent_genetics = pop_1[first_max_id]
    second_parent_genetics = pop_1[second_max_id]
    population_1.cross_over(first_parent_genetics, second_parent_genetics)


def generationAIPopulationByMin():
    population_1 = getPopulation_1()
    pop_1 = population_1.pop

    fitnesses = []
    for individual in pop_1:
        fitnesses.append(individual.fitness())

    n = len(pop_1)

    first_min = -1
    first_min_id = -1
    second_min = -1
    second_min_id = -1
    for i in range(n):
        if(pop_1[i].fitness() == min(fitnesses)):
            first_max = pop_1[i].fitness()
            first_min_id = i
            break

    fitnesses[first_min_id] = 100000000

    for i in range(n):
        if(i != first_min_id and pop_1[i].fitness() == min(fitnesses)):
            second_min = pop_1[i].fitness()
            second_min_id = i
            break

    first_parent_genetics = pop_1[first_min_id]
    second_parent_genetics = pop_1[second_min_id]
    population_1.cross_over(first_parent_genetics, second_parent_genetics)


def generateHorsePopulations():
    generatePlayerPopulation()
    generationAIPopulationRandomly()
    # generationAIPopulationByMax()
    # generationAIPopulationByMin()
