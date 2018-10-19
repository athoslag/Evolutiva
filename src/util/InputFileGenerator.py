from src.util.InputGenerator import InputGenerator


'''
Responsável por criar um arquivo com os dados para teste.
'''
class InputFileGenerator(object):

    def __init__(self, path: str, input_generator: InputGenerator):
        self.path = path
        self.input_generator = input_generator

    def generate_file(self):

        data, sum = self.input_generator.generate_input()

        with open(self.path, "w+") as file:
            file.write(str(len(data)))
            file.write("\n")
            file.write(" ".join([str(n) for n in data]))
            file.write("\n")
            file.write(str(sum))

