import operator

from src.domain.Individual import Individual


class GenerationSelector(object):

    def __init__(self, evaluator, recombination_rate = 0.25, t_max=100):
        self.evaluator = evaluator
        self.t_max = t_max
        self.r_rate = recombination_rate

    def next_generation(self, individuals):
        pop_fitness = []

        for individual in individuals:
            fitness = self.evaluator.evaluate(individual)
            wrapper = IndividualScoreWrapper(individual, fitness)
            pop_fitness.append(wrapper)

        pop_fitness = sorted(pop_fitness, key=operator.attrgetter('score'), reverse=True)
        pop_fitness = pop_fitness[:2]

        new_pop = []
        for p1 in pop_fitness:
            for p2 in pop_fitness:
                if p1 == p2:
                    continue
                new_1, new_2 = p1.individual.genotype.crossover(p2.individual.genotype)
                new_1.mutate()
                new_2.mutate()
                new_pop.append(Individual(new_1))
                new_pop.append(Individual(new_2))

        return new_pop



class IndividualScoreWrapper(object):

    def __init__(self, individual, score):
        self.individual = individual
        self.score = score


