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
    
    def checkUserExists(self, id):
        data = [id]
        self.cursor.execute("SELECT * FROM users WHERE users=?", data)
        return self.cursor.fetchall()
        
    def checkFollowing(self, following_id, follower_id):
        data = [following_id, follower_id]
        self.cursor.execute("SELECT 1 FROM following WHERE following_id=? AND follower_id=?", data)
        return self.cursor.fetchone()
    
    def checkBlocked(self, blocked_id, blocker_id):
        data = [blocked_id, blocker_id]
        self.cursor.execute("SELECT 1 FROM blocked WHERE blocked_id=? AND blocker_id=?", data)
        return self.cursor.fetchone()

    # allow one user to follow another user
    def insertFollowing(self, following_id, follower_id):
        if not self.checkUserExists(following_id) or not self.checkUserExists(follower_id):
            print("Check that both users exist")
            return []
        if (self.checkFollowing(following_id, follower_id)):
            # print('already following')
            return []
        # don't let someone follow someone they're blocking or they're being blocked by
        if (self.checkBlocked(following_id, follower_id) or self.checkBlocked(follower_id, following_id)):
            return []
        if follower_id == following_id:
            return []
        data = [following_id, follower_id]
        self.cursor.execute("INSERT INTO following (following_id, follower_id) VALUES (?, ?)", data)
        self.connection.commit()

    # get all users that one person is following
    def getAllFollowingByFollowerId(self, follower_id):
        if not self.checkUserExists(follower_id):
            print("Check that user exists")
            return []
        data = [follower_id]
        getFollowingQuery = """
        SELECT * FROM users
        JOIN following AS f1
            ON users.user_id=f1.following_id
        WHERE f1.follower_id=?
        """
        self.cursor.execute(getFollowingQuery, data)
        users = self.cursor.fetchall()
        return users
    
    # get all users that are following one particular person
    def getAllFollowersByFollowingId(self, following_id):
        if not self.checkUserExists(following_id):
            print("Check that user exists")
            return []
        data = [following_id]
        getFollowerQuery = """
        SELECT * FROM users
        JOIN following AS f1
            ON users.user_id=f1.follower_id
        WHERE f1.follower_id=?
        """
        self.cursor.execute(getFollowerQuery, data)
        users = self.cursor.fetchall()
        return users

    # allow one user to unfollow another user
    def removeFollow(self, following_id, follower_id):
        if not self.checkUserExists(following_id) or not self.checkUserExists(follower_id):
            print("Check that both users exist")
            return []
        data = [following_id, follower_id]
        self.cursor.execute("DELETE FROM following WHERE following_id=? AND follower_id=?", data)
        self.connection.commit()