import os
import time
import random


def roll_dice(num_sides):
    return random.randint(1, num_sides)


def roll_health():
    result = ((roll_dice(6) * roll_dice(12)) + 10) // 2
    return result


def roll_strength():
    result = ((roll_dice(6) * roll_dice(8)) + 12) // 2
    return result


print("⚔️ Character Generator ⚔️\n")
while True:
    name = input("Name your character: \n")
    race = input("Which race is your character?: \n")
    print(f"Hail and well met, \033[33m{name} the {race}\033[0m!\n")
    time.sleep(2)
    os.system("clear")
    print("Now lets figure out your stats!")
    D6 = roll_health()
    print("Rolling d6 🎲...")
    time.sleep(1)
    print("Rolling d12 🎲...")
    time.sleep(1)
    print("+10 HP...")
    time.sleep(1)
    print("Dividing by two...")
    time.sleep(1)
    print(f"\n{name} has a health stat of:\033[32m {D6} HP\033[0m.\n")
    time.sleep(2)
    os.system("clear")
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
            print(
                f"\033[33m{name}\033[0m has been put to death... Let's find another adventurer!")
            time.sleep(2)
            os.system("clear")
            break
        else:
            os.system("clear")
            print("\033[31mPlease type 'yes' or 'no'\033[0m.")
