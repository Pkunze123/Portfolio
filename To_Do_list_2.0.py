# | name | date | priority
import os
import time
todo = []


def add():
    time.sleep(1)
    os.system("clear")
    name = input("Name > ")
    date = input("Date > ")
    priority = input("Priority > ").capitalize()
    row = [name, date, priority]
    todo.append(row)
    print("Added!")


def view():
    time.sleep(1)
    os.system("clear")
    options = input("1: all\n2: By Priority\n>")
    if options == "1":
        for row in todo:
            for item in row:
                print(item, end=" | ")
            print("\n")
        print("\n")
    else:
        priority = input("What Priority? ").capitalize()
        for row in todo:
            if priority in row:
                for item in row:
                    print(item, end=" | ")
                print("\n")
            print("\n")
        time.sleep(4)
        os.system("clear")


def edit():
    time.sleep(1)
    os.system("clear")
    find = input("What would you like to edit? > ")
    found = False
    for row in todo:
        if find in row:
            found = True
    if not found:
        print("couldn't find that...")
        return
    for row in todo:
        if find in row:
            todo.remove(row)
    name = input("Name > ")
    date = input("Date > ")
    priority = input("Priority > ").capitalize()
    row = [name, date, priority]
    todo.append(row)
    print("Edited!")


def remove():
    time.sleep(1)
    os.system("clear")
    find = input("What would you like to remove? > ")
    for row in todo:
        if find in row:
            todo.remove(row)


while True:
    menu = input("1: Add\n2: View\n3: Edit\n4: Remove\n")
    if menu == "1":
        add()
    elif menu == "2":
        view()
    elif menu == "3":
        edit()
    else:
        remove()

time.sleep(1)
os.system("clear")
