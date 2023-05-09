from Chromosome import Chromosome
from numpy import array
from GColor import GColor
from utils import clamp


class Individual:
    def __init__(self, parents=None, genotype=Chromosome):
        self.parents = parents
        self.genotype = genotype

    def __eq__(self, o) -> bool:
        return self.genotype == o.genotype

    def fitness(self) -> int:
        return self.genotype.fitness()

    def chromosome_length(self) -> int:
        return self.genotype.get_length()

    def genes(self) -> array:
        return self.genotype.get_genes()

    def get_parents(self):
        return self.parents

    def color_trait(self) -> GColor:
        multiplier = 64
        g = self.genes()
        red = g[0] * 4 + g[1] * 2 + g[2]
        green = g[3] * 4 + g[4] * 2 + g[5]
        blue = g[6] * 4 + g[7] * 2
        red = clamp(red*multiplier, 0, 255)
        green = clamp(green*multiplier, 0, 255)
        blue = clamp(blue*multiplier, 0, 255)
        return GColor(red, green, blue)

    def __str__(self) -> str:
        return str(self.genotype)