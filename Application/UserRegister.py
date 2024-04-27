import sqlite3

from Domain.User import User


class UserRegister:
    def __init__(self, username, role, password):
        self.username = username
        self.role = role
        self.password = password
        self.conn = sqlite3.connect('application_storage.db')


    def register_user(self):
        while True:
            user = User(self.username, self.role, self.password)
            if user.check_username_availability(username):
                user.save()
                return user
            else:
                print("Username already taken. Please try again.")
