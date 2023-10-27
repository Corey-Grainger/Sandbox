"""CP1404 Practice and Extension
People Program"""

from person import Person
from operator import attrgetter

MENU = "(A)dd person, (D)isplay people, (Q)uit"


def main():
    """Gets and displays a list people"""
    print(MENU)
    people = []
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "A":
            add_person(people)
        elif choice == "D":
            display_people(people)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye")


def add_person(people):
    """Add a person."""
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = int(input("Enter age: "))
    add_person_to_people(first_name, last_name, age, people)


def add_person_to_people(first_name, last_name, age, people):
    """Append person to people."""
    person = Person(first_name, last_name, age)
    people.append(person)


def display_people(people):
    """Display people sorted and formatted."""
    people.sort(key=attrgetter('age'))
    for person in people:
        print(f"First Name: {person.first_name:12} Last Name: {person.last_name:12} Age: {person.age}")

def test_functions():
    people = []
    add_person(people)
    add_person_to_people("John", "James", 88, people)
    add_person_to_people("John", "Smith", 44, people)
    add_person_to_people("John", "Johnson", 20, people)
    add_person_to_people("James", "John", 1, people)
    display_people(people)

main()
# test_functions()