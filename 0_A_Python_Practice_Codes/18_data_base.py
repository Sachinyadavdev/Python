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
 INSERT INTO students (name, grade) VALUES ('Rampher','A');                             
               """)

# 1. Execute the select query
cursor.execute("SELECT * FROM students;")

# 2. Use fetchall() to pull the data into a Python list of tuples
rows = cursor.fetchall() 

# 3. Loop through rows and print them
for row in rows:
    print(row) # Each row looks like: (1, 'Sachin', 'A')

# Save (commit) the changes and close the connection

conn.commit()
conn.close()