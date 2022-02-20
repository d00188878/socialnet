# To run tests:

To run our tests/queries we used user inputs, depending on the user's
choice input we sent the responses to run the queries. To begin our program, run ```python3 main.py``` in the project directory.

The function of ```main.py``` is self-explanatory. ```dbCli.py``` creates formatted menus and gets user input. ```dataGetterFunctions.py``` is a container for handler functions used for fetching and storing information to the database. The database file is called ```network.db```.

On first running the program, you will see a formatted menu containing letters in square brackets with instructions and syntax on the same line, eg. ```[ga] Get all votes by post ID (syntax: ga <post_id>)``` in the votes menu. Read the instructions carefully and please take care to enter the right information, in the right order.

To make a selection, just type the letters in the square brackets, followed by the relevant information specified in the angle brackets. For example, here you could type ```ga 3``` to get all the existing votes on post 3, whether they are likes or dislikes. (Admittedly, the syntax can be weird and information is requested in different orders sometimes, depending on the command.)