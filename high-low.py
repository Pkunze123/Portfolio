import random

print("One Million to One: The Number guessing game!!!")
answer = random.randint(1, 1000000)
tries = 0

while True:
    try:
        guess = int(input("What is your guess?\n"))
        tries += 1
        if guess > answer:
            print("Too high...")
        elif guess < answer:
            print("Too low...")
        elif guess == answer:
            print("You Guessed It!!!")
            print(f"You Got it in {tries} tries! Great job!")
            break
        else:
            print("Try Again")
    except ValueError:
        print("Please enter a valid number")
