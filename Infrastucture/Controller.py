from Application.UserLogIn import UserLogin
from Application.UserRegister import UserRegister
from migrations.UserTable import UserTable


class Controller:
    def __init__(self):
        self.user = 0
        table = UserTable()
        table.create_table()
    def run(self):
        while True:
            is_new_user = input("Are you a new user? (Y/N): ").upper()
            if is_new_user == 'Y':
                username = input("Please write your username: ").upper()
                role = input("Please write your role: ").upper()
                password = input("Please write your password: ").upper()
                registration = UserRegister(username, role, password)
                self.user = registration.register_user()
                break
            elif is_new_user == 'N':
                username = input("Please write your username: ").upper()
                password = input("Please write your password: ").upper()
                login = UserLogin(username, password)
                if login.user_login():
                    self.user = login.user_login()
                    break
                else:
                    print("Invalid credentials. Please try again.")
                break
            else:
                print("Invalid input. Please enter Y or N.")

            # Show ticketing options
        print("Here are the ticketing options:")
