import os


def print_color(text, color, end='\n', sep=' '):
    color_dict = {
        'BLACK': "\033[0;30m",
        'RED': "\033[0;31m",
        'GREEN': "\033[0;32m",
        'BROWN': "\033[0;33m",
        'BLUE': "\033[0;34m",
        'PURPLE': "\033[0;35m",
        'CYAN': "\033[0;36m",
        'LIGHT_GRAY': "\033[0;37m",
        'DARK_GRAY': "\033[1;30m",
        'LIGHT_RED': "\033[1;31m",
        'LIGHT_GREEN': "\033[1;32m",
        'YELLOW': "\033[1;33m",
        'LIGHT_BLUE': "\033[1;34m",
        'LIGHT_PURPLE': "\033[1;35m",
        'LIGHT_CYAN': "\033[1;36m",
        'LIGHT_WHITE': "\033[1;37m",
        'END': "\033[0m"
    }

    print(f"{color_dict[color]}{text}{color_dict['END']}", end=end, sep=sep)


print("MokéBeast collector:\n")

myUser = {
    "name": input("MokéBeast name: \n").title(),
    "type": input("What is its type? (Earth, Fire, Air, Water, Spirit)\n").strip().capitalize(),
    "sm": input("What is its special move?\n"),
    "hp": int(input("What is its HP?\n")),
    "mp": int(input("What is its MP?\n")),
}

type_to_color = {
    "Earth": "BROWN",
    "Fire": "RED",
    "Air": "LIGHT_GRAY",
    "Water": "BLUE",
    "Spirit": "PURPLE"
}

os.system("clear")

type_color = type_to_color.get(myUser['type'])

print_color(f"Your new MokéBeast: {myUser['name']}", type_color)
print_color(
    f"Type: {myUser['type']}\n"
    f"sm: {myUser['sm']}\n"
    f"hp: {myUser['hp']}\n"
    f"mp: {myUser['mp']}\n",
    type_color
)
