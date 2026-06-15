import sqlite3

# Connect to a database (or create it if it doesn't exist)
conn = sqlite3.connect("app.db")

# Create the Cursor object to execute the Command

cursor = conn.cursor()

# Write the SQL Command to create the table

cursor.execute("""
 CREATE TABLE IF NOT EXISTS students (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               grade TEXT
               );                             
               """)

cursor.execute("""
 INSERT INTO students (name, grade) VALUES ('Sachin','A');                             
               """)

# Save (commit) the changes and close the connection

conn.commit()
conn.close()