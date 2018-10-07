from src.benchmark.BenchmarkRunner import BenchmarkRunner
from src.util.FileReader import FileReader
from src.util.FitnessEvaluator import FitnessEvaluator
from src.util.GenerationSelector import GenerationSelector
from src.util.IndividualsGenerator import IndividualsGenerator
from src.util.InputFileGenerator import InputFileGenerator
from src.util.InputGenerator import InputGenerator

if __name__ == '__main__':

    # gera arquivão
    # ig = InputGenerator(20, 750)
    #
    # fg = InputFileGenerator("./teste")
    #
    # data, sum = ig.generateInput()
    # fg.generateFile(data, sum)
    # exit(0)

    fr = FileReader("./teste")
    fr.read()

    fitness_evaluator = FitnessEvaluator(fr.weights, fr.max_size)
    generation_selector = GenerationSelector(10, fitness_evaluator)
    generator = IndividualsGenerator(len(fr.weights))

    benchmark = BenchmarkRunner(fitness_evaluator, generation_selector, generator)
    benchmark.run_benchmark()
