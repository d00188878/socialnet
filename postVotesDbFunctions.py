import sqlite3, os.path

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class votesDB:
    def __init__(self):
        self.connection = sqlite3.connect("network.db")
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()
    
    def checkUserExists(self, id):
        data = [id]
        self.cursor.execute("SELECT * FROM users WHERE user_id=?", data)
        return self.cursor.fetchall()

    def insertVote(self, vote_type, voter_id, post_id):
        if not self.checkUserExists(voter_id):
            print("Check that user exists")
            return []
        data = [vote_type, voter_id, post_id]
        self.cursor.execute("INSERT INTO votes (vote_type, voter_id, post_id) VALUES (?, ?, ?)", data)
        self.connection.commit()
    
    def updateVote(self, vote_type, voter_id, post_id):
        if not self.checkUserExists(voter_id):
            print("Check that user exists")
            return []
        data = [vote_type, voter_id, post_id]
        self.cursor.execute("UPDATE votes SET vote_type=? WHERE voter_id=? and post_id=?", data)
        self.connection.commit()
    
    # get all the votes assigned to one particular post, regardless of type
    def getAllVotesByPostId(self, post_id):
        #TODO: don't let someone add another vote to a post they've already voted on
        data = [post_id]
        self.cursor.execute("SELECT * FROM votes WHERE post_id=?", data)
        posts = self.cursor.fetchall()
        return posts

    def getAllLikesByPostId(self, post_id):
        data = [post_id]
        self.cursor.execute("SELECT * FROM votes WHERE post_id=? and vote_type=0", data)
        posts = self.cursor.fetchall()
        return posts

    def getAllDislikesByPostId(self, post_id):
        data = [post_id]
        self.cursor.execute("SELECT * FROM votes WHERE post_id=? and vote_type=1", data)
        posts = self.cursor.fetchall()
        return posts
    
    def removeVote(self, voter_id, post_id):
        data = [voter_id, post_id]
        self.cursor.execute("DELETE FROM votes WHERE voter_id=? AND post_id=?", data)
        self.connection.commit()

    # getAllPostsByVoterId(self, voter_id):
    #     data = [post_id]
    #     self.cursor.execute("SELECT * FROM posts where ")