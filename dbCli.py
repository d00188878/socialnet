import dataGetterFunctions as DGF

def getUserInput():
    cin = input()
    return list(cin)

# def handleRequestDataType(data):
#     if data[0] = 

def printDataTypeOptions():
    intro = """
    Welcome!\n
    Please select a data type to work with (just enter the letter in the brackets)\n\n

    [u] Users\n
    [p] Posts\n
    [f] Follows\n
    [b] Blocklists\n
    [v] Votes\n
    [q] Quit
    """
    print(intro)

def selectOption():
    choice = input("Select: ")
    return choice.split()

def printUserOptions():
    userOptionsDialogue = """
    Viewing user options.\n
    Select an option (mind the syntax).\n\n
    [i] Insert user (syntax: i <username> <email> <password>)\n
    [g] Get one user by ID (syntax: g <id>)\n
    [ga] Get all users and their information (syntax: ga)\n
    [u] Update one user's information (syntax: u <username> <email> <password> <id>)\n
    [q] Go back
    """
    print(userOptionsDialogue)

def notEnoughArguments():
    print("Not enough arguments provided")

def validateUserOption():
    if choice[0] == "i":
        if len(choice) >= 4:
            DGF.handleInsertUser(choice[1], choice[2], choice[3])
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "g":
        if len(choice) >= 2:
            DGF.handleGetUser(choice[1])
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "ga":
        DGF.handleGetAllUsers() 
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
    Viewing post options.\n
    Select an option (mind the syntax).\n\n
    [i] Insert post (syntax: i <user_id> <post_content> <parent_post_id (optional)>)\n
    [g] Get one post by ID (syntax: g <user_id>)\n
    [u] Update one post's content by ID (syntax: u <post_content> <id>)\n
    [ga] Get all posts and their information by one poster's ID (syntax: ga)\n
    [gs] Get n posts from a user's list of followed users, by the ID of that user (syntax: gs <user_id> <n>)\n
    [q] Go back
    """
    print(postOptionsDialogue)

def validatePostOption(choice):
    if choice[0] == "i":
        if len(choice) >= 3:
            if len(choice) >= 4:
                DGF.handleInsertPost(choice[1], choice[2], choice[3])
            else:
                DGF.handleInsertUser(choice[1], choice[2])
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "g":
        if len(choice) >= 2:
            DGF.handleGetPost(choice[1])
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "ga":
        if len(choice) >= 2:
            DGF.handleGetAllPostsByPosterId(choice[1])
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
            DGF.handleGetSeveralPostsByFollowerId(choice[1], choice[2])
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
    Viewing follows options.\n
    Select an option (mind the syntax).\n\n
    [i] Insert follow (syntax: i <following_id> <follower_id>)\n
    [gto] Get all users that one user is following, by that user's ID (syntax: gto <follower_id>)\n
    [gfrom] Get all users following one user, by that user's ID (syntax: gfrom <following_id>)\n
    [r] Remove one user's following of another user (syntax: r <following_id> <follower_id>)\n
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
            DGF.handleGetAllFollowingByFollowerId(choice[1])
        else:
            notEnoughArguments()
        return False
    elif choice[0] == "gfrom":
        if len(choice) >= 2:
            DGF.handleGetAllFollowersByFollowingId(choice[1])
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
