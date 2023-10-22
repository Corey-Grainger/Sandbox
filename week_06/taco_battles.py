"""CP1404 Taco Battles Program"""


def main():
    teams = [Team([User("Jim"), User("Bob"), User("Barry")], "Wildcats"), Team([User("Fred"), User("Ted"), User("Ned")], "Cowboys")]
    print(teams)
    for team in teams:
        print(f"{team.name}")
        for user in team.users:
            print(f"{user.name} has {user.number_of_tacos} Tacos and a score of {user.score}")