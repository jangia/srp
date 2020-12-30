import datetime
from .exceptions import InvalidUserException


class BanUser:

    def __init__(self, user_repository, username):
        self.user_repository = user_repository
        self.username = username #should pass this into execute instead, otherwise BanUser is a one-time use obj

    def execute(self):
        user = self.user_repository.get_by_username(self.username)
        user.banned_until = datetime.date.today() + datetime.timedelta(days=7)

class ChargeUser:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, username, amount):
        user = self.user_repository.get_by_username(username)
        if user is None:
            raise InvalidUserException(f"User {username} doesn't exist")

        user.balance = user.balance + amount
        self.user_repository.update(user)