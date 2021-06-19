#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from randbool import RandomBool
import game
from datetime import datetime
import codecs

def checkProbability(prob, times):
    rand = RandomBool(prob)
    false = 0
    true = 0
    for i in range(times):
        if rand.random():
            true += 1
        else:
            false += 1

    print("Из ", times, " попыток мы получили что:", sep='')
    print("1 попалась ", true, " раз", sep='')
    print("0 попался ", false, " раз", sep='')
    print("Разница между количеством 1 и 0: ", abs(true - false), sep='')

def playGame(PlayerA, PlayerB, times : int = 100):
    try:
        gameInstance = game.Game(PlayerA, PlayerB, times)

        return PlayerA, PlayerB, gameInstance
    except Exception as exc:
        print("ОШИБКА!", repr(exc))

def analyseGame(PlayerA, PlayerB, gameInstance):

    gameInstance.displayWinner()
    print("Средне значение выигрыша/проигрыша:")
    print("A:", PlayerA.getScore() / gameInstance.times)
    print("B:", PlayerB.getScore() / gameInstance.times, "\n")

    print("Математическое ожидание: ", gameInstance.getExpectancy(), "\n"
          "Среднее квадратичное отклонение от экспериментального среднего: ",
          gameInstance.getDeviationsDifference(), "\n"
          "Теоретическое среднее квадратичное отклонение для данных вероятностей (дисперсия):",
          gameInstance.getTheoreticalSquareDeviation(), "\n")

    time = datetime.now().strftime("%d.%m.%Y %H.%M.%S")
    with codecs.open("DATA " + time + ".csv", "w", "utf-8") as file:
        file.write(u"Среднее значение выигрыша/проигрыша:\n" +
                   u"A," + str(PlayerA.getScore() / gameInstance.times) + "\n" +
                   u"B," + str(PlayerB.getScore() / gameInstance.times) + "\n" +
                   u"Математическое ожидание," + str(gameInstance.getExpectancy()) + "\n" +
                   u"Среднее квадратичное отклонение от экспериментального среднего," +
                   str(gameInstance.getDeviationsDifference()) + "\n" +
                   u"Теоретическое среднее квадратичное отклонение для данных вероятностей," +
                   str(gameInstance.getTheoreticalSquareDeviation()) + "\n")

        listOfRounds = gameInstance.getRounds()
        file.write(u"Игрок А,Игрок В,Счёт\n")
        for i in listOfRounds:
            first, second, score = i[0], i[1], i[2]
            file.write(f"{int(first)},{int(second)},{score}\n")

        file.close()

def menu():
    print("МЕНЮ\n")
    print("1. Датчик случайных чисел")
    print("2. Первая стратегия: оба игрока равновероятно [вероятность 0.5] выбирают одну или другую строку/столбец")
    print("3. Вторая стратегия: A равновероятно выбирает строку, "
          "а игрок B (случайно) выбирает первый столбец втрое реже, чем второй.")
    print("4. Рассмотреть разные методы обучения игрока A при условии, что "
          "игрок B придерживается стратегии, описанной в предыдущем пункте")
    print("5. Рассмотреть обучение обоих игроков с подкреплением")
    print("6. Закончить работу программы.")
    print("\n Введите свой вариант: ", end='')

def call(option):
    try:
        if option < 1 or option > 6:
            raise Exception("было введено неправильное число")
        elif option == 1:
            print("Введите через строку вероятность выпадания 0 и"
                  "и количество раз для проверки")
            prob = float(input())
            times = int(input())
            print()
            checkProbability(prob, int(times))
        elif option == 2:
            firstPlayer, secondPlayer, playedGame = playGame(game.Player(), game.Player())
            analyseGame(firstPlayer, secondPlayer, playedGame)
        elif option == 3:
            firstPlayer, secondPlayer, playedGame = playGame(game.Player(), game.Player(float(1/4)))
            analyseGame(firstPlayer, secondPlayer, playedGame)
        elif option == 4:
            print("Первый метод: обучение с подкреплением.\n")
            firstPlayer, secondPlayer, playedGame = playGame(game.ReinfLearningPlayer(), game.Player(float(1/4)))
            firstPlayer, secondPlayer, playedGame = playGame\
                (game.Player(firstPlayer.getProbability()[0]), game.Player(float(1/4)))
            analyseGame(firstPlayer, secondPlayer, playedGame)
            input("Press Enter to continue...")
            print("Второй метод: обучение с наказанием.\n")
            firstPlayer, secondPlayer, playedGame = playGame(game.PunishLearningPlayer(), game.Player(float(1/4)))
            firstPlayer, secondPlayer, playedGame = playGame\
                (game.Player(firstPlayer.getProbability()[0]), game.Player(float(1/4)))
            analyseGame(firstPlayer, secondPlayer, playedGame)
        elif option == 5:
            firstPlayer, secondPlayer, playedGame = playGame(game.ReinfLearningPlayer(), game.ReinfLearningPlayer())
            firstPlayer, secondPlayer, playedGame = playGame\
                (game.Player(firstPlayer.getProbability()[0]),\
                 game.Player(secondPlayer.getProbability()[0]))
            analyseGame(firstPlayer, secondPlayer, playedGame)
    except Exception as exc:
        print("ОШИБКА!", repr(exc))

if __name__ == '__main__':
    option = 0
    print("Лекционное задание \"Вероятность в теории игр и машинное обучение\"\n")
    while option != 6:
        print()
        menu()
        option = int(input())
        call(option)
        input("Press Enter to continue...")




