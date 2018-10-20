from src.benchmark.BenchmarkRunner import BenchmarkRunner
from src.benchmark.GraphPlotter import GraphPlotter
from src.util.FileReader import FileReader
from src.util.FitnessEvaluator import FitnessEvaluator
from src.util.ElitistGenerationSelector import ElitistGenerationSelector
from src.util.IndividualsGenerator import IndividualsGenerator
from src.util.InputFileGenerator import InputFileGenerator
from src.util.InputGenerator import InputGenerator
from src.util.RandomGenerationSelector import RandomGenerationSelector

if __name__ == '__main__':

    fr = FileReader("./teste")
    fr.read()

    fitness_evaluator = FitnessEvaluator(fr.weights, fr.max_size)
    individuals_generator = IndividualsGenerator(len(fr.weights))

    elitist_selector = ElitistGenerationSelector(35, fitness_evaluator)
    random_selector = RandomGenerationSelector(35, fitness_evaluator)

    b1 = BenchmarkRunner(fitness_evaluator, elitist_selector, individuals_generator, GraphPlotter())
    b1.run_benchmark()

    # b2 = BenchmarkRunner(fitness_evaluator, random_selector, individuals_generator, GraphPlotter())
    # b2.run_benchmark()



