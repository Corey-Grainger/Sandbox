class User:
    def __init__(self, name="", number_of_tacos=5, score=0):
        self.name = name
        self.number_of_tacos = number_of_tacos
        self.score = score

    def __repr__(self):
        return f"{self.name} Tacos: {self.number_of_tacos} Score: {self.score}"

    def give_taco(self, recipient):
        self.number_of_tacos -= 1
        self.score += 1
        recipient.get_taco()

    def get_taco(self):
        self.score += 1


if __name__ == '__main__':
    users = [User("Tim"), User("Michelle"), User("Lindsay")]
    print(users)
    users[0].give_taco(users[1])
    print(users)
