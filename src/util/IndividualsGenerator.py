import numpy as np

from src.domain.Genotype import Genotype
from src.domain.Individual import Individual


class IndividualsGenerator(object):

    def __init__(self):
        pass

    def generate_random_individuals(self, popsize, total_genes):
        individuals = []

        for _ in range(popsize):
            dna = np.random.randint(2, size=total_genes)
            genotype = Genotype(dna=dna, m_rate=0.5)
            individual = Individual(genotype)
            individuals.append(individual)

        return individuals
