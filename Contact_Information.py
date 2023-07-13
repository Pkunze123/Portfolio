import os

myUser = {}

print("Let's create your virtual Card\n")
myUser["name"] = input("What is your full name?\n").title()
myUser["age"] = input("How old are you?\n")
myUser["phone"] = input("What is your phone number?\n")
myUser["email"] = input("What is your prefferred email address?\n").title()
myUser["address"] = input("What is your address?\n").title()

os.system("clear")
print(myUser["name"])
print(
    f"Here is your information: \n"
    f"Age: {myUser['age']}\n"
    f"Phone Number: {myUser['phone']}\n"
    f"Email address: {myUser['email']}\n"
    f"Address: {myUser['address']}"
)
