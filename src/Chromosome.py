from numpy import array, zeros, uint8


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

    def __str__(self) -> str:
        return str(self.genes)
