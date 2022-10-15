
birthdays = {}

def lookup_birthday():
    name = input("Please enter a name: ")
    if name in birthdays:
        print(name, "was born on", birthdays[name])
    else:
        print(name, "is not in the dictionary")


def add_birthday():
    name = input("Please enter a name: ")
    birthday = input("Please enter the birthday: ")
    if name in birthdays:
        print(name, "is already in the dictionary")
    else:
        birthdays[name] = birthday

def change_birthday():
    name = input("Please enter a name: ")
    if name in birthdays:
        birthday = input("Please enter the updated birthday: ")
        birthdays[name] = birthday
    else:
        print(name, "is not in the dictionary")


def delete_birthday():
    name = input("Please enter a name: ")
    if name in birthdays:
        birthdays.pop(name, "")
    else:
        print(name, "is not in the dictionary")


choice = "0"
while choice != "5":
    # os.system("clear")
    choice = input("1. Lookup a birthday\n2. Add a birthday\n3. Change a birthday\n4. Delete a birthday\n5. Quit\nPlease enter your choice: ")

    if choice == "1":
        lookup_birthday()
    elif choice == "2":
        add_birthday()
    elif choice == "3":
        change_birthday()
    elif choice == "4":
        delete_birthday()
    elif choice != "5":
        print("Invalid input")