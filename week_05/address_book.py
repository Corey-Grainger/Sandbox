"""CP1404 Week 5 Practice
Address Book Program"""

MENU = "(A)dd an address\n(C)hange address\n(P)rint address\n(Q)uit"


def main():
    print("Corey's Address Book")
    print(MENU)
    choice = input("What would you like to do? ").upper()
    while choice != "Q":
        if choice == "A":
            add_address_to_dictionary()
        elif choice == "C":
            change_address_in_dictionary()
        elif choice == "P":
            print_address_from_dictionary()
        else:
            print("Invalid selection")
        print(MENU)
        choice = input("What would you like to do? ").upper()
    print("Farewell")


def add_address_to_dictionary():
    print("Add address")

def change_address_in_dictionary():
    print("Change address")


def print_address_from_dictionary():
    print("Print address")


main()
