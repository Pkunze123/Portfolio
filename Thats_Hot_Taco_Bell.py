import time
import os


def logo():
    print(""" _______ _           _   _       _    _  ____ _______ _
|__   __| |         | | ( )     | |  | |/ __ \__   __| |
   | |  | |__   __ _| |_|/ ___  | |__| | |  | | | |  | |
   | |  | '_ \ / _` | __| / __| |  __  | |  | | | |  | |
   | |  | | | | (_| | |_  \__ \ | |  | | |__| | | |  |_|
   |_|  |_| |_|\__,_|\__| |___/ |_|  |_|\____/  |_|  (_)

🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮
🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥
🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋🌋
""")


def clear_and_logo():
    os.system("clear")
    logo()


def menu():
    print("📞Press 1 if you're just here for the volcano menu:\n")
    time.sleep(2)
    print("📞Press 2 for advice on 'Sliving' from Paris:\n")
    time.sleep(2)
    print("📞Press 3 if you want Paris to be your life coach:\n")
    time.sleep(2)
    print("📞Press 4 to hear Paris' thoughts on bangs:\n")
    time.sleep(2)
    print("📞Press 5 for Paris to read the volcano menu:\n")
    time.sleep(2)
    print("📞Press 6 for a first listen of Paris' unreleased single, Hot One!:\n")
    time.sleep(2)
    print("📞Press 0 to hear Paris say 'That's HOT!'\n")
    time.sleep(2)
    print("📞All hotline content is prerecorded. Volcano Menu available at participating U.S. Taco Bell Locations for a limited time and while supplies last\n")


os.system("clear")
logo()
time.sleep(2)
print("Presented by Paris Hilton and Taco Bell!")
time.sleep(4)
clear_and_logo()

print("📱You've reached the Taco Bell Volcano Menu HOTline, where you can get spicy advice from me, Paris Hilton, expert on all things HOT!")
time.sleep(5)
print("📞*Hold Please...*")
time.sleep(1)
print("\n🎶 Me, i'm the hot one... 🎶")
time.sleep(1)
print("\n🎶 ...EDM music Playing... 🎶")
time.sleep(4)
clear_and_logo()
while True:
    menu()
    choice = input("> ")
    if choice == "1":
        clear_and_logo()
        print("📞Order the Volcano Menu from Taco Bell!")
        time.sleep(1)
        print("📞It's the Spiciest thing you'll do this summer...")
        time.sleep(1)
        print("📞right Paris?")
        time.sleep(2)
        print("📱That's HOT!")
        time.sleep(5)
        clear_and_logo()
    elif choice == "2":
        clear_and_logo()
        print("📱I've learned that the best way to 'Slive', is having AMAZING friends around you to support you.")
        time.sleep(2)
        print("📱Speaking of, it would be SO HOT if you brought me a volcano burrito right now!")
        time.sleep(5)
        clear_and_logo()
    elif choice == "3":
        clear_and_logo()
        print("📱I've learned that your attitude toward life's kind of everything")
        time.sleep(2)
        print("📱Like basically... if you want a HOT life, you have to get a hot Volcano Taco from Taco Bell...")
        time.sleep(3)
        print("📱That's just math!")
        time.sleep(5)
        clear_and_logo()
    elif choice == "4":
        clear_and_logo()
        print("📱YES, you should ABSOLUTELY get a Volcano Taco!")
        time.sleep(2)
        print("📱oh... you're asking about bangs?!?")
        time.sleep(2)
        print("📱NO... No one looks good with bangs, babe!")
        time.sleep(5)
        clear_and_logo()
    elif choice == "5":
        clear_and_logo()
        print("📱Volcano Burrito?")
        time.sleep(1)
        print("📱That's HOT!")
        time.sleep(2)
        print("📱Volcano Taco?")
        time.sleep(1)
        print("📱THAT's HOT!")
        time.sleep(2)
        print("📱Lava Sauce?")
        time.sleep(1)
        print("📱That's REALLY HOT!")
        time.sleep(5)
        clear_and_logo()
    elif choice == "6":
        clear_and_logo()
        print("\n🎶 Me, I'm the hot one... 🎶")
        time.sleep(1)
        print("\n🎶 ...EDM music Playing... 🎶")
        time.sleep(4)
        print("\n🎶 Me, I'm the hot one... 🎶")
        time.sleep(1)
        print("\n🎶 ...EDM music Playing... 🎶")
        time.sleep(4)
        print("\n🎶 ...more EDM music Playing... 🎶")
        time.sleep(4)
        print("\n🎶 ...even MORE EDM music Playing... 🎶")
        time.sleep(4)
        print("🎶 ahhhh.... 🎶")
        time.sleep(2)
        clear_and_logo()
    elif choice == "0":
        clear_and_logo()
        print("📱  ... That's HOT!")
        time.sleep(3)
        clear_and_logo()
    else:
        clear_and_logo()
        print("📞Sorry, but that choice is totally NOT HOT!")
        time.sleep(1)
        print("📞select another option for spicy advice from Paris Hilton!")
        time.sleep(2)
        clear_and_logo()
