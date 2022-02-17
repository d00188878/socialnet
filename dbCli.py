import dataGetterFunctions as DGF

#TODO: ONLY ALLOW USER-RELATED OPERATIONS IF ALL INVOLVED USER IDS EXIST IN THE USER TABLE
# TODO: ALLOW POST REMOVAL
#TODO: ALLOW USER REMOVAL
#TODO: CASCADE WHEN USER DELETED
#TODO: clean up data ordering in db functions and table

def getUserInput():
    cin = input()
    return list(cin)

def printDataTypeOptions():
    intro = """
    Welcome!
    Please select a data type to work with (just enter the letter in the brackets)

    [u] Users
    [p] Posts
    [f] Follows
    [b] Blocklists
    [v] Votes
    [r] Recreate database from scratch 
    [q] Quit
    """
    print(intro)

def selectOption():
    choice = input("Select: ")
    return choice.split()

def printUserOptions():
    userOptionsDialogue = """
    Viewing user options.
    Select an option (mind the syntax).
    [i] Insert user (syntax: i <username> <email> <password>)
    [g] Get one user by ID (syntax: g <id>)
    [ga] Get all users and their information (syntax: ga)
    [u] Update one user's information (syntax: u <username> <email> <password> <id>)
    [q] Go back
    """
    print(userOptionsDialogue)

def notEnoughArguments():
    print("Not enough arguments provided")

def validateUserOption(choice):
    if choice[0] == "i":
        if len(choice) >= 4:
            DGF.handleInsertUser(choice[1], choice[2], choice[3])
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "g":
        if len(choice) >= 2:
            print(DGF.handleGetUser(choice[1]))
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "ga":
        print(DGF.handleGetAllUsers())
        return False
    elif choice[0] == "u":
        if len(choice) >= 5:
            DGF.handleUpdateUser(choice[1], choice[2], choice[3], choice[4])
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "q":
        return True
    else:
        print("Invalid input.")
        return False

def getUserQueryInput():
    notFinished = True
    while notFinished:
        printUserOptions()
        choice = selectOption()
        if validateUserOption(choice):
            break
    return

def printPostOptions():
    postOptionsDialogue = """
    Viewing post options.
    Select an option (mind the syntax).
    [i] Insert post (syntax: i <user_id> <post_content> <parent_post_id (optional)>)
    [g] Get one post by ID (syntax: g <user_id>)
    [u] Update one post's content by ID (syntax: u <post_content> <id>)
    [ga] Get all posts and their information by one poster's ID (syntax: ga <user_id>)
    [gs] Get n posts from a user's list of followed users, by the ID of that user (syntax: gs <user_id> <n>)
    [q] Go back
    """
    print(postOptionsDialogue)

def validatePostOption(choice):
    if choice[0] == "i":
        if len(choice) >= 3:
            if len(choice) >= 4:
                DGF.handleInsertPost(choice[1], choice[2], choice[3])
            else:
                DGF.handleInsertPost(choice[1], choice[2])
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "g":
        if len(choice) >= 2:
            print(DGF.handleGetPost(choice[1]))
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "ga":
        if len(choice) >= 2:
            print(DGF.handleGetAllPostsByPosterId(choice[1]))
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "u":
        if len(choice) >= 3:
            DGF.handleUpdatePost(choice[1], choice[2])
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "gs":
        if len(choice) >= 3:
            print(DGF.handleGetSeveralPostsByFollowerId(choice[1], choice[2]))
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "q":
        return True
    else:
        print("Invalid input.")
        return False

def getPostQueryInput():
    notFinished = True
    while notFinished:
        printPostOptions()
        choice = selectOption()
        if validatePostOption(choice):
            break
    return

def printFollowsOptions():
    followsOptionsDialogue = """
    Viewing follows options.
    Select an option (mind the syntax).
    [i] Insert follow (syntax: i <following_id> <follower_id>)
    [gto] Get all users that one user is following, by that user's ID (syntax: gto <follower_id>)
    [gfrom] Get all users following one user, by that user's ID (syntax: gfrom <following_id>)
    [r] Remove one user's following of another user (syntax: r <following_id> <follower_id>)
    [q] Go back
    """
    print(followsOptionsDialogue)

def validateFollowsOption(choice):
    if choice[0] == "i":
        if len(choice) >= 3:
            DGF.handleInsertFollowing(choice[1], choice[2])
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "gto":
        if len(choice) >= 2:
            print(DGF.handleGetAllFollowingByFollowerId(choice[1]))
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "gfrom":
        if len(choice) >= 2:
            print(DGF.handleGetAllFollowersByFollowingId(choice[1]))
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "r":
        if len(choice) >= 3:
            DGF.handleRemoveFollow(choice[1], choice[2])
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "q":
        return True
    else:
        print("Invalid input.")
        return False

def getFollowsQueryInput():
    notFinished = True
    while notFinished:
        printFollowsOptions()
        choice = selectOption()
        if validateFollowsOption(choice):
            break
    return

def printBlocklistOptions():
    blocklistOptionsDialogue = """
    Viewing blocklist options.
    Select an option (mind the syntax).
    [i] Insert block (syntax: i <blocked_id> <blocker_id>)
    [ga] Get information of all users that are blocked by one user, by that user's ID. (syntax: ga <blocker_id>)
    [r] Remove one user from another user's blocklist (syntax: r <blocked_id> <blocker_id>)
    [q] Go back
    """
    print(blocklistOptionsDialogue)

def validateBlocklistOption(choice):
    if choice[0] == "i":
        if len(choice) >= 3:
            DGF.handleInsertBlocked(choice[1], choice[2])
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "ga":
        if len(choice) >= 2:
            print(DGF.handleGetAllBlockedByBlockerId(choice[1]))
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "r":
        if len(choice) >= 3:
            DGF.handleRemoveBlock(choice[1], choice[2])
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "q":
        return True
    else:
        print("Invalid input.")
        return False

def getBlocklistsQueryInput():
    notFinished = True
    while notFinished:
        printBlocklistOptions()
        choice = selectOption()
        if validateBlocklistOption(choice):
            break
    return

def printVoteOptions():
    voteOptionsDialogue = """
    Viewing vote options.
    Select an option (mind the syntax).
    [i] Insert vote (syntax: i <vote_type (0 for like, 1 for dislike)> <voter_id> <post_id>)
    [ga] Get all votes by post ID (syntax: ga <post_id>)
    [gl] Get all likes on a post by ID (syntax: gl <post_id>)
    [gd] Get all dislikes on a post by ID (syntax: gd <post_id>)
    [u] Update a vote's type (syntax: u <vote_type> <voter_id> <post_id>)
    [r] Remove one vote from a post (syntax: r <voter_id> <post_id>)
    [q] Go back
    """
    print(voteOptionsDialogue)

def validateVoteOption(choice):
    if choice[0] == "i":
        if len(choice) >= 4:
            DGF.handleInsertVote(choice[1], choice[2], choice[3])
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "ga":
        if len(choice) >= 2:
            print(DGF.handleGetAllVotesByPostId(choice[1]))
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "gl":
        if len(choice) >= 2:
            print(DGF.handleGetAllLikesByPostId(choice[1]))
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "gd":
        if len(choice) >= 2:
            print(DGF.handleGetAllDislikesByPostId(choice[1]))
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "r":
        if len(choice) >= 3:
            DGF.handleRemoveVote(choice[1], choice[2])
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "u":
        if len(choice) >= 3:
            DGF.handleUpdateVote(choice[1], choice[2], choice[3])
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "q":
        return True
    else:
        print("Invalid input.")
        return False

def getVotesQueryInput():
    notFinished = True
    while notFinished:
        printVoteOptions()
        choice = selectOption()
        if validateVoteOption(choice):
            break
    return

def validateDataTypeOption(choice):
    choice = choice[0]
    if choice == "u":
        getUserQueryInput()
        return False
    elif choice == "p":
        getPostQueryInput()
        return False
    elif choice == "f":
        getFollowsQueryInput()
        return False
    elif choice == "b":
        getBlocklistsQueryInput()
        return False
    elif choice == "v":
        getVotesQueryInput()
        return False
    elif choice == "q":
        return True
    elif choice == "r":
        confirm = input("Really delete the database? input y to confirm: ")
        if confirm == "y" or confirm == "Y":
            DGF.recreateDb()
        else:
            return False
    else:
        print("Invalid input.")
        return False

def runDbCli():
    notFinished = True
    while notFinished:
        printDataTypeOptions()
        choice = selectOption()
        if validateDataTypeOption(choice):
            break
    return
