import sqlite3
## connect to the database

connection = sqlite3.connect("student.db")

##create a cursor object to insert record, create table

cursor = connection.cursor()

##create the table

table_info = """
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25));

"""
cursor.execute(table_info)

##insert the records

cursor.execute('''INSERT Into STUDENT values('Rahul','Data Science','A')''')
cursor.execute('''INSERT Into STUDENT values('Rohit','DEVOPS','B')''')  
cursor.execute('''INSERT Into STUDENT values('Ravi','Data Science','C')''')
cursor.execute('''INSERT Into STUDENT values('Raj','Data Science','D')''')
cursor.execute('''INSERT Into STUDENT values('Vikas','DEVOPS','A')''')
cursor.execute('''INSERT Into STUDENT values('Vivek','DEVOPS','B')''')
cursor.execute('''INSERT Into STUDENT values('Vijay','Data Science','C')''')

## Display the records

print("The inserted records are:")
data = cursor.execute('''SELECT * FROM STUDENT''')
for record in data:
    print(record)