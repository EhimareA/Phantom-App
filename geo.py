import mysql.connector # change everything to mySQL

scan = light # Look for the barcode to scan, also use ardiuno or rspbrrypi for the scanning purposes

def sensor(scan):
    print (barcode)
# NOT using any of this!!! Just to study it to understand how to write SQL code!!

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

# Reformat until nothing looks like the original and understand everything!

DB_NAME = 'prosthetics database'

TABLES = {}
TABLES['prosthethics'] = (
    "CREATE TABLE `prosthetics` ("
    "  `pros_no` int(11) NOT NULL,"
    "  `prosthetic_name` varchar(14) NOT NULL,"
    "  PRIMARY KEY (`pros_no`)"
    ") ENGINE=InnoDB")

TABLES['models'] = (
    "CREATE TABLE `models` ("
    "  `model_no` char(8) NOT NULL,"
    "  `model_date` date NOT NULL,"
    "  `model_name` varchar(40) NOT NULL,"
    "  PRIMARY KEY (`model_no`), UNIQUE KEY `model_name` (`model_name`)"
    ") ENGINE=InnoDB")

TABLES['brands'] = (
    "CREATE TABLE `brands` ("
    "  `emp_no` int(11) NOT NULL,"
    "  `salary` int(11) NOT NULL,"
    "  `from_date` date NOT NULL,"
    "  `to_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`,`from_date`), KEY `emp_no` (`emp_no`),"
    "  CONSTRAINT `salaries_ibfk_1` FOREIGN KEY (`emp_no`) "
    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['prosthetics cost'] = (
    "CREATE TABLE `prosthetics cost` ("
    "  `tier_id` INT PRIMARY KEY IDENTITY(1,1) NOT NULL,"
    "  `product_id` INT NOT NULL,"
    "  `min_quantity INT NOT NULL,"
    "  `max_quanitity` INT NULL," # NULL for above and higher
    "  `price_per_unit` DECIMAL (10,2) NOT NULL,"
    "  PRIMARY KEY (`tier_id`,`product_id`), KEY `emp_no` (`emp_no`),"
    "  KEY `dept_no` (`dept_no`),"
    "  CONSTRAINT `dept_emp_ibfk_1` FOREIGN KEY (`emp_no`) "
    "     REFERENCES `employees` (`emp_no`) ON DELETE CASCADE,"
    "  CONSTRAINT `dept_emp_ibfk_2` FOREIGN KEY (`dept_no`) "
    "     REFERENCES `departments` (`dept_no`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")


def main():
    print("Hey! Listen")


if __name__ == 'main':
    main()
