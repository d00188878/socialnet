import sqlite3, os.path

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class socialNetwork:
    def __init__(self):
        self.connection = sqlite3.connect("network.db")
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()

    ### users table
        
    def insertUser(self, username, email, password_encrypted):
        data = [username, email, password_encrypted]
        self.cursor.execute("INSERT INTO users (username, email, password_encrypted) VALUES (?, ?, ?)", data)
        self.connection.commit()

    def getUserById(self, id):
        data = [id]
        self.cursor.execute("SELECT * FROM users WHERE user_id = ?", data)
        user = self.cursor.fetchone()
        return user
    
    def getUserByUsername(self, username):
        data = [username]
        self.cursor.execute("SELECT * FROM users WHERE username = ?", data)
        user = self.cursor.fetchone()
        return user
    
    def updateUser(self, username, email, password_encrypted, id):
        data = [username, email, password_encrypted, id]
        self.cursor.execute("UPDATE users SET username=?, email=?, password_encrypted=? WHERE user_id=?", data)
        self.connection.commit()
    
    
    ## following table
        
    # allow one user to follow another user
    def insertFollowing(self, following_id, follower_id):
        data = [following_id, follower_id]
        self.cursor.execute("INSERT INTO following (following_id, follower_id) VALUES (?, ?)", data)
        self.connection.commit()

    # get all users that one person is following
    def getAllFollowingByFollowerId(self, follower_id):
        data = [follower_id]
        self.cursor.execute("SELECT * FROM following WHERE follower_id = ?", data)
        users = self.cursor.fetchall()
        return users
    
    # get all users that are following one particular person
    def getAllFollowersByFollowingId(self, following_id):
        data = [following_id]
        self.cursor.execute("SELECT * FROM following WHERE following_id = ?", data)
        users = self.cursor.fetchall()
        return users

    # allow one user to unfollow another user
    def removeFollow(self, following_id, follower_id):
        data = [following_id, follower_id]
        self.cursor.execute("DELETE FROM following WHERE follower_id = ? AND following_id = ?", data)
        self.connection.commit()
        
    ##  posts table
    def insertPost(self, user_id, post_type, post_content):
        data = [user_id, post_type, post_content]
        self.cursor.execute("INSERT INTO posts (user_id, post_type, post_content, timestamp) VALUES (?, ?, ?)", data)
        self.connection.commit()

    def getPost(self, id):
        data = [id]
        self.cursor.execute("SELECT * FROM posts WHERE id = ?", data)
        posts = self.cursor.fetchone()
        return post
    
    def updatePost(self, post_content, id):
        data = [post_content, id]
        self.cursor.execute("UPDATE posts SET post_content=? WHERE id=?", data)
        self.connection.commit()
        
    ## block table

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
