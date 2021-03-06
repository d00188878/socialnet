import sqlite3, os.path

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class userDB:
    def __init__(self):
        self.connection = sqlite3.connect("network.db")
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()
    
    def checkUserExists(self, id):
        data = [id]
        self.cursor.execute("SELECT * FROM users WHERE user_id=?", data)
        return self.cursor.fetchall()

    def insertUser(self, username, email, password_encrypted):
        data = [username, email, password_encrypted]
        self.cursor.execute("INSERT INTO users (username, email, password_encrypted) VALUES (?, ?, ?)", data)
        self.connection.commit()

    def deleteUser(self, id):
        if not self.checkUserExists(id):
            print("Check that user exists")
            return []
        data = [id]
        self.cursor.execute("DELETE FROM users where user_id=?", data)
        self.connection.commit()
        
    def getUser(self, id):
        if not self.checkUserExists(id):
            print("Check that user exists")
            return []
        data = [id]
        self.cursor.execute("SELECT * FROM users WHERE user_id=?", data)
        user = self.cursor.fetchone()
        return user
    
    def getAllUsers(self):
        self.cursor.execute("SELECT * FROM users")
        users = self.cursor.fetchall()
        return users
    
    def updateUser(self, username, email, password_encrypted, id):
        if not self.checkUserExists(id):
            print("Check that user exists")
            return []
        data = [username, email, password_encrypted, id]
        self.cursor.execute("UPDATE users SET username=?, email=?, password_encrypted=? WHERE user_id=?", data)
        self.connection.commit()