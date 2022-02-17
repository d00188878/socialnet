import sqlite3, os.path

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class followingDB:
    def __init__(self):
        self.connection = sqlite3.connect("network.db")
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()

    # allow one user to follow another user
    def insertFollowing(self, following_id, follower_id):
        data = [following_id, follower_id]
        self.cursor.execute("INSERT INTO following (following_id, follower_id) VALUES (?, ?)", data)
        self.connection.commit()

    # get all users that one person is following
    def getAllFollowingByFollowerId(self, follower_id):
        data = [follower_id]
        self.cursor.execute("SELECT * FROM users WHERE follower_id=?", data)
        users = self.cursor.fetchall()
        return users
    
    # get all users that are following one particular person
    def getAllFollowersByFollowingId(self, following_id):
        data = [following_id]
        self.cursor.execute("SELECT * FROM users WHERE following_id=?", data)
        users = self.cursor.fetchall()
        return users

    # allow one user to unfollow another user
    def removeFollow(self, following_id, follower_id):
        data = [following_id, follower_id]
        self.cursor.execute("DELETE FROM users WHERE follower_id=? AND following_id=?", data)
        self.connection.commit()