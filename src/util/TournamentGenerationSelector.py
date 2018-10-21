import operator
import random

from src.domain.Individual import Individual
from src.util.AbstractGeneration import AbstractGeneration

'''
Seletor #2 - Método de seleção por torneio
A seleção por torneio sorteia aleatoriamente dois indivíduos e seleciona 
para participar da próxima geração aquele com melhor avaliação. Os melhores 

'''
class TournamentGenerationSelector(AbstractGeneration):

    def __init__(self, popsize, evaluator, recombination_rate=0.25, t_max=100):
        super().__init__(popsize, evaluator, recombination_rate, t_max)

    def next_generation(self, individuals):

        pop_fitness = self.evaluate_generation(individuals)
        
        # creates a randomized copy of the population
        current_fitness = pop_fitness
        random.shuffle(current_fitness)

        # configures the parameters of the tournaments
        tournament_count = int(pow(self.popsize, 0.5))
        tournament_participants = 2
        tournament_fitness = []

        for tournament in range(tournament_count):
            participants = []
            # selects each of the participants of the tournament
            for p in range(tournament_participants):
                participants.append(current_fitness.pop())
                random.shuffle(current_fitness)

            # selects the best participant of the tournament
            selected = sorted(participants, key=operator.attrgetter('score'), reverse=True)[0]
            tournament_fitness.append(selected)

        pop_fitness = tournament_fitness

        # crossover
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

        return new_pop, pop_fitness