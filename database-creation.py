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
    ("1984", "George Orwell", "Dystopian"),
    ("The Hunger Games", "Suzanne Collins", "Dystopian"),
    ("Lord of the Flies", "William Golding", "Dystopian"),
    ("The Hobbit", "J.R.R. Tolkien", "Fantasy"),
    ("The Lion, the Witch and the Wardrobe", "C.S. Lewis", "Fantasy"),
    ("Harry Potter", "J.K. Rowling", "Fantasy"),
    ("Pride and Prejudice", "Jane Austen", "Romance"),
    ("Wuthering Heights", "Emily Brönte", "Romance"),
    ("Gone with the Wind", "Margaret Mitchell", "Romance"),
    ("The Haunting of Hill House", "Shirley Jackson", "Horror"),
    ("The Shining", "Stephen King", "Horror"),
    ("Dracular", "Bram Stoker", "Horror"),
    ("The Hound of Baskervilles", "Aurther Conan Doyle", "Mystery"),
    ("Muder on the Orient Express", "Agatha Christie", "Mystery"),
    ("The Da Vinci Code", "Dan Brown", "Mystery")
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
    ("03/05/2023", "03/06/2023", "23/05/2023", True, 2, 4),
    ("05/10/2024", "05/11/2024", "N/A", False, 5, 7),
    ("25/02/2022", "25/03/2022", "24/03/2022", True, 2, 1),
    ("07/08/2021", "07/09/2021", "12/09/2021", True, 3, 3),
    ("11/08/2024", "11/09/2024", "N/A", False, 3, 2),
    ("15/01/2024", "15/02/2024", "10/02/2024", True, 1, 5),
    ("20/03/2024", "20/04/2024", "18/04/2024", True, 4, 6),
    ("01/06/2024", "01/07/2024", "N/A", False, 1, 8),
    ("12/07/2024", "12/08/2024", "05/08/2024", True, 5, 9),
    ("10/09/2024", "10/10/2024", "N/A", False, 2, 10),
    ("05/11/2024", "05/12/2024", "01/12/2024", True, 4, 11),
    ("15/01/2025", "15/02/2025", "N/A", False, 3, 12),
    ("31/08/2019", "1/10/2019", "15/08/2019", True, 1, 15)

         ]

cursor.executemany("""
INSERT INTO Borrow(Date_borrowed, Due_date, Return_date, Available, Member_id, Book_id)
VALUES (?,?,?,?,?,?)
""", borrowed)

conn.commit()
conn.close()