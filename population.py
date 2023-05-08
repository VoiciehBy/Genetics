

import numpy
from chromosome import chromosome
from individual import individual
from utils import generateBinaryArray
from utils import combine as c


def generateRandomGenes(length):
    return generateBinaryArray(length)


class population():
    def __init__(self, pop):
        self.pop = pop

    def size(self) -> int:
        return int(len(self.pop))

    def generate_initial_population(self, chromosome_length, population_size):
        self.pop = numpy.zeros(population_size, dtype=individual)
        for i in range(population_size):
            genes = generateRandomGenes(chromosome_length)
            g = chromosome(chromosome_length, genes)
            self.pop[i] = (individual(genotype=g))

    def cross_over(self, a, b, variant=0):
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
        offsprings = numpy.zeros(4, dtype=individual)

        if(variant == 0):
            offsprings[0] = (individual(
                parents, chromosome(a_length, c(first_half_a, last_half_b))))

            offsprings[1] = (individual(
                parents, chromosome(a_length, c(first_half_b, last_half_a))))

            offsprings[2] = (individual(parents, chromosome(
                a_length, c(first_half_a, first_half_b))))

            offsprings[3] = (individual(
                parents, chromosome(a_length, c(last_half_a, last_half_b))))
        else:
            offsprings[0] = (individual(
                parents, chromosome(a_length, c(last_half_b, first_half_a))))

            offsprings[1] = (individual(
                parents, chromosome(a_length, c(last_half_a, first_half_b))))

            offsprings[2] = (individual(parents, chromosome(
                a_length, c(first_half_b, first_half_a))))

            offsprings[3] = (individual(
                parents, chromosome(a_length, c(last_half_b, last_half_a))))

        #last_generation = self.pop
        # for i in last_generation:
        #    print(i)
        del self.pop
        self.pop = numpy.zeros(4, dtype=individual)
        for i in range(4):
            self.pop[i] = offsprings[i]
        # return last_generation
