from Domain.User import User

class UserLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def user_login(self):
        user = User(self.username, '', self.password)
        maybe_user = user.check_credentials()
        if maybe_user:
            user = maybe_user
            return user
        else:
            return False
