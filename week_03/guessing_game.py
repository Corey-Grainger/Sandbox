"""Guessing game program for files and exceptions"""

FILENAME = "secret.txt"


def main():
    secret = load_number(FILENAME)
    guess = get_valid_number()
    while guess != secret:
        print("Guess again!")
        guess = get_valid_number()
    print("You got it!")


def get_valid_number():
    is_valid_input = False
    while not is_valid_input:
        try:
            guess = int(input("Enter guess: "))
            is_valid_input = True
        except ValueError:
            print("Invalid integer")
    return guess # no problem with undefined variable


def load_number(filename):
    """Load an integer from file filename."""
    in_file = open(filename, "r")
    try:
        number = int(in_file.read())
    except ValueError:
        print(f"Invalid contents in {filename}")
        number = 6
    except FileNotFoundError:
        print(f"{filename} not found")
        number = 4
    in_file.close()
    return number


main()
