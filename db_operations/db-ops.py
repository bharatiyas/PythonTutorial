# To work with My SQL DB we need to install mysql-connector module
# $ pip install mysql-connector

import mysql.connector

# Create a connectior to the DB
connection = mysql.connector.connect(host="localhost", user="springuser", passwd="ThePassword", database = "library_db")

print(connection)

if connection:
    print("Connection Successful")
else:
    print("Connection Unsuccessful")

cursor = connection.cursor()    # returns the cursor

# Execute a SQL query
cursor.execute("show databases")      # Provide the SQL query which you want to execute

for db in cursor:
    print(db)

# Create a table
# cursor.execute("create table EMPLOYEE (EMPLOYEE_ID int, NAME varchar(100), DESIGNATION varchar(100), SALARY DECIMAL(15,2))")

# Insert records using normal SQL query
# cursor.execute("insert into EMPLOYEE (EMPLOYEE_ID, NAME, DESIGNATION, SALARY) values (101, 'Sanjay', 'Developer', 20000)")

# Insert data using Tuple
#insert_data = "insert into EMPLOYEE (EMPLOYEE_ID, NAME, DESIGNATION, SALARY) values(%s, %s, %s, %s)"

records = [
    (102, 'Vandana', 'Manager', 30000),
    (103, 'Idhant', 'CEO', 50000)
]

#cursor.executemany(insert_data, records)

connection.commit()

cursor.execute("select * from EMPLOYEE")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute("select * from EMPLOYEE WHERE SALARY > 25000")
rows = cursor.fetchone()        # Will fetch one record

for row in rows:
    print(row)

cursor.fetchall()

cursor.execute("update EMPLOYEE set SALARY = 70000 WHERE NAME = 'Vandana'")
connection.commit()

cursor.execute("delete from EMPLOYEE where EMPLOYEE_ID = 101")
connection.commit()

