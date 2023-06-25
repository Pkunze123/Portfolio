import time
import os


def add_name(namesList):
    first_name = input("Please enter your first name: ").strip().capitalize()
    last_name = input("Please enter your last name: ").strip().capitalize()
    full_name = first_name + " " + last_name
    if full_name not in namesList:
        print(f"Welcome, {first_name} {last_name}!")
        time.sleep(2)
        namesList.append(full_name)
    else:
        print("That doggo has already been added!")
        time.sleep(2)
    return namesList


namesList = []

while True:
    print("NEW Doggo Friends!!!\n")
    if namesList:  # check if namesList is not empty
        print(", ".join(namesList))
        print("\n")
        print("\n")
    print("Please add your new friends!\n")
    namesList = add_name(namesList)
    os.system("clear")
    continue
