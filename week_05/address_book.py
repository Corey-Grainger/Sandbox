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
            add_address_to_dictionary(name_to_address)
        elif choice == "C":
            change_value_in_dictionary(name_to_address)
        elif choice == "P":
            print_address_from_dictionary(name_to_address)
        else:
            print("Invalid selection")
        print(MENU)
        choice = input("What would you like to do? ").upper()
    # TODO Add function to save dictionary to a file
    print("Farewell")


def add_address_to_dictionary(dictionary):
    """Add name to address pair to dictionary."""
    name = get_valid_string("name")
    address = get_valid_string("address")
    if name in dictionary.keys():
        print("Name already in dictionary")
    else:
        dictionary[name] = address
    print(f"{name} added to address book with address: {address}")


def change_value_in_dictionary(dictionary):
    """Changes the value for a key in dictionary."""
    name = get_valid_string("name to change")
    if name in dictionary.keys():
        dictionary[name] = get_valid_string("new address")
    else:
        print(f"{name} not in address book")


def print_address_from_dictionary(dictionary):
    name = get_valid_string("name")
    try:
        print(f"{name}'s address is: {dictionary[name]}")
    except KeyError:
        print("Name not in dictionary.")


def get_valid_string(prompt):
    """Gets a non-empty string."""
    string = input(f"Enter {prompt}: ")
    while string == "":
        print(f"Invalid {prompt}")
        string = input(f"Enter {prompt}: ")
    return string


main()
