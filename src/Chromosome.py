from numpy import array, zeros, uint8
from utils import yes_or_no


class Chromosome:
    def __init__(self, length=0, genes=None):
        self.length = length
        if(genes is None):
            self.genes_vector = zeros(self.length, dtype=uint8)
        else:
            self.genes_vector = genes

    def __eq__(self, o) -> bool:
        if(self.length != o.length):
            return False
        else:
            n = self.length
            for i in range(n):
                if(self.genes_vector[i] != o.genes_vector[i]):
                    return False
            return True

    def get_length(self) -> int:
        return int(self.length)

    def get_genes(self) -> array:
        return self.genes_vector

    def fitness(self) -> int:
        c = 0
        for gene in self.genes_vector:
            if gene == 1:
                c += 1
        return int(c)

    def mutate(self):
        n = self.length
        mutation_probability = 1/n
        for i in range(n):
            m = yes_or_no(mutation_probability)
            if m:
                if(self.genes_vector[i] == 0):
                    self.genes_vector[i] = 1
                elif(self.genes_vector[i] == 1):
                    self.genes_vector[i] = 0

    def __str__(self) -> str:
        return str(self.genes_vector)
