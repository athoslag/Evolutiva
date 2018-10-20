import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class GraphPlotter(object):

    def __init__(self):
        self.X = []
        self.Y = []
        self.title = ''
        self.x_label = ''
        self.y_label = ''

    def with_title(self, title):
        plt.title(title)
        return self

    def with_x_label(self, label):
        plt.xlabel(label)
        return self

    def with_y_label(self, label):
        plt.ylabel(label)
        return self

    def add_data(self, iteration, pop_fitness):
        if iteration % 200 == 0:
            self.X = self.X + [iteration]*len(pop_fitness)
            self.Y = self.Y + [i.score for i in pop_fitness]

    def plot(self):
        plt.ylim(bottom=0, top=max(self.Y))
        plt.scatter(self.X, self.Y)
        plt.show()
