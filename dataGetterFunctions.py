from sqlite3 import Timestamp
from userDbFunctions import *
from newDbFunctions import *
from followingDbFunctions import *
from blockedDbFunctions import *
from postDbFunctions import *
from postVotesDbFunctions import *
import time, os

def handleInsertUser(username, email, password):
    db = userDB()
    #insert user if user does not already exist
    # salt = bcrypt.gensalt()
    # password = bcrypt.hashpw(password, salt)
    db.insertUser(username, email, password)

def handleGetUser(id):
    db = userDB()
    return db.getUser(id)

def handleGetAllUsers():
    db = userDB()
    return db.getAllUsers()

def handleUpdateUser(username, email, password, id):
    db = userDB()
    primarykey = int(id)
    db.updateUser(username, email, password, primarykey)

def handleInsertFollowing(following_id, follower_id):
    db = followingDB()
    db.insertFollowing(following_id, follower_id)

def handleGetAllFollowingByFollowerId(follower_id):
    db = followingDB()
    return db.getAllFollowingByFollowerId(follower_id)

def handleGetAllFollowersByFollowingId(following_id):
    db = followingDB()
    return db.getAllFollowersByFollowingId(following_id)

def handleRemoveFollow(following_id, follower_id):
    db = followingDB()
    db.removeFollow()

def handleInsertPost(user_id, post_content, parent_post_id = None):
    timestamp = time.time()
    db = postDB()
    db.insertPost(user_id, post_content, timestamp, parent_post_id)

def handleGetPost(id):
    db = postDB()
    return db.getPost(id)

def handleUpdatePost(post_content, id):
    db = postDB
    db.updatePost(post_content, id)

def handleGetAllPostsByPosterId(user_id):
    db = postDB()
    return db.getAllPostsByPosterId(user_id)

def handleGetSeveralPostsByFollowerId(id, n):
    db = postDB()
    return db.getSeveralPostsByFollowerId(id, n)

def handleRemovePost(id):
    db = postDB()
    db.removePost(id)

def handleInsertVote(vote_type, voter_id, post_id):
    db = votesDB()
    db.insertVote(vote_type, voter_id, post_id)

def handleUpdateVote(vote_type, voter_id, post_id):
    db = votesDB()
    db.updateVote(vote_type, voter_id, post_id)

def handleGetAllVotesByPostId(post_id):
    db = votesDB()
    return db.getAllVotesByPostId(post_id)

def handleGetAllLikesByPostId(post_id):
    db = votesDB()
    return db.getAllLikesByPostId(post_id)

def handleGetAllDislikesByPostId(post_id):
    db = votesDB()
    return db.getAllDislikesByPostId(post_id)

def recreateDb():
    db = newDB()
    db.createFreshDb()