

class BenchmarkRunner(object):

    def __init__(self, fitness_evaluator, generation_selector, individuals_generator, plotter):
        self.fitness_evaluator = fitness_evaluator
        self.generation_selector = generation_selector
        self.individuals_generator = individuals_generator
        self.plotter = plotter

    def run_benchmark(self):
        individuals = self.individuals_generator.get_individuals(10)

        iteration = 0
        while iteration < 5000 and not self.generation_selector.found:
            iteration += 1
            individuals, pop_fitness = self.generation_selector.next_generation(individuals)
            self.plotter.add_data(iteration, pop_fitness)

        print('Total de iterações ', iteration)
        self.plotter.add_data(iteration, pop_fitness)
