"""Random Things"""

import random

ALPHABET_CHARACTERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "h", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                       "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                       "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def main():
    """Prints results of random booleans functions"""
    random_boolean = generate_first_random_boolean(0.5)
    print(random_boolean)
    random_boolean = generate_second_random_boolean()
    print(random_boolean)
    random_boolean = generate_third_random_boolean()
    print(random_boolean)


# is_randomly_true?
def generate_first_random_boolean(chance_true=0.5):
    """Generates a random boolean with chance of chance_true."""
    return random.random() <= chance_true


def generate_second_random_boolean():
    """Generates a random boolean."""
    return random.randint(1, 100) <= 50


def generate_third_random_boolean():
    """Generates a random boolean"""
    return random.choice(ALPHABET_CHARACTERS).isupper()


main()
