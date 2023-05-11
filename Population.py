from numpy import array, zeros
from Chromosome import Chromosome
from Individual import Individual
from utils import generate_binary_array
from utils import combine as c


def generate_random_genes(length: int):
    return generate_binary_array(length)


class Population:
    def __init__(self, pop: array):
        self.pop = pop

    def get_pop(self):
        return self.pop

    def size(self) -> int:
        return int(len(self.pop))

    def generate_initial_population(self, chromosome_length: int, population_size: int):
        self.pop = zeros(population_size, dtype=Individual)
        for i in range(population_size):
            genes = generate_random_genes(chromosome_length)
            g = Chromosome(chromosome_length, genes)
            self.pop[i] = (Individual(genotype=g))

    def cross_over(self, a: Individual, b: Individual, variant=0):
        if(a.chromosome_length() != b.chromosome_length()):
            print("Not same length")

        a_length = a.chromosome_length()
        h_l = int(a_length/2)

        # Python slicing
        first_half_a = a.genes()[:h_l]
        last_half_a = a.genes()[h_l:]

        first_half_b = b.genes()[:h_l]
        last_half_b = b.genes()[h_l:]

        parents = [a, b]
        offsprings = zeros(4, dtype=Individual)

        if(variant == 0):
            offsprings[0] = (Individual(
                parents, Chromosome(a_length, c(first_half_a, last_half_b))))

            offsprings[1] = (Individual(
                parents, Chromosome(a_length, c(first_half_b, last_half_a))))

            offsprings[2] = (Individual(parents, Chromosome(
                a_length, c(first_half_a, first_half_b))))

            offsprings[3] = (Individual(
                parents, Chromosome(a_length, c(last_half_a, last_half_b))))
        else:
            offsprings[0] = (Individual(
                parents, Chromosome(a_length, c(last_half_b, first_half_a))))

            offsprings[1] = (Individual(
                parents, Chromosome(a_length, c(last_half_a, first_half_b))))

            offsprings[2] = (Individual(parents, Chromosome(
                a_length, c(first_half_b, first_half_a))))

            offsprings[3] = (Individual(
                parents, Chromosome(a_length, c(last_half_b, last_half_a))))

        #last_generation = self.pop
        # for i in last_generation:
        #    print(i)
        del self.pop
        self.pop = zeros(4, dtype=Individual)
        for i in range(4):
            self.pop[i] = offsprings[i]
        # return last_generation
