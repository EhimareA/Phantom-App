import sqlite3

scan = "Look for barcode"

def sensor(scan):
    print 


# connecting to the database
connection = sqlite3.connect("gfg.db")

# cursor
crsr = connection.cursor()

# print statement will execute if there
# are no errors
print("Connected to the database")


# Connect to the SQLite database (or create it if it doesn't exist)
connection_obj = sqlite3.connect('geek.db') # Geek is example code, don't hold onto any of it

# Create a cursor object to interact with the database
cursor_obj = connection_obj.cursor()

# Drop the GEEK table if it already exists (for clean setup)
cursor_obj.execute("DROP TABLE IF EXISTS GEEK")

# SQL query to create the table
table_creation_query = """
    CREATE TABLE GEEK (
        Email VARCHAR(255) NOT NULL,
        First_Name CHAR(25) NOT NULL,
        Last_Name CHAR(25),
        Score INT
    );
"""

# Execute the table creation query
cursor_obj.execute(table_creation_query)

# Confirm that the table has been created
print("Table is Ready")

# Close the connection to the database
connection_obj.close()

# close the connection
connection.close()

# What information do I want in the app program?

# What TABLES do you need to have in the program?

# Build in an Ardiuno attachment to scan for the current prosthetic barcode that the user has?

print('Hello')

def main():
    print("Hey! Listen")


if __name__ == 'main':
    main()
