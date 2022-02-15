import sqlite3, os.path

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class blockedDB:
    def __init__(self):
        self.connection = sqlite3.connect("blocked.db")
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()

    # allow one user to block another user
    def insertBlocked(self, blocked_id, blocker_id):
        data = [blocked_id, blocker_id]
        self.cursor.execute("INSERT INTO blocked (blocked_id, blocker_id) VALUES (?, ?)", data)
        self.connection.commit()

    # get all users that one person is blocking
    def getAllBlockedByBlockerId(self, blocker_id):
        data = [blocker_id]
        self.cursor.execute("SELECT * FROM blocked WHERE blocker_id = ?", data)
        users = self.cursor.fetchall()
        return users

    # allow one user to unblock another user
    def removeBlock(self, blocking_id, blocker_id):
        data = [blocking_id, blocker_id]
        self.cursor.execute("DELETE FROM blocked WHERE blocking_id = ? AND blocker_id = ?", data)
        self.connection.commit()