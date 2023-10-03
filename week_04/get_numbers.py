
def main():
    """Square a list of input numbers and print it"""
    numbers = get_numbers()
    square_numbers(numbers)
    display_numbers(numbers)


def get_numbers():
    """Get string of numbers and return as list."""
    numbers_string = input("Enter numbers seperated by commas: ")
    number_strings = numbers_string.split(",")
    numbers = [float(string.strip()) for string in number_strings]
    return numbers


def square_numbers(numbers):
    """Square a list of numbers."""
    for i, number in enumerate(numbers):
        numbers[i] = number ** 2


def display_numbers(numbers):
    """Print a list of numbers."""
    print("..".join(str(number) for number in sorted(numbers)))



if __name__ == '__main__':
    main()
