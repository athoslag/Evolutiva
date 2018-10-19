
'''
Responsável por avaliar o fitness de um determinado indivíduo
'''
class FitnessEvaluator(object):

    def __init__(self, weights, size):
        self.weights = weights
        self.size = size

    def evaluate(self, individual):
        knapsack_sum = sum([x*y for (x, y) in zip(individual.genotype.dna, self.weights)])
        if knapsack_sum > self.size:
            return -1
        if knapsack_sum == self.size:
            print([y for (x, y) in zip(individual.genotype.dna, self.weights) if x > 0])
        return knapsack_sum
