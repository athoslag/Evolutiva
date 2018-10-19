from src.benchmark.BenchmarkRunner import BenchmarkRunner
from src.benchmark.GraphPlotter import GraphPlotter
from src.util.FileReader import FileReader
from src.util.FitnessEvaluator import FitnessEvaluator
from src.util.ElitistGenerationSelector import ElitistGenerationSelector
from src.util.IndividualsGenerator import IndividualsGenerator
from src.util.InputFileGenerator import InputFileGenerator
from src.util.InputGenerator import InputGenerator

if __name__ == '__main__':

    fr = FileReader("./teste")
    fr.read()

    fitness_evaluator = FitnessEvaluator(fr.weights, fr.max_size)
    generation_selector = ElitistGenerationSelector(35, fitness_evaluator)
    generator = IndividualsGenerator(len(fr.weights))

    plotter = GraphPlotter()
    benchmark = BenchmarkRunner(fitness_evaluator, generation_selector, generator, plotter)
    benchmark.run_benchmark()
