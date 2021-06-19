**&quot;Вероятность в теории игр и машинное обучение&quot;**

_Краткое описание игры:_ ![](RackMultipart20210619-4-1m8wufn_html_9da21f962c2bc4eb.png)

Игроки A и B играют в следующую игру: они одновременно выбирают строку и столбец таблицы выигрышей соответственно.

Указанное в таблице число является размером выигрыша/проигрыша игрока A и соответственно размером проигрыша/выигрыша игрока B.

Игроки проводят 100 игр.

[Полная постановка задачи](https://docs.google.com/document/d/12KgcBxp2nowimJlgqwT1E5rCzpHe2dnwELoGraQKqOI/edit)

_Описание исследования_

Для выполнения была написана программа на языке программирования Python 3.8. В программе было построено 2 модуля:

1. randbool содержит одноимённый класс, который способен генерировать 0 или 1. Модуль был сделан при помощи модуля random, имеющий псевдо-случайный генератор чисел.
2. game содержит 4 класса
  1. Game - класс игры. При инициализации объекта проходит вышеописанная игра, где игроки используют собственный стратегии выбора строки/столбца
  2. Player - класс игрока. Игрок содержит в себе вероятность выбора строки/столбца и способен случайно его выбирать, в зависимости изначально установленной вероятности (планировалось сделать его базовым классом, но я не обладаю достаточными знаниями наследования в языке python)
  3. ReinfLearningPlayer - класс игрока, обладающий такими же методами и полями, как и Player, однако в функции score игрок меняет свою стратегию в пользу столбца/строки, благодаря которому он заработал положительный счёт.
  4. PunishLearningPlayer - аналогичен прошлому классу, однако он в функции score игрок меняет свою стратегию против столбца/строки, из-за которого он заработал отрицательный счёт.

[Код программы](https://github.com/Dusty305/Probabilities-in-game-theory-and-machine-learning)

Меню программы:

![](RackMultipart20210619-4-1m8wufn_html_9adbc569f5957c54.png)

1. Генератор случайных чисел описан в модуле RandomBool.py, в котором построен класс, сделанный с помощью модуля random языка Python

![](RackMultipart20210619-4-1m8wufn_html_d015cd2043bf0aae.png)

1. [Первая стратегия](https://docs.google.com/spreadsheets/d/1XtfBDYEhrvmQmBtkh7tIcPcBEiNNcj30LN-OfiznrFo/edit?usp=sharing)

![](RackMultipart20210619-4-1m8wufn_html_687d78edeaabb733.png)

1. [Вторая стратегия](https://docs.google.com/spreadsheets/d/1xQtPBVv9rMxM2cpiIe2Iya52Xw8Qx5LHrQ-SULccYE4/edit?usp=sharing)

![](RackMultipart20210619-4-1m8wufn_html_107dcdfbb7eb7ed2.png)

1. Третья стратегия

[Обучение с подкреплением](https://docs.google.com/spreadsheets/d/1LzSFuquX5xPqqSf9c_YKtZxh6ovOZwNOrgcVxsF_t0k/edit?usp=sharing)

[Обучение с наказанием](https://docs.google.com/spreadsheets/d/11B3Jkjf_7M58zOE8BjnxIK8OXo_h6b43rtrzTiuQAYM/edit?usp=sharing)

![](RackMultipart20210619-4-1m8wufn_html_eb3ad83d76e173b5.png)

![](RackMultipart20210619-4-1m8wufn_html_180beb55fdfce4a8.png)

1. [Четвертая стратегия](https://docs.google.com/spreadsheets/d/1QKPXZ1Th5-uWPKB0o6qRa7CnpsLi9oeYOtuLCtqYY5g/edit?usp=sharing)

![](RackMultipart20210619-4-1m8wufn_html_e9dda4255d4eeb4c.png)

_Вывод_

Очевидно, что первая стратегия - наименее предпочтительная из всех остальных, т.к. математическое ожидиние при ней равно 0 и неизвестно, кто из игроков будет в выигрыше.

Вторая стратегия более оптимальная для игрока B, т.к. он с меньшим шансом будет проигрывать 3 очка и останется в плюсе. Такие вывод можно сделать из того, что мат. ожидание для первого игрока равно -0.25, т.е. он, скорее всего, будет проигрывать.

В третьей стратегии, при том что игрок В придерживается более оптимальной для себя стратегии, выигравает игрок А, т.к. он обучается и благодаря этому вырабатывает собственную стратегию, которая основывается на выборах игрока В.

В четвертой стратегии мат. ожидание близится к 0, что говорит о том, что когда оба игрока обучаются исходя и решений друг друга, результат игры будет непредсказуем, как и в первой стратегии.

В общем, игру можно назвать честной только в том случае, когда стратегии игроков в целом сходятся, как в первой и четвёртой стратегии, т.к. при них нельзя предугадать заранее, кто выиграет.