# Import the DBManager
from DBManager import Database

# Create a new database object
db = Database("database.db", True)

# Execute the create tables sql file
# This should only be run the first time the code is executed
db.fTransaction("create_tables.sql")

# Get a username and password
uname = input("Enter your username: ")
pword = input("Enter your password: ")

# Execute sql statement
db.transaction("INSERT into Users VALUES ('{}', '{}');".format(uname,pword))

# Execute a statement to select all users
print(db.fTransaction("fetch_users.sql"))
