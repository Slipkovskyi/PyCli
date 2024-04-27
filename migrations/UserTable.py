import sqlite3


class UserTable:
    def __init__(self):
        self.conn = sqlite3.connect('application_storage.db')

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            role TEXT,
            password TEXT
        )
        ''')
        self.conn.commit()