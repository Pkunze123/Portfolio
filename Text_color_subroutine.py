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


print("Super Subroutine!\n")
print("With my", end=" ")
print_color("new program", 'PURPLE', end=" ")
print("I can just call the Subroutine")
print_color("and", 'RED', end=" ")
print("that word appears in the chosen color!\n")
print("with no", end=" ")
print_color("Weird Gaps", 'CYAN')
print("\nPretty cool!")
