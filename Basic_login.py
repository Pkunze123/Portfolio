from getpass import getpass


def login():
    correct_username = "Yoshi"
    correct_password = "Doggo1"

    print("Dog System Login\n")

    while True:
        username = input("Enter username: ")
        password = getpass("Enter password: ")

        if username == correct_username and password == correct_password:
            print("Login successful!")
            break
        else:
            print("Invalid username or password. Please try again.")


login()
