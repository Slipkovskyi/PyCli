import sqlite3


class User:
    def __init__(self, username, role, password):
        self.username = username
        self.role = role
        self.password = password
        self.conn = sqlite3.connect('application_storage.db')

    def save(self):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO users (username, role, password) VALUES (?, ?, ?)", (self.username, self.role, self.password))
        self.conn.commit()

    def check_credentials(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (self.username, self.password))
        user = cursor.fetchone()
        if user:
            return User(self.username, user[2], self.password)
        else:
            return False

    def check_username_availability(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (self.username,))
        user = cursor.fetchone()
        if user:
            return False
        else:
            return True
