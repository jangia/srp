import datetime
from .exceptions import InvalidUserException


class BanUser:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def execute(self, username):
        user = self.user_repository.get_by_username(username)
        if user is None: #dupe, should be extracted to a baseclass
            raise InvalidUserException(f"User {username} doesn't exist")

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