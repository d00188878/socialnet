import sqlite3, os.path

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class postDB:
    def __init__(self):
        self.connection = sqlite3.connect("network.db")
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()

    # the parent post id thing means we're going to let people do reblogs of other posts and add on their own comments, a la tumblr
    def insertPost(self, user_id, post_content, parent_post_id, timestamp):
        data = [user_id, post_content, timestamp, parent_post_id]
        self.cursor.execute("INSERT INTO posts (user_id, post_content, time_stamp, parent_post_id) VALUES (?, ?, ?, ?, ?)", data)
        self.connection.commit()

    # TODO: RECURSIVELY GET CHILD POSTS BY PARENT POST ID
    def getPostAndChildren(self, id):
        pass

    def getPost(self, id):
        data = [id]
        self.cursor.execute("SELECT * FROM posts WHERE id = ?", data)
        posts = self.cursor.fetchone()
        return post
    
    def updatePost(self, post_content, id):
        data = [post_content, id]
        self.cursor.execute("UPDATE posts SET post_content=? WHERE id=?", data)
        self.connection.commit()
    
    # get all existing posts that one person has ever posted
    def getAllPostsByPosterId(self, user_id):
        data = [user_id]
        self.cursor.execute("SELECT * FROM posts WHERE user_id = ?", data)
        posts = self.cursor.fetchall()
        return posts
    
    # find all posts by users that a certain user is following, in chronological order, limited to a given number
    def getSeveralPostsByFollowerId(self, id, n):
        data = [id, n]
        posts = self.cursor.fetchmany("SELECT * FROM posts JOIN following ON following.follower_id = ? as op_id HAVING posts.user_id = op_id ORDER BY timestamp LIMIT ?", data)
        return posts
    
    def removePost(self, id):
        data = [id]
        self.cursor.execute("DELETE FROM posts WHERE id=?", data)
        self.connection.commit()