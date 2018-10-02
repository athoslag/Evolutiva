import random


class InputGenerator(object):

    def __init__(self, size, max_val):
        self.size = size
        self.max_val = max_val

    def generateInput(self):
        random_data = [random.randint(1, self.max_val) for _ in range(self.size)]

        array_index = random.randint(1, self.size - 1)
        iterations = array_index
        sum = 0
        while iterations < self.size:
            print("round")
            sum += random_data[iterations]
            array_index = random.randint(1, ((self.size - iterations)%15)+1)
            iterations += array_index
        return random_data, sum
