
class City:

    def __init__(self, name="", population=1000, population_percentage=0.05):
        self.name = name
        self.population = population
        self.population_percentage = population_percentage

    def __repr__(self):
        return f"{self.name}: {self.population} ({self.population_percentage * 100}%)"

    def __add__(self, other):
        return City(self.name[:len(self.name)//2] + other.name[len(other.name)//2:], self.population + other.population, self.population_percentage)


class Person:

    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name}: {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


def test_methods():
    # c1 = City("Rome", 2000000, 0.12)
    # c2 = City("Tokyo", 1500000, 0.09)
    # print (c1 + c2)
    john_smith = Person("John", 44)
    john_jones = Person("John", 44)
    john_james = Person("John", 54)
    jim_jones = Person("Jim", 88)
    jack_smith = Person("Jack", 44)
    print(f"Should be true is {john_smith == john_jones}")
    print(f"Should be false is {john_smith == john_james}")
    print(f"Should be false is {john_smith == jim_jones}")
    print(f"Should be false is {john_smith == jack_smith}")


test_methods()