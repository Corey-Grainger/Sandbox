"""ACSII character displayer"""

MENU = "Get (A)CSII Code from character, Get (C)haracter from ACSII Code, (P)rint ACSII table (Q)uit"

LOWER_BOUND = 33
UPPER_BOUND = 127


def main():
    """Displays the ACSII value for an input character or the character for an input ACSII value."""
    print(MENU)
    choice = input("What would you like to do?: ").upper()
    while choice != "Q":
        if choice == "A":
            acsii_code, letter = get_acsii_code_from_letter()
            print(f"The ACSII code for {letter} is {acsii_code}")
        elif choice == "C":
            letter, number = get_character_from_valid_acsii_code()
            print(f"The character for {number} is {letter}")
        elif choice == "P":
            print_acsii_characters()
        else:
            print("Something went wrong")
        choice = input("What would you like to do?: ").upper()


def get_acsii_code_from_letter():
    """Gets the acsii code for an input character and returns the code and letter"""
    letter = input("Enter a character: ")
    return ord(letter), letter


def get_character_from_valid_acsii_code():
    """Gets the character for an input number that is a valid ACSII code and returns the character and number"""
    number = int(input("Enter a number between 33 and 127: "))
    while number < LOWER_BOUND or number > UPPER_BOUND:
        print("Number must be between 33 and 127")
        number = int(input("Enter a number between 33 and 127: "))
    return chr(number), number


def print_acsii_characters():
    for i in range(33, 128):
        print(f"{i:3} {chr(i)}")


main()
