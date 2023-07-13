import os
import random
import time

bingo = []


def ran():
    number = random.randint(1, 90)
    return number


def prettyPrint():
    for row in bingo:
        print(*row, sep="\t|\t")
    print("\n")


def createCard():
    global bingo
    numbers = []
    for i in range(8):
        num = ran()
        while num in numbers:
            num = ran()
        numbers.append(num)
    numbers.sort()

    bingo = [[numbers[0], numbers[1], numbers[2]],
             [numbers[3], "FR", numbers[4]],
             [numbers[5], numbers[6], numbers[7]]
             ]


createCard()
while True:
    prettyPrint()
    num = int(input("Next Number: "))
    for row in range(3):
        for item in range(3):
            if bingo[row][item] == num:
                bingo[row][item] = "x"

    exes = 0
    for row in bingo:
        for item in row:
            if item == "x":
                exes += 1  # correct incrementation

    if exes == 8:
        print("You win!")
        break

    time.sleep(1)
    os.system("clear")
