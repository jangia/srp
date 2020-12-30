import datetime
import pytest

from user import User, BanUser, ChargeUser


def test_user():
    """
    GIVEN username and banned until date
    WHEN User is initialized
    THEN User's username is set to username and banned_until to banned_until
    """
    username = 'johndoe'
    banned_until = datetime.datetime(1899, 1, 1)
    balance = 0.00

    user = User(username=username, banned_until=banned_until, balance=balance)

    assert user.username == username
    assert user.banned_until == banned_until
    assert user.balance == balance

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

def testchargeuser_whenuserdoesntexist_throws(existing_user, repository_with_existing_user):
    #arrange
    cmd = ChargeUser(
        user_repository=repository_with_existing_user
    )
    username = "not" + existing_user.username

    #act
    with pytest.raises(Exception):
        cmd.execute(username=username, amount=1)

def testchargeuser_whenuserexists_updates_and_persists_balance(existing_user, repository_with_existing_user):
    #arrange
    cmd = ChargeUser(
        user_repository=repository_with_existing_user
    )
    amount_to_charge = 20.20 
    expected_balance = amount_to_charge

    #act
    cmd.execute(username=existing_user.username, amount=amount_to_charge)
    user = repository_with_existing_user.get_by_username(existing_user.username)
    
    #assert
    assert user.balance == expected_balance