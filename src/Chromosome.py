from numpy import array, zeros, uint8
from random import choices


class Chromosome:
    def __init__(self, length=0, genes=None):
        self.length = length
        if(genes is None):
            self.genes = zeros(self.length, dtype=uint8)
        else:
            self.genes = genes

    def __eq__(self, o) -> bool:
        if(self.length != o.length):
            return False
        else:
            n = self.length
            for i in range(n):
                if(self.genes[i] != o.genes[i]):
                    return False
            return True

    def get_length(self) -> int:
        return int(self.length)

    def get_genes(self) -> array:
        return self.genes

    def fitness(self) -> int:
        c = 0
        for gene in self.genes:
            if gene == 1:
                c += 1
        return int(c)

    def mutate(self):
        n = self.length
        mutation_probability = 1/n
        m_prime = 1 - mutation_probability
        for i in range(n):
            m = choices([True, False], weights=[
                        mutation_probability, m_prime])[0]
            if(m is True):
                if(self.genes[i] == 0):
                    self.genes[i] = 1
                elif(self.genes[i] == 1):
                    self.genes[i] = 0

    def __str__(self) -> str:
        return str(self.genes)
