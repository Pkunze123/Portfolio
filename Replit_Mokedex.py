mokedex = {"name": None, "type": None,
           "special attack": None, "HP:": None, "MP": None}

print("MokéBeast")
print("\n")

for name in mokedex:
    mokedex[name] = input(f"What is their {name}?\n").strip().title()

if mokedex["type"] == "Earth":
    print("\033[32m", end="")
elif mokedex["type"] == "Air":
    print("\033[37m", end="")
elif mokedex["type"] == "Fire":
    print("\033[31m", end="")
elif mokedex["type"] == "Water":
    print("\033[34m", end="")
elif mokedex["type"] == "Spirit":
    print("\033[33m", end="")
else:
    print("\033[0m", end="")

for name, value in mokedex.items():
    print(f"{name:<15}: {value}")
