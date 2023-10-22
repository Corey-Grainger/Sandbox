from user import User

class Team:
    def __init__(self, users: list, name=""):
        self.users = users
        self.name = name

    def __repr__(self):
        return f"Team {self.name}"

    def add_user(self, name):
        self.users.append(User(name))


if __name__ == '__main__':
    teams = [Team([User("Jim"), User("Bob"), User("Barry")], "Wildcats"), Team([User("Fred"), User("Ted"), User("Ned")], "Cowboys")]
    print(teams)
    for team in teams:
        print(f"{team.name}")
        for user in team.users:
            print(f"{user.name} has {user.number_of_tacos} Tacos and a score of {user.score}")
    teams[0].add_user("Sam")
    for team in teams:
        print(f"{team.name}")
        for user in team.users:
            print(f"{user.name} has {user.number_of_tacos} Tacos and a score of {user.score}")
