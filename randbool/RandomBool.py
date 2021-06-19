import random

class RandomBool():

    def __init__(self, false : float = 0.5):
        if false > 1 or false < 0:
            raise Exception("probability must be within [0;1]")
        random.seed()
        self._falseProbability = false
        self._trueProbability = 1 - false

    def random(self):
        return False if random.uniform(0, 1) < self._falseProbability else True
