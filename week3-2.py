#SCA WEEK 3 ASSIGNMENT2
#Program using Sqlite3 and Python

import sqlite3


conn = sqlite3.connect('my_database.sqlite')
cursor = conn.cursor() #A cursor object is our interface to the database, that allows running anySQL query on our database.
print("Opened database successfully")

cursor.execute('''CREATE TABLE SCHOOL
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         MARKS          INT);''')

cursor.execute("INSERT INTO SCHOOL (ID,NAME,AGE,ADDRESS,MARKS) \
      VALUES (1, 'Hafsah', 22, 'Delhi', 200)");
cursor.execute("INSERT INTO SCHOOL (ID,NAME,AGE,ADDRESS,MARKS) \
      VALUES (2, 'Rohan', 30, 'Mexico', 210)");

conn.commit()
conn.close()