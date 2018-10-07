import numpy as np

from src.domain.Genotype import Genotype
from src.domain.Individual import Individual


class IndividualsGenerator(object):

    def __init__(self, total_genes):
        self.total_genes = total_genes
        pass

    def generate_random_individuals(self, popsize):
        individuals = []

        for _ in range(popsize):
            dna = np.random.randint(2, size=self.total_genes)
            genotype = Genotype(dna=dna, m_rate=0.5)
            individual = Individual(genotype)
            individuals.append(individual)

        return individuals
