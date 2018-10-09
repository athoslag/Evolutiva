from src.util.InputFileGenerator import InputFileGenerator


class BenchmarkFilesGenerator:

    def __init__(self, file_generator: InputFileGenerator):
        self.file_generator = file_generator

    def generate_files(self, total):
        for i in range(total):
            self.file_generator.generate_file()

