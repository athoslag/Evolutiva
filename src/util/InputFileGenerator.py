

class InputFileGenerator(object):

    def __init__(self, path):
        self.path = path

    def generateFile(self, data, sum):
        with open(self.path, "w+") as file:
            file.write(str(len(data)))
            file.write("\n")
            file.write(" ".join([str(n) for n in data]))
            file.write("\n")
            file.write(str(sum))

