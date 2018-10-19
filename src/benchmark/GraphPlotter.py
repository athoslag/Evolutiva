import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class GraphPlotter(object):

    def __init__(self):
        self.X = []
        self.Y = []

    def add_data(self, x, y):
        self.X.append(x)
        self.Y.append(y)

    def plot(self):
        plt.plot(self.X, self.Y)
        plt.show()