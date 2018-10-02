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
    generation_selector = GenerationSelector(fitness_evaluator)
    generator = IndividualsGenerator()

    individuals = generator.generate_random_individuals(10, len(fr.weights))

    iteration = 0
    while True:
        if iteration % 100 == 0:
            print(iteration)
        iteration+=1
        individuals = generation_selector.next_generation(individuals)



    print('pim')