import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE students (Name TEXT, Classes TEXT, Major TEXT, GPA TEXT)')
print ("Table created successfully")
conn.close()
