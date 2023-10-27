"""CP1404 Practice and Extension
Person Class"""


class Person:
    """Person class"""
    def __init__(self, first_name, last_name, age):
        """Construct the person class with first_name, last_name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        """Return the string version of Person"""
        return f"{self.first_name} {self.last_name}: {self.age}"

    def __repr__(self):
        """Return the string version of Person"""
        return self.__str__()
