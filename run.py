from network import socialNetwork

network = socialNetwork()

choice = input("Choices (type the number)\n 1 Register New User\n 2 Get User By Id\n 3 Get User By Username\n 4 Update User\n 5 Follow someone\n 6 Check Your Followers\n 8 Remove a follower\n 9 Add post\n 10 See A post\n 11 Update a post\n 12 Block Someone\n 13 Checked blocked people\n 14 Unblock Someone\n") 

if choice =="1":
    username = input("Enter Username: ")
    email = input("Enter Email: ")
    password = input("Enter password: ")
    network.insertUser(username, email, password)
if choice =="2":
    userid = input("Enter User's ID: ")
    network.getUserById(int(userid))
if choice =="3":
    userid = input("Enter User's ID: ")
    network.getUserByUsername(userid)
if choice =="4":
    username = input("Enter Username: ")
    email = input("Enter Email: ")
    password = input("Enter password: ")
    userid = input("Enter User ID: ")
    network.updateUser(username, email, password, int(userid))
if choice == "5":
    you = input("Enter your ID: ")
    following = input("ID of who you'll follow: ")
    network.insertFollowing(int(you), int(following))
if choice == "6":
    userid = input("Enter Your ID: ")
    network.getAllFollowingByFollowerId(int(userid))
if choice == "8":
    you = input("Enter your ID: ")
    unfollow = input("Enter the ID of the person to be unfollow: ")
    network.removeFollow(int(you), int(unfollow))
if choice == "9":
    you = input("Enter your ID: ")
    atype = input("What type of post is it? ")
    content = input("Enter content of the post: ")
    network.insertPost(int(you), atype, content)
if choice == "10":
    post = input("Enter post ID: ")
    network.getPost(int(post))
if choice == "11":
    post= input("Enter post ID: ")
    content = input("Enter the new content: ")
    network.updatePost(content, int(post))
if choice == "12":
    you = input("Enter your ID: ")
    block = input("Enter the person to be blocked: ")
    network.insertBlocked(int(block), int(you))
if choice == "13":
    you = input("Enter you ID: ")
    network.getAllBlockedByBlockerId(int(you))
if choice == "14":
    you = input("Enter you ID: ")
    blocked = input("Enter ID of the blocked person: ")
    network.removeBlock(int(blocked), int(you))
    
    
    
    
    
    
    