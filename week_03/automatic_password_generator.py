"""Automatic password generator"""

import random


def main():
    required_number_of_characters = int(input("How many characters: "))
    required_number_of_uppercase_characters = int(input("How many uppercase characters: "))
    required_number_of_lowercase_characters = int(input("How many lowercase characters: "))
    required_number_of_digits = int(input("How many digits: "))
    required_number_of_special_characters = int(input("How many special characters: "))
    random_password = generate_random_password(required_number_of_characters, required_number_of_uppercase_characters,
                                               required_number_of_lowercase_characters,
                                               required_number_of_special_characters, required_number_of_digits)
    print(random_password)
    print(is_valid_password(random_password))


def generate_random_password(required_number_of_characters=12, required_number_of_uppercase_characters=1,
                             required_number_of_lowercase_characters=1, required_number_of_special_characters=1,
                             required_number_of_digits=1, uppercase_characters="ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                             lowercase_characters="abcdefghijklmnopqrstuvwxyz", digits="1234567890",
                             special_characters="!@#$%^&*()_-=+`~,./'[]<>?{}|\\"):
    password_characters = []
    random_password = ""
    for i in range(required_number_of_uppercase_characters):
        password_characters.append(random.choice(uppercase_characters))
    for i in range(required_number_of_lowercase_characters):
        password_characters.append(random.choice(lowercase_characters))
    for i in range(required_number_of_digits):
        password_characters.append(random.choice(digits))
    for i in range(required_number_of_special_characters):
        password_characters.append(random.choice(special_characters))
    while len(password_characters) < required_number_of_characters:
        password_characters.append(
            random.choice(uppercase_characters + lowercase_characters + digits + special_characters))
    random.shuffle(password_characters)
    for character in password_characters:
        random_password += character
    return random_password


def is_valid_password(password, min_uppercase=1, min_lowercase=1, min_digit=1, min_special=1,
                      special_chars_required=True,
                      special_characters="!@#$%^&*()_-=+`~,./'[]<>?{}|\\", min_length=8, max_length=20):
    """Determine if the provided password is valid."""
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.isupper():
            count_upper += 1
        if char.islower():
            count_lower += 1
        if char in special_characters:
            count_special += 1
        if char.isdigit():
            count_digit += 1
    if len(password) < min_length or len(password) > max_length:
        return False
    if count_upper < min_uppercase or count_lower < min_lowercase or count_digit < min_digit:
        return False
    if special_chars_required and count_special < min_special:
        return False
    return True


def test_password_generator():
    password = generate_random_password()
    print(password)
    print(is_valid_password(password))
    password = generate_random_password()
    print(password)
    print(is_valid_password(password))


test_password_generator()
# main()
