import sqlite3, os.path

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class blockedDB:
    def __init__(self):
        self.connection = sqlite3.connect("network.db")
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()
    
    def checkBlocked(self, blocked_id, blocker_id):
        data = [blocked_id, blocker_id]
        self.cursor.execute("SELECT 1 FROM blocked WHERE blocked_id=? AND blocker_id=?", data)
        users = self.cursor.fetchone()

    # allow one user to block another user
    def insertBlocked(self, blocked_id, blocker_id):
        # don't let someone block themselves
        #TODO: don't let someone block someone they've already blocked
        if blocked_id == blocker_id:
            return
        data = [blocked_id, blocker_id]
        # alreadyBlocked = 
        # if a user is blocking someone they already follow, or who follows them, when adding the block relationship, delete any follow relationship
        self.cursor.execute("INSERT INTO blocked (blocked_id, blocker_id) VALUES (?, ?)", data)
        self.connection.commit()
        self.cursor.execute("DELETE FROM following WHERE following_id=? AND follower_id=?", data)
        self.connection.commit()
        self.cursor.execute("DELETE FROM following WHERE follower_id=? AND following_id=?", data)
        self.connection.commit()


    # get all users that one person is blocking
    def getAllBlockedByBlockerId(self, blocker_id):
        data = [blocker_id]
        self.cursor.execute("SELECT * FROM blocked WHERE blocker_id=?", data)
        users = self.cursor.fetchall()
        return users

    # allow one user to unblock another user
    def removeBlock(self, blocked_id, blocker_id):
        data = [blocked_id, blocker_id]
        self.cursor.execute("DELETE FROM blocked WHERE blocked_id=? AND blocker_id=?", data)
        self.connection.commit()