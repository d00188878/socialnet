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
    
    def checkUserExists(self, id):
        data = [id]
        self.cursor.execute("SELECT * FROM users WHERE user_id=?", data)
        users = self.cursor.fetchall()
        # print(users)
        return users

    # the parent post id thing means we're going to let people do reblogs of other posts and add on their own comments, a la tumblr
    def insertPost(self, user_id, post_content, parent_post_id):
        if not self.checkUserExists(user_id):
            print("Check that user exists")
            return []
        data = [user_id, post_content, parent_post_id]
        self.cursor.execute("INSERT INTO posts (user_id, post_content, parent_post_id) VALUES (?, ?, ?)", data)
        self.connection.commit()

    def getPostAndParents(self, id):
        data = [id]
        recursiveQuery = """
        WITH RECURSIVE rec_parent(id, user_id, post_content, parent_post_id, time_stamp) 
        as (
            SELECT p.id, p.user_id, p.post_content, p.parent_post_id, p.time_stamp
            FROM posts p
            WHERE p.id=? AND p.id IS NOT NULL

            UNION ALL

            SELECT p.id, p.user_id, p.post_content, p.parent_post_id, p.time_stamp
            FROM posts p
            INNER JOIN rec_parent r ON p.id=r.parent_post_id
            ORDER BY p.parent_post_id NULLS FIRST
        )
        SELECT * FROM rec_parent;
        """
        self.cursor.execute(recursiveQuery, data)
        posts = self.cursor.fetchall()
        return posts

    def getPost(self, id):
        data = [id]
        self.cursor.execute("SELECT * FROM posts WHERE id=?", data)
        post = self.cursor.fetchone()
        return post
    
    def updatePost(self, post_content, id):
        data = [post_content, id]
        self.cursor.execute("UPDATE posts SET post_content=? WHERE id=?", data)
        self.connection.commit()
    
    # get all existing posts that one person has ever posted
    def getAllPostsByPosterId(self, user_id):
        if not self.checkUserExists(user_id):
            print("Check that user exists")
            return []
        data = [user_id]
        self.cursor.execute("SELECT * FROM posts WHERE user_id=?", data)
        posts = self.cursor.fetchall()
        return posts
    
    # TODO: TEST: get n posts from a user's list of followed users
    # find all posts by users that a certain user is following, in chronological order, limited to a given number
    def getSeveralPostsByFollowerId(self, id, n):
        data = [id, n]
        getPostsQuery = """
        SELECT * FROM posts p
        JOIN following f1 ON f1.follower_id=p.user_id
        JOIN following f2 ON f2.following_id=p.user_id
        WHERE f1.follower_id=?
        ORDER BY time_stamp LIMIT ?
        """
        self.cursor.execute(getPostsQuery, data)
        posts = self.cursor.fetchall()
        return posts
    
    def removePost(self, id):
        data = [id]
        self.cursor.execute("DELETE FROM posts WHERE id=?", data)
        self.connection.commit()