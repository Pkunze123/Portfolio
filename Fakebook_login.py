import os


def colorChange(text, color):
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
        'WHITE': "\033[0m",
        'END': "\033[0m"
    }
    return f"{color_dict[color]}{text}{color_dict['END']}"


# Determine the width of the console
console_width = os.get_terminal_size().columns

# Compose the titles
title1 = "Welcome To"
title2 = "- -      FakeBook     - -"
footer = "Definitely NOT a ripoff of a certain other social networking site...  it's NOT Facebook..."

# Calculate the padding needed to center the titles
padding1 = (console_width - len(title1)) // 2
padding2 = (console_width - len(title2)) // 2

# Print the titles with padding
print(' ' * padding1 + colorChange(title1, 'WHITE'))
print(' ' * padding2 + colorChange(title2, 'BLUE'))

print("\n")
print(footer.rjust(console_width))
text = "Honest"
print(f"{colorChange('Honest!', 'RED'):^35}")

print("\n")
print("\n")
username = input(f"{colorChange('Username: ', 'YELLOW'):^50}")
password = input(f"{colorChange('Password: ', 'YELLOW'):^50}")
