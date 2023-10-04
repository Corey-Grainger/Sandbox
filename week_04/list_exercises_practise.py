"""CP1404 Week 4 Practicals List exercises program extra practise"""


# Basic List Operations
def main1():
    """Basic list operations program"""
    numbers = []
    count = 1
    number = get_valid_number(count)
    while number >= 0:
        count += 1
        numbers.append(number)
        number = get_valid_number(count)
    if len(numbers) > 0:
        print_numbers_breakdown(numbers)
    else:
        print("No numbers in list")


def print_numbers_breakdown(numbers):
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


def main2():
    """Woefully inadequate security checker"""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn',
                 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    username = input("Enter your username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


def get_valid_number(count):
    """Gets a valid integer"""
    is_valid_number = False
    while not is_valid_number:
        try:
            number = int(input(f"Number {count}: "))
            is_valid_number = True
        except ValueError:
            print("Number must be a valid integer")
    return number  # Error checking ensures number is defined


main1()
