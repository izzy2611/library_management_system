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
            Genre TEXT,
            Available BOOL)
            """)

books = [
    ("1984", "George Orwell", "Dystopian", True),
    ("The Hunger Games", "Suzanne Collins", "Dystopian", False ),
    ("Lord of the Flies", "William Golding", "Dystopian", True),
    ("The Hobbit", "J.R.R. Tolkien", "Fantasy", True),
    ("The Lion, the Witch and the Wardrobe", "C.S. Lewis", "Fantasy", True),
    ("Harry Potter", "J.K. Rowling", "Fantasy", True),
    ("Pride and Prejudice", "Jane Austen", "Romance", False),
    ("Wuthering Heights", "Emily Brönte", "Romance", False),
    ("Gone with the Wind", "Margaret Mitchell", "Romance", True),
    ("The Haunting of Hill House", "Shirley Jackson", "Horror", False),
    ("The Shining", "Stephen King", "Horror", True),
    ("Dracular", "Bram Stoker", "Horror", False),
    ("The Hound of Baskervilles", "Aurther Conan Doyle", "Mystery",False ),
    ("Muder on the Orient Express", "Agatha Christie", "Mystery", False),
    ("The Da Vinci Code", "Dan Brown", "Mystery", True)
]

cursor.executemany("""
INSERT INTO Books (Title, Author, Genre, Available)
VALUES (?, ?, ?, ?)
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
            Member_id INTEGER,
            Book_id INTEGER,
            FOREIGN KEY(Member_id) REFERENCES Members(Member_id),
            FOREIGN KEY(Book_id) REFERENCES Books(Book_id))
            """)
borrowed = [
    ("03/05/2023", "03/06/2023", "23/05/2023", 2, 4),
    ("05/10/2024", "05/11/2024", "N/A", 5, 7),
    ("25/02/2022", "25/03/2022", "24/03/2022", 2, 1),
    ("07/08/2021", "07/09/2021", "12/09/2021", 3, 3),
    ("11/08/2024", "11/09/2024", "N/A", 3, 2),
    ("15/01/2024", "15/02/2024", "10/02/2024", 1, 5),
    ("20/03/2024", "20/04/2024", "18/04/2024", 4, 6),
    ("01/06/2024", "01/07/2024", "N/A", 1, 8),
    ("12/07/2024", "12/08/2024", "05/08/2024", 5, 9),
    ("10/09/2024", "10/10/2024", "N/A", 4, 10),
    ("05/11/2024", "05/12/2024", "01/12/2024", 4, 11),
    ("15/01/2025", "15/02/2025", "N/A", 3, 12),
    ("31/08/2019", "1/10/2019", "15/08/2019",  1, 15)

         ]

cursor.executemany("""
INSERT INTO Borrow(Date_borrowed, Due_date, Return_date, Member_id, Book_id)
VALUES (?,?,?,?,?)
""", borrowed)

conn.commit()
conn.close()