import sqlite3

class TheatreTable:
    def __init__(self, db):
        self.conn = sqlite3.connect('application_storage.db')
