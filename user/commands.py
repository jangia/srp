import datetime


class BanUser:

    def __init__(self, user_repository, username):
        self.user_repository = user_repository
        self.username = username

    def execute(self):
        user = self.user_repository.get_by_username(self.username)
        user.banned_until = datetime.date.today() + datetime.timedelta(days=7)
