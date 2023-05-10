animals = {
    "dog": "bark",
    "cat": "meow",
    "cow": "moo",
    "horse": "neigh",
    "fish": "Blub!",
    "seal": "ow, ow, ow",
    "fox": "Ringa Ding Ding"
}

while True:
    animal = input("What animal do you want to hear? ")
    if animal.lower() in animals:
        sound = animals[animal.lower()]
        print("The", animal.lower(), "says", sound + "!")
        exit_choice = input("Do you want to exit? (yes/no) ")
        if exit_choice.lower() == "yes":
            break
    else:
        print("Sorry, we don't have the sound for that animal.")
