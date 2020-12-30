import datetime

from user import User, BanUser


def test_user():
    """
    GIVEN username and banned until date
    WHEN User is initialized
    THEN User's username is set to username and banned_until to banned_until
    """
    username = 'johndoe'
    banned_until = datetime.datetime(1899, 1, 1)

    user = User(username=username, banned_until=banned_until)

    assert user.username == username
    assert user.banned_until == banned_until


def test_ban_user(existing_user, repository_with_existing_user):
    """
    GIVEN username of user existing in repository and user repository
    WHEN execute is called on BanUser instance
    THEN existing user is banned for 7 days
    """
    ban_user = BanUser(
        user_repository=repository_with_existing_user, username=existing_user.username
    )
    ban_user.execute()

    user = repository_with_existing_user.get_by_username(existing_user.username)
    banned_until = (datetime.date.today() + datetime.timedelta(days=7))

    assert user.banned_until == banned_until
