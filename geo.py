import sqlite3

# connecting to the database
connection = sqlite3.connect("gfg.db")

# cursor
crsr = connection.cursor()

# print statement will execute if there
# are no errors
print("Connected to the database")

# close the connection
connection.close()


print('Hello')

def main():
    print('Hey! Listen")


if __name__ == 'main':
    main()
