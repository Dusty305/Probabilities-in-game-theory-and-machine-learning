from randbool import RandomBool

class Player():

    def __init__(self, probability : float = 0.5):
        if probability > 1 or probability < 0:
            raise Exception("вероятность лежит в промежутке [0;1]")
        self.__probability = probability
        self.__score = 0

    def choose(self):
        self.__lastChoice = RandomBool(self.__probability).random()
        return self.__lastChoice

    def getProbability(self):
        return [self.__probability, 1 - self.__probability]

    def score(self, sc):
        self.__score += sc

    def getScore(self):
        return self.__score

class ReinfLearningPlayer():

    def __init__(self, zero = 10, one = 10):
        self.__zeroPoints = zero
        self.__onePoints = one
        self.__probability = zero / (zero + one)
        self.__score = 0

    def score(self, sc):
        self.__score += sc
        if sc >= 0:
            if self.__lastChoice == 0:
                self.__zeroPoints += 1
            else:
                self.__onePoints += 1
            self.__recalculateProbability()

    def __recalculateProbability(self):
        self.__probability = self.__zeroPoints / (self.__zeroPoints + self.__onePoints)

    def choose(self):
        self.__lastChoice = RandomBool(self.__probability).random()
        return self.__lastChoice

    def getProbability(self):
        return [self.__probability, 1 - self.__probability]

    def getScore(self):
        return self.__score

class PunishLearningPlayer():

    def __init__(self, zero = 100, one = 100):
        self.__zeroPoints = zero
        self.__onePoints = one
        self.__probability = zero / (zero + one)
        self.__score = 0

    def score(self, sc):
        self.__score += sc
        if sc < 0:
            if self.__lastChoice == 0:
                self.__zeroPoints += sc if (self.__zeroPoints + sc) >= 0 else self.__zeroPoints
            else:
                self.__onePoints += sc if (self.__onePoints + sc) >= 0 else self.__onePoints
            self.__recalculateProbability()

    def __recalculateProbability(self):
        self.__probability = self.__zeroPoints / (self.__zeroPoints + self.__onePoints)

    def choose(self):
        self.__lastChoice = RandomBool(self.__probability).random()
        return self.__lastChoice

    def getProbability(self):
        return [self.__probability, 1 - self.__probability]

    def getScore(self):
        return self.__score
