"""
Classe abstrata que representa uma geração de uma população. Responsável por avaliar uma populção em relação ao
fitness dela e gerar a próxima geração.
"""
class AbstractGeneration(object):

    def __init__(self, popsize, evaluator, recombination_rate, t_max):
        self.popsize = popsize
        self.evaluator = evaluator
        self.t_max = t_max
        self.r_rate = recombination_rate
        self.max_fitness = -1
        self.found = False

    def evaluate_generation(self, individuals):
        pop_fitness = []
        for individual in individuals:
            fitness, found = self.evaluator.evaluate(individual)
            wrapper = IndividualScoreWrapper(individual, fitness)
            pop_fitness.append(wrapper)
            self.found = self.found or found
        self.max_fitness = max([i.score for i in pop_fitness])
        return pop_fitness

    def next_generation(self, individuals):
        raise NotImplementedError("This class is abstract")

class IndividualScoreWrapper(object):

    def __init__(self, individual, score):
        self.individual = individual
        self.score = score