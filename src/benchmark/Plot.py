import matplotlib
import matplotlib.pyplot as plt
import numpy as np


class Plot:

    def __init__(self, ax):
        self.ax = ax
        self.X = []
        self.Y = []

    def with_title(self, title):
        self.ax.set_title(title)
        return self

    def with_x_label(self, label):
        self.ax.set_xlabel(label)
        return self

    def with_y_label(self, label):
        self.ax.set_ylabel(label)
        return self

    def add_data(self, iteration, pop_fitness):
        if iteration % 5 == 0:
            self.X = self.X + [iteration] * len(pop_fitness)
            self.Y = self.Y + [i.score for i in pop_fitness]

    def draw(self):
        self.ax.scatter(self.X, self.Y, s=10)
