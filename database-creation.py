import sqlite3

file = "library.db"

try:
    conn = sqlite3.connect(file)
    print("database formed")
except:
    print("database not formed")

cursor = conn.cursor()

cursor.execute("""
            CREATE TABLE IF NOT EXISTS Books(
            Book_id INTEGER PRIMARY KEY,
            Title TEXT,
            Author TEXT,
            Genre TEXT)
            """)

books = [
    ("Dune", "Frank Herbert", "Science Fiction"),
    ("1984", "George Orwell", "Dystopian"),
    ("The Hobbit", "J.R.R. Tolkien", "Fantasy"),
    ("Pride and Prejudice", "Jane Austen", "Romance")
]

cursor.executemany("""
INSERT INTO Books (Title, Author, Genre)
VALUES (?, ?, ?)
""", books)

cursor.execute("""
            CREATE TABLE IF NOT EXISTS Members(
            Member_id INTEGER PRIMARY KEY ,
            First_name TEXT,
            Last_name TEXT)
            """)
members = [
    ("Masie", "Smith"),
    ("Zach", "Jones"),
    ("Clare", "Brown"),
    ("Amy", "Clark"),
    ("Jake", "Webster")
]

cursor.executemany("""
INSERT INTO Members (First_name, Last_name)
VALUES (?,?)
""", members)

cursor.execute("""
            CREATE TABLE IF NOT EXISTS Borrow(
            Borrow_id INTEGER PRIMARY KEY,
            Date_borrowed TEXT,
            Due_date TEXT,
            Return_date TEXT,
            Available BOOL,
            Member_id INTEGER,
            Book_id INTEGER,
            FOREIGN KEY(Member_id) REFERENCES Members(Member_id),
            FOREIGN KEY(Book_id) REFERENCES Books(Book_id))
            """)
borrowed = [
        ("3/5/23", "3/6/23", "23/5/23", True, 2, 4),
        ("5/10/24", "5/11/24", "N/A", False, 5, 7),
        ("25/2/22", "25/3/22", "24/3/22", True, 2 ,1),
        ("7/8/21", "7/9/21", "12/9/21", True, 8, 3)
        ]

cursor.executemany("""
INSERT INTO Borrow(Date_borrowed, Due_date, Return_date, Available, Member_id, Book_id)
VALUES (?,?,?,?,?,?)
""", borrowed)

conn.commit()
conn.close()