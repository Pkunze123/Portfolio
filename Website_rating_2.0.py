import os

print("Website Description\n")

myUser = {
    "name": input("What is your favorite website?\n").title(),
    "url": input("What is its URL?\n"),
    "desc": input("Please leave a short description:\n"),
    "star": int(input("how many stars would you rate this website (1-5)?\n")),
}

os.system("clear")

print(f"Website: {myUser['name']}")
print(
    f"URL: {myUser['url']}\n"
    f"Description: {myUser['desc']}\n"
    f"Rating: {'⭐' * myUser['star']}\n"
)
