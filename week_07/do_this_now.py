
class City:

    def __init__(self, name="", population=1000, population_percentage=0.05):
        self.name = name
        self.population = population
        self.population_percentage = population_percentage

    def __repr__(self):
        return f"{self.name}: {self.population} ({self.population_percentage * 100}%)"

    def __add__(self, other):
        return City(self.name[:len(self.name)//2] + other.name[len(other.name)//2:], self.population + other.population, self.population_percentage)


def test_methods():
    c1 = City("Rome", 2000000, 0.12)
    c2 = City("Tokyo", 1500000, 0.09)
    print (c1 + c2)

# test_methods()



