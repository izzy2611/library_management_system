import sqlite3

file = "library.db"

try:
    conn = sqlite3.connect(file)
    print("database formed")
except:
    print("database not formed")

cursor = conn.cursor()

cursor.execute("""
            CREATE TABLE Books(
            Book_id INTEGER PRIMARY KEY,
            Title TEXT,
            Author TEXT,
            Genre TEXT,
            Available BOOLEAN)
            """)

cursor.execute("""
            CREATE TABLE Author(
            First_name TEXT,
            Last_name TEXT,
            Book_id INTEGER
            PRIMARY KEY(First_name, Last_name),
            FOREIGN KEY(Book_id) REFERENCES Books(Book_id))
            """)
conn.commit()
conn.close()