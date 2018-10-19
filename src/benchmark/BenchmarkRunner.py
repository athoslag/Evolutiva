

class BenchmarkRunner(object):

    def __init__(self, fitness_evaluator, generation_selector, individuals_generator, plotter):
        self.fitness_evaluator = fitness_evaluator
        self.generation_selector = generation_selector
        self.individuals_generator = individuals_generator
        self.plotter = plotter

    def run_benchmark(self):
        individuals = self.individuals_generator.generate_random_individuals(10)

        iteration = 0
        found = False
        fitness = -1
        while iteration < 200000 and not found:
            if iteration % 100 == 0:
                print('Iteration ' + str(iteration))
            iteration += 1
            individuals, pop_fitness = self.generation_selector.next_generation(individuals)
            fitness = max([i.score for i in pop_fitness])
            if fitness > 0:
                self.plotter.add_data(iteration, fitness)
            found = fitness == self.fitness_evaluator.size

        self.plotter.add_data(iteration, fitness)
        self.plotter.plot()
