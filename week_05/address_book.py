"""CP1404 Week 5 Practice
Address Book Program"""

MENU = "(A)dd an address\n(C)hange address\n(P)rint address\n(Q)uit"


def main():
    print("Corey's Address Book")
    print(MENU)
    # TODO Add function to load dictionary from file
    name_to_address = {}
    choice = input("What would you like to do? ").upper()
    while choice != "Q":
        if choice == "A":
            add_address_to_dictionary()
        elif choice == "C":
            change_key_value_pair()
        elif choice == "P":
            print_address_from_dictionary()
        else:
            print("Invalid selection")
        print(MENU)
        choice = input("What would you like to do? ").upper()
    # TODO Add function to save dictionary to a file
    print("Farewell")


def add_address_to_dictionary():
    name = get_valid_string("name")
    address = get_valid_string("address")
    print(f"{name} {address}")


def change_key_value_pair(dictionary):
    print("Change address")


def print_address_from_dictionary():
    print("Print address")


def get_valid_string(prompt):
    string = input(f"Enter {prompt}: ")
    while string == "":
        print(f"Invalid {prompt}")
        string = input(f"Enter {prompt}: ")
    return string


main()
