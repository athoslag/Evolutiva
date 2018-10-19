"""
Lê um arquivo de entrada com os dados de teste e mantém as informações a respeito dele.
"""

class FileReader(object):

    def __init__(self, path):
        self.total_items = []
        self.weights = []
        self.max_size = -1
        self.path = path

    def read(self):
        with open(self.path, "r") as file:
            self.total_items = int(file.readline().split("\n")[0])
            self.weights = [int(x) for x in file.readline().split(" ")]
            self.max_size = int(file.readline())
