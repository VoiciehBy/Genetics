from Chromosome import Chromosome
from numpy import array
from GColor import GColor
from utils import clamp

import json


class Individual:
    count: int = 0

    def __init__(self, parents=None, genotype=Chromosome):
        self.id = Individual.count
        self.parents = parents
        self.genotype = genotype
        Individual.count += 1

    def get_id(self) -> int:
        return int(self.id)

    def individual_fitness(self) -> int:
        return self.genotype.fitness()

    def chromosome_length(self) -> int:
        return self.genotype.get_length()

    def genes(self) -> array:
        return self.genotype.get_genes()

    def get_parents(self) -> list:
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

    def to_json(self) -> str:
        genotype = str(self.genotype)
        parents = self.get_parents()
        if parents:
            result = str(int(parents[0].id)) + ' ' + str(int(parents[1].id))
            parents = result
        else:
            parents = ''
        return json.dumps({"id": self.id, "genes": genotype, "fitness": self.individual_fitness(), "parents": parents})

    def __str__(self) -> str:
        return str(self.id) + ' ' + str(self.genotype)
