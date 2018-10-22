import operator

from src.domain.Individual import Individual
from src.util.AbstractGeneration import AbstractGeneration
from src.util.IndividualsGenerator import IndividualsGenerator

'''
Classe de teste 1 para selecionar a próxima geração da população. Baseado no método da roleta com os
melhores indivíduos da geração anterior.
'''
class RandomGenerationSelector(AbstractGeneration):

    def __init__(self, popsize, evaluator, recombination_rate=0.25, t_max=100):
        super().__init__(popsize, evaluator, recombination_rate, t_max)

    def next_generation(self, individuals):
        pop_fitness = self.evaluate_generation(individuals)

        generator = IndividualsGenerator(len(individuals[0].genotype.dna))
        return generator.generate_random_individuals(len(individuals)), pop_fitness



