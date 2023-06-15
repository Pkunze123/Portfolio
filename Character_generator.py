import random

print("New Character Stats Generator!\n")

# rolls any size dice:


def roll_dice(num_sides):
    return random.randint(1, num_sides)

# One 6 and one 8 sided:


def roll_and_multiply():
    roll_1 = roll_dice(6)
    roll_2 = roll_dice(8)
    result = roll_1 * roll_2
    return result


while True:
    name = input("Name your Character: ")
    print(f"\n{name} has a health stat of: {roll_and_multiply()} HP\n")
    while True:
        new = input(
            f"Would you like to play with {name} or create a new character? (play/new)\n").lower()
        if new == "play":
            print(f"Hail and well met! Welcome to the party {name}")
            break
        elif new == "new":
            print("Creating a new character...")
            break
        else:
            print("Please type 'play' or 'new'.\n")
    if new == "play":
        break
