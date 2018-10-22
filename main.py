from src.benchmark.BenchmarkRunner import BenchmarkRunner
from src.benchmark.GraphPlotter import GraphPlotter
from src.util.FileReader import FileReader
from src.util.FitnessEvaluator import FitnessEvaluator
from src.util.ElitistGenerationSelector import ElitistGenerationSelector
from src.util.IndividualsGenerator import IndividualsGenerator
from src.util.InputFileGenerator import InputFileGenerator
from src.util.InputGenerator import InputGenerator
from src.util.RandomGenerationSelector import RandomGenerationSelector
from src.util.TournamentGenerationSelector import TournamentGenerationSelector
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

    fr = FileReader("./teste")
    fr.read()

    fitness_evaluator = FitnessEvaluator(fr.weights, fr.max_size)
    individuals_generator = IndividualsGenerator(len(fr.weights))

    elitist_selector = ElitistGenerationSelector(35, fitness_evaluator)
    random_selector = RandomGenerationSelector(35, fitness_evaluator)
    tournament_selector = TournamentGenerationSelector(35, fitness_evaluator)

    graph_plotter = GraphPlotter(3)

    print('\nRodando Seletor elitista: ')
    p1 = graph_plotter.plots[0]
    p1.with_title('Seletor elitista')\
        .with_x_label('Iteração')\
        .with_y_label('Soma da Mochila')
    b1 = BenchmarkRunner(fitness_evaluator, elitist_selector, individuals_generator, p1)
    b1.run_benchmark()
    p1.draw()

    print('\nRodando Seletor randômico: ')
    p2 = graph_plotter.plots[1]
    p2.with_title('Seletor Randômico') \
        .with_x_label('Iteração') \
        .with_y_label('Soma da Mochila')
    b2 = BenchmarkRunner(fitness_evaluator, random_selector, individuals_generator, p2)
    b2.run_benchmark()
    p2.draw()


    print('\nRodando Seletor por torneio: ')
    p3 = graph_plotter.plots[2]
    p3.with_title('Seletor por torneio') \
        .with_x_label('Iteração') \
        .with_y_label('Soma da Mochila')
    b3 = BenchmarkRunner(fitness_evaluator, tournament_selector, individuals_generator, p3)
    b3.run_benchmark()
    p3.draw()

    graph_plotter.plot()


