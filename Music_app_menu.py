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


title = f"{colorChange('=', 'RED')}{colorChange('=', 'WHITE')}{colorChange('=', 'BLUE')}{colorChange(' Music App ', 'YELLOW')}{colorChange('=', 'BLUE')}{colorChange('=', 'WHITE')}{colorChange('=', 'RED')}"
# This section will center the title in the console no matter the size.
# Determine the width of the console
console_width = os.get_terminal_size().columns

# Compose the title and calculate the length without color codes
base_title = "= = = Music App = = ="
color_title = f"{colorChange('=', 'RED')}{colorChange('=', 'WHITE')}{colorChange('=', 'BLUE')}{colorChange(' Music App ', 'YELLOW')}{colorChange('=', 'BLUE')}{colorChange('=', 'WHITE')}{colorChange('=', 'RED')}"

# Calculate the padding needed to center the title
padding = (console_width - len(base_title)) // 2

# Print the title with padding
print(' ' * padding + color_title)

print("\n")
print(f"🔥▶️\t{colorChange('Radio Gaga', 'WHITE')}")
print(f"\t{colorChange('Queen', 'YELLOW')}")
print("\n")
print(f"{colorChange('Prev', 'WHITE'):<35}")
print(f"{colorChange('Next', 'GREEN'):^35}")
print(f"{colorChange('Pause', 'PURPLE'):>35}")
