import datetime

import pytest

from user import User


@pytest.fixture
def existing_user():
    username = 'johndoe'
    banned_until = datetime.datetime(1899, 1, 1)
    balance = 0.00

    user = User(username=username, banned_until=banned_until, balance=balance)

    return user


class InMemoryUserRepository:

    def __init__(self):
        self.users = []

    def add(self, user):
        self.users.append(user)

    def update(self, user):
        existing_user = self.get_by_username(user.username)
        self.users.remove(existing_user)
        self.users.append(user)

    def get_by_username(self, username):
        return next((user for user in self.users if user.username == username), None) #return None instead of StopIteration


@pytest.fixture
def repository_with_existing_user(existing_user):
    repository = InMemoryUserRepository()
    repository.add(existing_user)

    return repository
