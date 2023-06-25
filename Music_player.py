import os
import time
import random


def roll_dice(num_sides):
    return random.randint(1, num_sides)


def roll_stat(dice1, dice2, bonus):
    result = ((roll_dice(dice1) * roll_dice(dice2)) + bonus) // 2
    return result


def create_character():
    print("⚔️ Character Generator ⚔️\n")
    name = input("Name your character: \n")
    race = input("Which race is your character?: \n")
    print(f"Hail and well met, \033[33m{name} the {race}\033[0m!\n")
    time.sleep(2)
    os.system("clear")
    print("Now lets figure out your stats!")
    health = roll_stat(6, 12, 10)
    strength = roll_stat(6, 8, 12)
    for msg in ["Rolling d6 🎲...", "Rolling d12 🎲...", "+10 HP...", "Dividing by two..."]:
        print(msg)
        time.sleep(1)
    print(f"\n{name} has a health stat of:\033[32m {health} HP\033[0m.\n")
    time.sleep(2)
    os.system("clear")
    for msg in ["Rolling d6 🎲...", "Rolling d8 🎲...", "+12 Strength...", "Dividing by two..."]:
        print(msg)
        time.sleep(1)
    print(f"\n{name} has a strength stat of: \033[31m{strength}\033[0m.\n")
    time.sleep(2)
    os.system("clear")
    print(
        f"Welcome to the party,\033[33m\n{name} the {race}\033[0m.\n \033[32mHEALTH: {health} \033[0m\n \033[31mSTRENGTH: {strength}\033[0m\n")
    time.sleep(3)
    os.system("clear")
    return name, race, health, strength


def battle_announcement(character):
    name, race, health, strength = character
    print(
        f"\033[33m{name} the {race}\033[0m\n\033[32mHEALTH: {health}\033[0m\n\033[31mSTRENGTH: {strength}\033[0m\n")


def battle(character1, character2):
    name1, race1, health1, strength1 = character1
    name2, race2, health2, strength2 = character2

    print("⚔️ BATTLE TIME! ⚔️\n")
    print("\nLet the battle begin!!!!\n")
    battle_announcement(character1)
    print("VS.\n")
    battle_announcement(character2)

    time.sleep(4)
    os.system("clear")
    while True:
        os.system("clear")
        print("Rolling Dice...")
        time.sleep(2)
        os.system("clear")
        roll1 = roll_dice(6)
        roll2 = roll_dice(6)

        if roll1 > roll2:
            damage = abs(strength1 - strength2) + 1
            health2 -= damage
            print(f"\033[33m{name1}\033[0m wins the round with a roll of \033[31m{roll1}\033[0m against \033[33m{name2}\033[0m's roll of \033[32m{roll2}\033[0m!")
            time.sleep(2)
            print(
                f"\033[33m{name2}\033[0m loses {damage} health and now has {health2} health left.\n")
            time.sleep(2)

            if health2 <= 0:
                print(
                    f"\033[33m{name2}\033[0m has died. \033[33m{name1}\033[0m is victorious!\n")
                time.sleep(2)
                return True

        elif roll2 > roll1:
            damage = abs(strength1 - strength2) + 1
            health1 -= damage
            print(f"\033[33m{name2}\033[0m wins the round with a roll of \033[32m{roll2}\033[0m against \033[33m{name1}\033[0m's roll of \033[31m{roll1}\033[0m!")
            time.sleep(2)
            print(
                f"\033[33m{name1}\033[0m loses {damage} health and now has {health1} health left.\n")
            time.sleep(2)

            if health1 <= 0:
                print(
                    f"\033[33m{name1}\033[0m has died. \033[33m{name2}\033[0m is victorious!\n")
                time.sleep(2)
                return True


while True:
    character1 = create_character()
    print("Now, lets see who they are battling!")
    time.sleep(2)
    os.system("clear")
    character2 = create_character()
    battle(character1, character2)

    again = input("Would you like to play again? (yes/no): ").lower()
    while again not in ["yes", "no"]:
        print("please type 'yes' or 'no'")
        again = input("Would you like to play again? (yes/no): ").lower()

    if again == "no":
        print("Thanks for playing!")
        break
    elif again == "yes":
        os.system("clear")
