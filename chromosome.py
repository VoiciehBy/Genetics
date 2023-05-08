from numpy import zeros, uint8


class chromosome:
    def __init__(self, length=0, genes=zeros):
        self.length = length
        self.genes = zeros(self.length, dtype=uint8)
        self.genes = genes

    def __eq__(self, o) -> bool:
        return self.length == o.length and (self.genes == o.genes).all()

    def fitness(self) -> int:
        c = 0
        for gene in self.genes:
            if gene == 1:
                c = c + 1
        return int(c)

    def __str__(self) -> str:
        return str(self.genes)
