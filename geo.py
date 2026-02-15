import mysql.connector # change everything to mySQL

scan = light # Look for the barcode to scan, also use ardiuno or rspbrrypi for the scanning purposes

def sensor(scan):
    print (barcode)

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

# Check to make sure the database shows up in IDE

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

# Make a table, see if I can streamline and drop some code

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


def main():
    print("Hey! Listen")


if __name__ == 'main':
    main()
