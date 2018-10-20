"""
Responsável por avaliar o fitness de um determinado indivíduo
"""
class FitnessEvaluator(object):

    def __init__(self, weights, size):
        self.weights = weights
        self.size = size

    def evaluate(self, individual):
        found = False
        knapsack_sum = int(sum([x*y for (x, y) in zip(individual.genotype.dna, self.weights)]))
        if knapsack_sum > self.size:
            return -1, found
        if knapsack_sum == self.size:
            found = True
            print([y for (x, y) in zip(individual.genotype.dna, self.weights) if x > 0])
        return knapsack_sum, found
