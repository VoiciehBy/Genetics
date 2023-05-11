import gettersAndSetters as gAS
from objects import get_population_0, get_population_1
from horse_utils import generate_horses_array
from Game import Game
from utils import generate_two_different_numbers



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

        

        with open("horses.json","a",encoding="utf-8") as file:
            for i in last_generation:
                file.write(i.to_json() + str(",\n"))

        reset_parents()

        counter = 0
        pop_size = len(population_0.get_pop())
        for individual in last_generation:
            if(counter != pop_size and individual.fitness() == 0):
                counter += 1
            if(counter == pop_size):
                with open("horses.json","a",encoding="utf-8") as file:
                    file.write(']\n}')
                txt = ''
                with open("horses.json","r",encoding="utf-8") as file:
                    txt = file.read()
                    n = len(txt)
                    txt = txt[:n-5] + txt[n-4:] 
                with open("horses.json","w",encoding="utf-8") as file:
                    file.write(txt)
                Game.end_game()

def generate_ai_population_randomly():
    population_1 = get_population_1()

    ab = generate_two_different_numbers(0, population_1.size() - 1)
    pop_1 = population_1.get_pop()
    first_parent_genetics = pop_1[ab[0]]
    second_parent_genetics = pop_1[ab[1]]
    last_generation = population_1.cross_over(first_parent_genetics, second_parent_genetics)

    with open("ai_horses.json", "a", encoding="utf-8") as file:
        for i in last_generation:
            file.write(i.to_json() + str(",\n"))


def generate_ai_population_by_max():
    population_1 = get_population_1()
    pop_1 = population_1.get_pop()

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
    population_1 = get_population_1()
    pop_1 = population_1.get_pop()

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
