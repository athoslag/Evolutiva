import numpy as np


class Genotype(object):

    def __init__(self, dna, m_rate):
        self.dna = dna
        self.m_rate = m_rate

    def mutate(self):
        for i in range(len(self.dna)):
            r = np.random.random()
            if r < self.m_rate:
                self.dna[i] = 1 - self.dna[i]

    def crossover(self, mate):
        ind1 = list(self.dna.copy())
        ind2 = list(mate.dna.copy())

        r = np.random.randint(1, len(ind1) - 1)

        new_ind1 = Genotype(dna=ind1[:r] + ind2[r:], m_rate=self.m_rate)
        new_ind2 = Genotype(dna=ind2[:r] + ind1[r:], m_rate=self.m_rate)

        return new_ind1, new_ind2
