import sqlite3, os.path

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class userDB:
    def __init__(self):
        self.connection = sqlite3.connect("users.db")
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()

    def insertUser(self, username, email, password_encrypted):
        data = [username, email, password_encrypted]
        self.cursor.execute("INSERT INTO users (username, email, password_encrypted) VALUES (?, ?, ?)", data)
        self.connection.commit()

    def getUser(self, id):
        data = [id]
        self.cursor.execute("SELECT * FROM users WHERE id = ?", data)
        user = self.cursor.fetchone()
        return user
    
    def updateUser(self, username, email, password_encrypted, id):
        data = [username, email, password_encrypted, id]
        self.cursor.execute("UPDATE users SET username=?, email=?, password_encrypted=? WHERE id=?", data)
        self.connection.commit()