import os
import time
import random


def roll_dice(num_sides):
    return random.randint(1, num_sides)


def roll_health():
    roll_1 = roll_dice(6)
    roll_2 = roll_dice(8)
    result = ((roll_1 * roll_2) + 10) // 2
    return result


def roll_strength():
    roll_1 = roll_dice(6)
    roll_2 = roll_dice(8)
    result = ((roll_1 * roll_2) + 10) // 2
    return result


print("⚔️ Character Generator ⚔️\n")
while True:
    name = input("Name your character: ")
    race = input("Which race is your character?: ")
    print(f"Hail and well met, \033[33m{name} the {race}\033[0m!\n")
    time.sleep(2)
    os.system("clear")
    print("Now lets figure out your stats!")
    while True:
        D6 = roll_health()
        print("Rolling d6 🎲...")
        time.sleep(1)
        print("Rolling d8 🎲...")
        time.sleep(1)
        print("+10 HP...")
        time.sleep(1)
        print("Dividing by two...")
        time.sleep(1)
        print(f"\n{name} has a health stat of:\033[32m {D6} HP\033[0m.\n")
        time.sleep(2)
        os.system("clear")
        break
    while True:
        D8 = roll_strength()
        print("Rolling d6 🎲...")
        time.sleep(1)
        print("Rolling d8 🎲...")
        time.sleep(1)
        print("+12 Strength...")
        time.sleep(1)
        print("Dividing by two...")
        time.sleep(1)
        print(f"\n{name} has a strength stat of: \033[31m{D8}\033[0m.\n")
        time.sleep(2)
        os.system("clear")
        break
    while True:
        print(
            f"Welcome to the party,\033[33m\n{name} the {race}\033[0m.\n \033[32mHEALTH: {D6} \033[0m\n \033[31mSTRENGTH: {D8}\033[0m\n")
        keep = input(
            "would you like to keep this character? (type 'yes' or 'no'): ")
        if keep.lower() == "yes":
            os.system("clear")
            print(
                f"May your name go down in legend, \033[33m{name} the {race}\033[0m!")
            time.sleep(3)
            os.system("clear")
            exit()
        elif keep.lower() == "no":
            os.system("clear")
            print(f"{name} has been put to death... Let's find another adventurer!")
            time.sleep(2)
            os.system("clear")
            break
        else:
            os.system("clear")
            print("Please type 'yes' or 'no'.")
