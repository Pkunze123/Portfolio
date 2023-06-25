import os
import time

todo_list = []


def printList():
    print("\n")
    for i, item in enumerate(todo_list, 1):
        print(f"{i}. {item}")
    print("\n")


title = "My To-Do List."

while True:
    print(f"{title}")
    print("\n")
    menu = input(
        "What would you like to do? \nYou may ADD, EDIT, or REMOVE items or you may VIEW the list. You can also DELETE the list.: \n").lower()
    print("\n")
    if menu == "add":
        os.system("clear")
        item = input("What would you like to add?:\n").title()
        if item not in todo_list:
            todo_list.append(item)
            print("List item added!.")
        else:
            print(f"{item} is already in the list.")
        time.sleep(2)
        os.system("clear")

    elif menu == "edit":
        os.system("clear")
        while True:
            item = input("What would you like to edit?:\n").title()
            new = input("What would you like to change it to?:\n").title()
            found = False
            for i in range(len(todo_list)):
                if todo_list[i] == item:
                    todo_list[i] = new
                    found = True
                    print("List item edited!.")
                    time.sleep(2)
                    os.system("clear")
                    break
            if not found:
                print("This item is not in the list.")
                continue
            else:
                break
        time.sleep(2)
        os.system("clear")

    elif menu == "remove":
        os.system("clear")
        while True:
            item = input("What would you like to remove?:\n").title()
            if item in todo_list:
                remove = input(
                    f"Are you sure you want to remove {item}? (yes / no)\n")
                if remove == "yes":
                    todo_list.remove(item)
                    print("List item removed!.")
                    time.sleep(2)
                    os.system("clear")
                    break
                elif remove == "no":
                    os.system("clear")
                    break
                else:
                    print("Invalid option. Please enter yes or no.")
            else:
                print("This item is not in the list.")
    elif menu == "view":
        os.system("clear")
        printList()
        print("\n")
        input("Press Enter to continue...").lower()
        os.system("clear")
    elif menu == "delete":
        print("\n")
        delete = input(
            "Are you sure you want to delete the list? (This action cannot be undone!): \n").lower()
        while True:
            if delete == "yes":
                todo_list = []
                print("Your list has been deleted.")
                time.sleep(3)
                os.system("clear")
                break
            elif delete == "no":
                break
            else:
                print("Invalid option. Please enter yes or no.")
                continue
        os.system("clear")
    else:
        print("Invalid option. Please enter either ADD, VIEW or COMPLETE.")
