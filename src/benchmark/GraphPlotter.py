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

    def add_data(self, x, y):
        self.X.append(x)
        self.Y.append(y)

    def plot(self):
        plt.plot(self.X, self.Y)
        plt.show()
