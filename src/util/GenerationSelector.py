import operator

from src.domain.Individual import Individual
from src.util.AbstractGeneration import AbstractGeneration


class GenerationSelector(AbstractGeneration):

    def __init__(self, popsize, evaluator, recombination_rate=0.25, t_max=100):
        super().__init__(popsize, evaluator, recombination_rate, t_max)


    def next_generation(self, individuals):

        pop_fitness = self.evaluate_generation(individuals)

        array_cut = int(pow(self.popsize, 0.5))
        remaining = self.popsize - pow(array_cut, 2)
        pop_fitness = sorted(pop_fitness, key=operator.attrgetter('score'), reverse=True)
        pop_fitness = pop_fitness[:array_cut]

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




