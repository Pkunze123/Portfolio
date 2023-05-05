print("Generation Generator")
print("Which gereration are you?")
print("+++++++++++++++++++++++++++")
year = int(input("What year were you born?\n"))
if year >= 2015:
    print("you are Gen Alpha")
elif year >= 1995:
    print("You are Gex Z")
elif year >= 1981:
    print("You are a Millenial")
elif year >= 1964:
    print("You are Gex X")
elif year >= 1946:
    print("You are a Boomer")
elif year >= 1925:
    print("You are Traditionalist")
else:
    print("you are either long dead or not yet alive")
