from numpy import array, zeros
from GChromosome import GChromosome
from GIndividual import GIndividual
from utils import generate_binary_array
from utils import combine as c
import sys


def generate_random_genes(length: int):
    return generate_binary_array(length)


class GPopulation:
    def __init__(self, pop: array):
        self.pop = pop

    def get_pop(self) -> array:
        return self.pop

    def size(self) -> int:
        return int(len(self.pop))

    def set_pop(self, new_population):
        n = int(len(self.pop))
        del self.pop
        self.pop = zeros(n, dtype=GIndividual)
        for i in range(n):
            self.pop[i] = new_population[i]

    def generate_initial_population(self, chromosome_length: int, population_size: int):
        if population_size < 2:
            print("Population size too small", file=sys.stderr)
            return
        self.pop = zeros(population_size, dtype=GIndividual)
        for i in range(population_size):
            genes = generate_random_genes(chromosome_length)
            g = GChromosome(chromosome_length, genes)
            self.pop[i] = GIndividual(genotype=g)

    @staticmethod
    def cross_over(a: GIndividual, b: GIndividual, variant=0) -> array:
        a_length = a.chromosome_length()
        b_length = b.chromosome_length()

        if a_length != b_length:
            print("Not same length", file=sys.stderr)
            return

        h_l = int(a_length/2)

        a_genes = a.genes()
        b_genes = b.genes()

        # Python slicing
        first_half_a = a_genes[:h_l]
        last_half_a = a_genes[h_l:]

        first_half_b = b_genes[:h_l]
        last_half_b = b_genes[h_l:]

        parents = [a, b]
        offsprings = zeros(2, dtype=GIndividual)

        if variant == 0:
            first_chromosome = GChromosome(
                a_length, c(first_half_a, last_half_b))
            first_chromosome.mutate()
            second_chromosome = GChromosome(
                a_length, c(first_half_b, last_half_a))
            second_chromosome.mutate()
        else:
            first_chromosome = GChromosome(
                a_length, c(last_half_b, first_half_a))
            first_chromosome.mutate()
            second_chromosome = GChromosome(
                a_length, c(last_half_a, first_half_b))
            second_chromosome.mutate()

        offsprings[0] = (GIndividual(parents, first_chromosome))
        offsprings[1] = (GIndividual(parents, second_chromosome))

        return offsprings

    def fitness(self) -> int:
        fitness = 0
        for individual in self.pop:
            fitness += individual.individual_fitness()
        return int(fitness)
