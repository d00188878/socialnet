import sqlite3, os.path

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class newDB:
    def __init__(self):
        self.connection = sqlite3.connect("network.db")
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()

    def createFreshDb(self):
        self.cursor.execute("DROP TABLE IF EXISTS users")
        self.connection.commit()
        self.cursor.execute("DROP TABLE IF EXISTS blocked")
        self.connection.commit()
        self.cursor.execute("DROP TABLE IF EXISTS following")
        self.connection.commit()
        self.cursor.execute("DROP TABLE IF EXISTS posts")
        self.connection.commit()
        self.cursor.execute("DROP TABLE IF EXISTS votes")
        self.connection.commit()
        tableData = """
        CREATE TABLE users (
            user_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password_encrypted TEXT NOT NULL
        );"""
        self.cursor.execute(tableData)
        self.connection.commit()

        followingData = """
        CREATE TABLE following (
            following_id INTEGER,
            follower_id INTEGER,
            FOREIGN KEY (following_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE
            FOREIGN KEY  (follower_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE
        );"""
        self.cursor.execute(followingData)
        self.connection.commit()

        postData = """
        CREATE TABLE posts (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            post_content TEXT,
            parent_post_id INTEGER,
            time_stamp DATE DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE
        );"""
        self.cursor.execute(postData)
        self.connection.commit()

        voteData = """
        CREATE TABLE votes (
            voter_id INTEGER,
            vote_type INTEGER,
            post_id INTEGER,
            FOREIGN KEY (voter_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE
        );"""
        self.cursor.execute(voteData)
        self.connection.commit()

        blockedData = """
        CREATE TABLE blocked (
            blocked_id INTEGER,
            blocker_id INTEGER,
            FOREIGN KEY (blocker_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE
            FOREIGN KEY (blocked_id) REFERENCES users(user_id) ON DELETE CASCADE ON UPDATE CASCADE
        );
        """
        self.cursor.execute(blockedData)
        self.connection.commit()