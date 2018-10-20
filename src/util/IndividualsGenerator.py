import numpy as np

from src.domain.Genotype import Genotype
from src.domain.Individual import Individual


'''
Classe responsável por gerar uma população aleatória de indivíduos. 
Usada para criar a primeira população de uma geração 
'''
class IndividualsGenerator(object):

    def __init__(self, total_genes):
        self.total_genes = total_genes
        self.individuals = []
        pass

    def generate_random_individuals(self, popsize):

        if self.individuals:
            return self.individuals

        for _ in range(popsize):
            dna = np.random.randint(2, size=self.total_genes)
            genotype = Genotype(dna=dna, m_rate=0.5)
            individual = Individual(genotype)
            self.individuals.append(individual)

        return self.individuals
