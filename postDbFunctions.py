import sqlite3, os.path

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class postDB:
    def __init__(self):
        self.connection = sqlite3.connect("posts.db")
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()

    def insertPost(self, user_id, post_type, post_content, timestamp):
        data = [user_id, post_type, post_content, timestamp]
        self.cursor.execute("INSERT INTO posts (user_id, post_type, post_content, timestamp) VALUES (?, ?, ?, ?)", data)
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