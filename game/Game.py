from .Player import Player

class Game():

    def __init__(self, a, b,
                 times : int = 100,
                 matrix : list = [ [2, -3], [-1, 2] ]):
        if times < 1:
            raise Exception("количество раундов в игре должно быть натуральным числом")
        if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
            raise Exception("введена неправильная матрица игры")

        self.times = times
        self.__playerA = a
        self.__playerB = b
        self.__rounds = list()
        self.__matrix = matrix
        aProb, bProb = list(self.__playerA.getProbability()), list(self.__playerB.getProbability())
        self.__probList = [
            [aProb[0] * bProb[0], aProb[0] * bProb[1]],
            [aProb[1] * bProb[0], aProb[1] * bProb[1]]
        ]

        for i in range(times):
            aChoice = self.__playerA.choose()
            bChoice = self.__playerB.choose()
            self.__score(aChoice, bChoice)
            self.__rounds.append([aChoice, bChoice, self.__matrix[aChoice][bChoice]])

        print()

        self.__defineWinner()
        self.__calculateAverage()
        self.__calculateExpectancy()
        self.__calculateDispersion()
        self.__calculateTheoreticalSqDeviation()
        self.__calculateDeviationsDifference()

    def __score(self, a, b):
        sc = self.__matrix[a][b]
        self.__playerA.score(sc)
        self.__playerB.score(-sc)

    def __defineWinner(self):
        aScore = self.__playerA.getScore()
        bScore = self.__playerB.getScore()
        if aScore > bScore:
            self.__winner, self.__loser = self.__playerA, self.__playerB
        elif aScore < bScore:
            self.__winner, self.__loser = self.__playerB, self.__playerA
        else:
            self.__winner, self.__loser = None, None

    def __calculateAverage(self):
        nOfRounds = len(self.__rounds)
        self.__aAverage = self.__playerA.getScore() / nOfRounds
        self.__bAverage = self.__playerB.getScore() / nOfRounds

    def __calculateExpectancy(self):
        self.__expectancy = 0
        for i in range(2):
            for j in range(2):
                self.__expectancy += self.__matrix[i][j] * self.__probList[i][j]

    # Сделано с опорой на "Вероятность: примеры и задачи" А. Шень
    # Страница 39 "20. Дисперсия"
    def __calculateTheoreticalSqDeviation(self):
        self.__thSqDeviation = self.__dispersion**(1/2)

    def __calculateDeviationsDifference(self):
        self.__deviationDif = 0
        for i in self.__rounds:
            self.__deviationDif += (i[2] - self.__aAverage)**2
        self.__deviationDif = (self.__deviationDif / len(self.__rounds))**(1/2)

    def __calculateDispersion(self):
        self.__dispersion = 0
        exp = self.__expectancy
        for i in range(2):
            for j in range(2):
                self.__dispersion += self.__probList[i][j] * (self.__matrix[i][j] - exp) ** 2

    def displayWinner(self):
            winner = self.getWinner()
            loser = self.getLoser()
            if winner is None:
                print("Ничья\n")
            elif winner is self.__playerA:
                print("Игрок A - победитель со счётом", str(winner.getScore()), "\n"
                      "Игрок B - проигравший со счётом", str(loser.getScore()))
            else:
                print("Игрок B - победитель со счётом", str(winner.getScore()), "\n"
                      "Игрок A - проигравший со счётом", str(loser.getScore()))

    def getRounds(self):
        return [list(self.__rounds[i]) for i in range(len(self.__rounds))]

    def getWinner(self):
        return self.__winner

    def getLoser(self):
        return self.__loser

    def getExpectancy(self):
        return self.__expectancy

    def getTheoreticalSquareDeviation(self):
        return self.__thSqDeviation

    def getDeviationsDifference(self):
        return self.__deviationDif

    def getDispersion(self):
        return self.__dispersion