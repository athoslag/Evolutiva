import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from src.benchmark.Plot import Plot


class GraphPlotter(object):

    def __init__(self, total):
        self.plots = []
        fig, plots = plt.subplots(total, sharey=True)
        for plot in plots:
            self.plots.append(Plot(plot))
        plt.tight_layout()

    def add_data(self, id, iteration, pop_fitness):
        plot = self.plots[id]
        plot.add_data(iteration, pop_fitness)

    def plot(self):
        plt.show()
