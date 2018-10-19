import random

'''
Responsável por criar os dados de teste. 
Gera uma lista de pesos e a soma que deve ser encontrada dada esta lista
'''
class InputGenerator(object):

    def __init__(self, size, max_val):
        self.size = size
        self.max_val = max_val

    def generate_input(self):
        random_data = [random.randint(1, self.max_val) for _ in range(self.size)]

        total_items_to_sum = random.randint(10, self.size)
        indexes_to_add = [random.randint(0, self.size-1) for _ in range(total_items_to_sum)]
        indexes_to_add = list(set(indexes_to_add))
        indexes_to_add.sort()

        sum=0
        for index in indexes_to_add:
            sum += random_data[index]
        print(indexes_to_add)
        return random_data, sum
