print("FAKE Fan Finder!")
print("++++++++++++++++")
print("I am going to ask you a series of questions to prove your fan knowledge and see if you are a real fan!")
fan = input("Are you a fan of 'Spidey and his amazing friends'?\n")
if fan.lower() == "yes":
    print("GREAT! Then...")
    character = input("Which is your favorite character?\n")
    if character.lower() == "spidey":
        print("The title character, of course...")
        name = input("What is his secret identity?\n")
        if name.lower() == "peter parker":
            print("WOW! You really know your stuff!")
        else:
            print("You are NOT a real fan!")
    elif character.lower() == "spin":
        print("Ah, yes! He's pretty awesome...")
        name = input("What is his secret identity?\n")
        if name.lower() == "miles morales":
            print("WOW! You really know your stuff!")
        else:
            print("You are NOT a real fan!")
    elif character.lower() == "ghost spider" or character.lower() == "ghosty":
        print("Ah, yes! She's my favorite too...")
        name = input("What is her secret identity?\n")
        if name.lower() == "gwen stacy":
            print("WOW! You really know your stuff!")
        else:
            print("You are NOT a real fan!")
    elif character.lower() == "hulk":
        print("Ah, yes! He's super strong...")
        name = input("What is his secret identity?\n")
        if name.lower() == "bruce banner":
            print("WOW! You really know your stuff!")
        else:
            print("You are NOT a real fan!")
    elif character.lower() == "miss marvel":
        print("Ah, yes! I like her powers...")
        name = input("What is her secret identity?\n")
        if name.lower() == "kamala khan":
            print("WOW! You really know your stuff!")
        else:
            print("You are NOT a real fan!")
    elif character.lower() == "reptil":
        print("Ah, yes! He is super cool...")
        ability = input("What is his superpower?\n")
        if ability.lower() == "he can turn into dinosaurs":
            print("That's so cool!")
        else:
            print("You are NOT a real fan!")
        name = input("What is his secret identity?\n")
        if name.lower() == "humberto lopez":
            print("WOW! You really know your stuff!")
        else:
            print("You are NOT a real fan!")
    elif character.lower() == "iron man":
        print("Ah, yes! He can fly and shoot lasers...")
        name = input("What is his secret identity?\n")
        if name.lower() == "tony stark":
            print("WOW! You really know your stuff!")
        else:
            print("You are NOT a real fan!")
    elif character.lower() == "wasp and antman":
        print("Ah, yes! They can shrink so teeny tiny...")
        name = input("What are their secret identities?\n")
        if name.lower() == "scott lang and hope van dyne":
            print("WOW! You really know your stuff!")
        else:
            print("You are NOT a real fan!")
    else:
        print("I'm sorry, I don't recognize that character.")
else:
    print("Stop wasting my time!")
