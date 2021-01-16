import datetime
from .exceptions import InvalidUserException

def get_or_throw(user_repository, username):
    user = user_repository.get_by_username(username)
    if user is None:
        raise InvalidUserException(f"User {username} doesn't exist")
    return user

class BanUser:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, username):
        user = get_or_throw(self.user_repository, username)

        user.banned_until = datetime.date.today() + datetime.timedelta(days=7)
        self.user_repository.update(user)

class ChargeUser:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, username, amount):
        user = get_or_throw(self.user_repository, username)
        user.balance = user.balance + amount
        self.user_repository.update(user)