import random
import os
import time


hangman_stages = [
    '''
     ----
     |  |
        |
        |
        |
    ____|_
    ''',
    '''
     ----
     |  |
     O  |
        |
        |
    ____|_
    ''',
    '''
     ----
     |  |
     O  |
     |  |
        |
    ____|_
    ''',
    '''
     ----
     |  |
     O  |
    /|  |
        |
    ____|_
    ''',
    '''
     ----
     |  |
     O  |
    /|\ |
        |
    ____|_
    ''',
    '''
     ----
     |  |
     O  |
    /|\ |
    /   |
    ____|_
    ''',
    '''
     ----
     |  |
     O  |
    /|\ |
    / \ |
    ____|_
    '''
]

listOfWords = ["british", "suave", "integrity", "accent",
               "evil", "genius", "downton", "bollocks", "crisps", "bobbie"]

while True:  # Game replay loop
    letterPicker = []
    lives = 6
    word = random.choice(listOfWords)
    os.system("clear")
    print("Hangman Game\n")
    print(hangman_stages[6 - lives])  # Print hangman stage
    time.sleep(2)
    print("Try to guess the word by trying one letter at a time. You win if you guess it in less than 6 tries!\n")
    time.sleep(4)
    os.system("clear")

    feedback_message = ""  # initialize feedback message

    while True:  # Word guessing loop
        letter = input("\nType in a letter: ").lower()
        if letter in letterPicker:
            feedback_message = "Already tried that one..."
            continue
        letterPicker.append(letter)

        if letter in word:
            feedback_message = "You found a letter! Please try again..."
        else:
            feedback_message = "Nope!"
            lives -= 1

        allLetter = True
        os.system("clear")
        print(hangman_stages[6 - lives])  # Print hangman stage
        print(feedback_message)  # print feedback message

        for i in word:
            if i in letterPicker:
                print(i, end="")
            else:
                print("_", end="")
                allLetter = False
        print("\n")

        if allLetter:
            print(f"You've won with {lives} left!")
            time.sleep(4)
            os.system("clear")
            break

        if lives <= 0:
            print("You ran out of lives!")
            print(f"\n The answer was {word}")
            time.sleep(4)
            os.system("clear")
            break

        else:
            print(f"you have {lives} lives left...")

    while True:  # Loop to handle invalid input
        answer = input("Would you like to play again? (yes or no): \n").lower()
        if answer == "no":
            os.system("clear")
            print("Thanks for playing! Goodbye")
            time.sleep(4)
            os.system("clear")
            exit()
        elif answer == "yes":
            break
        else:
            print("Please type yes or no.")
