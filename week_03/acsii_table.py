"""ACSII character displayer"""

import math

MENU = "Get (A)CSII Code from character, Get (C)haracter from ACSII Code, (P)rint ACSII table (Q)uit"
LOWER_BOUND = 33
UPPER_BOUND = 127
NUMBER_OF_ACSII_CHARACTERS = 94

def main():
    """Displays the ACSII value for an input character or the character for an input ACSII value."""
    print(MENU)
    choice = input("What would you like to do?: ").upper()
    while choice != "Q":
        if choice == "A":
            acsii_code, letter = get_acsii_code_from_letter()
            print(f"The ACSII code for {letter} is {acsii_code}")
        elif choice == "C":
            letter, number = get_character_from_valid_acsii_code(LOWER_BOUND, UPPER_BOUND)
            print(f"The character for {number} is {letter}")
        elif choice == "P":
            print_acsii_character_table()
        else:
            print("Invalid choice")
        choice = input("What would you like to do?: ").upper()


def get_acsii_code_from_letter():
    """Gets the acsii code for an input character and returns the code and letter"""
    letter = input("Enter a character: ")
    return ord(letter), letter


def get_character_from_valid_acsii_code(lower_bound, upper_bound):
    """Gets the character for an input number that is a valid ACSII code and returns the character and number"""
    number = int(input("Enter a number between 33 and 127: "))
    while number < lower_bound or number > upper_bound:
        print("Number must be between 33 and 127")
        number = int(input("Enter a number between 33 and 127: "))
    return chr(number), number


def print_acsii_character_table():
    number_of_columns = int(input("How many columns (1-94): "))
    while number_of_columns < 1 or number_of_columns > 94:
        print("Invalid number of columns")
        number_of_columns = int(input("How many columns (1-94): "))
    for column, i in enumerate(range(33, 128), 1):
        if column % number_of_columns == 0 or column == 95:
            end_character = "\n"
        else:
            end_character = " "
        print(f"{i:3} is {chr(i):1}", end=end_character)


main()
