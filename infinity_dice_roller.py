import random
print("Random Sided Die Roller\n")


def roll_dice():
    num_sides = int(input("Enter the number of sides for the dice: \n"))
    return random.randint(1, num_sides)


while True:
    print(f"You rolled a {roll_dice()}.")
    while True:
        play_again = input("Do you want to roll again? (yes/no) ").lower()
        if play_again == "yes":
            break
        elif play_again == "no":
            print("Thanks for playing")
            break
        else:
            print("Please type 'yes' or 'no'.\n")
    if play_again == "no":
        break
