import os
import time
import random


def roll_dice(num_sides):
    return random.randint(1, num_sides)


def stats(character):
    print(
        f"\033[33m{character['name']} the {character['race']}\033[0m\n\033[32mHEALTH: {character['health']}\033[0m\n\033[31mSTRENGTH: {character['strength']}\033[0m\n"
    )


def roll_stat(dice1, dice2, bonus):
    result = ((roll_dice(dice1) * roll_dice(dice2)) // 2) + bonus
    return result


def create_character():
    print("⚔️ Epic Battle Generator ⚔️\n")
    name = input("Name your character: \n")
    race = input("Which race is your character?: \n")
    print(f"Hail and well met, \033[33m{name} the {race}\033[0m!\n")
    time.sleep(2)
    os.system("clear")
    print("Now lets figure out your stats!")
    health = roll_stat(6, 12, 10)
    strength = roll_stat(6, 8, 12)
    for msg in [
        "Rolling d6 🎲...", "Rolling d12 🎲...", "dividing by 2...", "+10 HP..."
    ]:
        print(msg)
        time.sleep(1)
    print(f"\n{name} has a health stat of:\033[32m {health} HP\033[0m.\n")
    time.sleep(2)
    os.system("clear")
    for msg in [
        "Rolling d6 🎲...", "Rolling d8 🎲...", "Dividing by 2...",
        "+12 Strength..."
    ]:
        print(msg)
        time.sleep(1)
    print(f"\n{name} has a strength stat of: \033[31m{strength}\033[0m.\n")
    time.sleep(2)
    os.system("clear")
    print(
        f"Welcome to the party,\033[33m\n{name} the {race}\033[0m.\n \033[32mHEALTH: {health} \033[0m\n \033[31mSTRENGTH: {strength}\033[0m\n"
    )
    time.sleep(3)
    os.system("clear")
    return {'name': name, 'race': race, 'health': health, 'strength': strength}


def battle_announcement(character):
    print(
        f"\033[33m{character['name']} the {character['race']}\033[0m\n\033[32mHEALTH: {character['health']}\033[0m\n\033[31mSTRENGTH: {character['strength']}\033[0m\n"
    )


def battle(character1, character2):
    round = 1

    print("⚔️ BATTLE TIME! ⚔️\n")
    print("\nLet the battle begin!!!!\n")
    battle_announcement(character1)
    print("VS.\n")
    battle_announcement(character2)

    time.sleep(4)
    os.system("clear")
    while True:
        os.system("clear")
        stats(character1)
        stats(character2)
        print("Rolling Dice...")
        time.sleep(2)
        roll1 = roll_dice(6)
        roll2 = roll_dice(6)

        if roll1 > roll2:
            damage = abs(character1['strength'] - character2['strength']) + 1
            character2['health'] -= damage
            print(
                f"\033[33m{character1['name']}\033[0m wins round {round} with a roll of \033[31m{roll1}\033[0m against \033[33m{character2['name']}\033[0m's roll of \033[32m{roll2}\033[0m!"
            )
            time.sleep(2)
            print(
                f"\033[33m{character2['name']}\033[0m loses {damage} health and now has {character2['health']} health left.\n"
            )
            round += 1
            time.sleep(2)
            os.system("clear")

            if character2['health'] <= 0:
                print(
                    f"\033[33m{character2['name']}\033[0m has died. \033[33m{character1['name']}\033[0m is victorious!\n"
                )
                time.sleep(2)
                print(
                    f"\033[33m{character1['name']}\033[0m won the battle in \033[32m{round}\033[0m rounds!")
                time.sleep(4)
                os.system("clear")
                return True

        elif roll2 > roll1:
            damage = abs(character1['strength'] - character2['strength']) + 1
            character1['health'] -= damage
            print(
                f"\033[33m{character2['name']}\033[0m wins round {round} with a roll of \033[32m{roll2}\033[0m against \033[33m{character1['name']}\033[0m's roll of \033[31m{roll1}\033[0m!"
            )
            time.sleep(2)
            print(
                f"\033[33m{character1['name']}\033[0m loses {damage} health and now has {character1['health']} health left.\n"
            )
            round += 1
            time.sleep(2)
            os.system("clear")

            if character1['health'] <= 0:
                print(
                    f"\033[33m{character1['name']}\033[0m has died. \033[33m{character2['name']}\033[0m is victorious!\n"
                )
                time.sleep(2)
                print(
                    f"\033[33m{character2['name']}\033[0m won the battle in \033[32m{round}\033[0m rounds!")
                time.sleep(4)
                os.system("clear")
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
        os.system("clear")
        print("Thanks for playing!")
        time.sleep(3)
        exit()
    elif again == "yes":
        os.system("clear")
