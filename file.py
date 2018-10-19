from src.benchmark.BenchmarkRunner import BenchmarkRunner
from src.util.FileReader import FileReader
from src.util.FitnessEvaluator import FitnessEvaluator
from src.util.ElitistGenerationSelector import ElitistGenerationSelector
from src.util.IndividualsGenerator import IndividualsGenerator
from src.util.InputFileGenerator import InputFileGenerator
from src.util.InputGenerator import InputGenerator


if __name__ == '__main__':
	ig = InputGenerator(20, 750)
	fg = InputFileGenerator("./teste_new", ig)
	fg.generate_file()
	exit(0)
