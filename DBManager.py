# Imports
import sqlite3

# Create a database manager class
class Database(object):

    # Function to initialise the object
    def __init__(self, dbName, suppress = False):

        # Open a connection to the database
        self.conn = sqlite3.connect(dbName)

        # Print warnings if unsuppressed
        if not suppress:
            print("Warning:")
            print("--------")
            print("The Database object was written to help demonstrate how a database works.")
            print("It is not a good idea to use this production code.")
            print("To suppress this warning: db = Database('database.db', True)\n-------\n\n")

    # Destructor
    def __del__(self):

        # Close the connection to the database
        self.conn.close()
        print("Database closed successfully...")

    # Create a function to execute a transaction from a file
    def transaction(self, query):

        # Create a new cursor object for the DB
        c = self.conn.cursor()

        # Try and execute the command, handling database errors
        try:
            c.execute(query)
        except sqlite3.Error as e:
            print("Database Error: \n{}".format(e))
            return
        except Exception as e:
            print("Error: \n{}".format(e))
            return

        # Commit the change
        self.conn.commit()

        # Add the data
        return c.fetchall()

    # Create a function to execute a transaction from a file
    def fTransaction(self, fName):

        # Create a list of return statements
        returns = []

        # Try and open the contents of the file, handling IO errors
        try:
            queries = open(fName).read().split(";")
        except IOError as e:
            print("Error: Accessing file {}\n{}".format(fName, e))
            return returns

        # Execute each query
        for query in queries:

            # Create a new cursor object for the DB
            c = self.conn.cursor()

            # Try and execute the command, handling database errors
            try:
                c.execute(query)
            except sqlite3.Error as e:
                print("Database Error: \n{}".format(e))
                continue
            except Exception as e:
                print("Error: \n{}".format(e))
                continue

            # Commit the change
            self.conn.commit()

            # Add the data
            returns += c.fetchall()

        # Return the list of rows
        return returns
