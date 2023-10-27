from user import User
from operator import attrgetter

class Team:
    def __init__(self, users: list, name=""):
        self.users = users
        self.name = name

    def __str__(self):
        return f"Team {self.name}"

    def add(self, user_name):
        self.users.append(User(user_name))

    def delete(self, user_name: str):
        for user in self.users:
            if user.name == user_name:
                self.users.remove(user)

