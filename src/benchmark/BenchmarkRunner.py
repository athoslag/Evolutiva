

class BenchmarkRunner(object):

    def __init__(self, fitness_evaluator, generation_selector, individuals_generator):
        self.fitness_evaluator = fitness_evaluator
        self.generation_selector = generation_selector
        self.individuals_generator = individuals_generator

    def run_benchmark(self):
        individuals = self.individuals_generator.generate_random_individuals(10)

        iteration = 0
        while True:
            if iteration % 100 == 0:
                print('pim ' + str(iteration))
            iteration += 1
            individuals = self.generation_selector.next_generation(individuals)
