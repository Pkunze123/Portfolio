import random
import os
import time


def roll_dice(side):
    result = random.randint(1, side)
    return result


def health():
    healthstat = ((roll_dice(6) * roll_dice(12)) / 2) + 10
    return healthstat


def strength():
    strengthstat = ((roll_dice(6) * roll_dice(8)) / 2) + 12
    return strengthstat


print("⚔️ Epic Battle Generator ⚔️\n")
c1_name = input("Name your character:\n")
c1_type = input("Character type:\n")
os.system("clear")
print(f"{c1_name} the {c1_type}")
c1_health = health()
c1_strength = strength()
print("HEALTH:", c1_health)
print("strength", c1_strength)


print("\n Who are they battling today? \n")
c2_name = input("Name your character:\n")
c2_type = input("Character type:\n")
os.system("clear")
print(f"{c2_name} the {c2_type}")
c2_health = health()
c2_strength = strength()
print("HEALTH:", c2_health)
print("strength", c2_strength)
print()

round = 1
winner = None

while True:
    time.sleep(1)
    os.system("clear")
    print("⚔️ Epic Battle Generator ⚔️\n")
    print("Let's begin...\n")

    c1dice = roll_dice(6)
    c2dice = roll_dice(6)

    difference = abs(c1_strength - c2_strength) + 1

    if c1dice > c2dice:
        c2_health -= difference
        if round == 1:
            print(c1_name, "wins the first blow!")
        else:
            print(c1_name, "wins round", round)
    elif c2dice > c1dice:
        c1_health -= difference
        if round == 1:
            print(c2_name, "wins the first blow!")
        else:
            print(c2_name, "wins round", round)
    else:
        print("Their swords clash and they draw round", round)

    print()
    print(c1_name)
    print("HEALTH:", c1_health)
    print("Strength", c1_strength)
    print()
    print()
    print(c2_name)
    print("HEALTH:", c2_health)
    print("Strength", c2_strength)
    print()

    if c1_health <= 0:
        print(c1_name, "has died!")
        winner = c1_name
        break
    elif c2_health <= 0:
        print(c2_name, "has died!")
        winner = c2_name
        break
    else:
        print("and they are both standing for the next round!")
        round += 1

time.sleep(1)
os.system("clear")
print("⚔️ Epic Battle Generator ⚔️\n")
print(winner, "has won in round", round, "rounds")
