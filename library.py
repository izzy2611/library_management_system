import sqlite3
import sys
from datetime import datetime, timedelta

#Displays options and prompts the user to pick one
print(" 1. See a which books you've borrowed \n 2. See all the available books of a genre \n 3. Take out a book")
user_option = input("Please pick an option:")


#Return a list of all the books a specified member has borrowed 
def borrowed_books(conn, Member_id):
        query = ('''
                SELECT DISTINCT First_name, Last_name, Title, Date_Borrowed
                FROM Books
                JOIN Borrow ON Books.book_id = Borrow.book_id
                JOIN Members ON Borrow.Member_id = Members.Member_id
                WHERE Members.Member_id = ?''')
        cursor = conn.execute(query, (Member_id,))
        return cursor.fetchall()

#connects to the database and calls the function 'borrowed_books' using their member id 
conn = sqlite3.connect("library.db")
if user_option == "1":    
        user_id = input("What is your Member_id?")
        print(borrowed_books(conn, user_id))
 


#Return a list of all the available books in the specific genre
def book_genre(conn, Genre):
        query = (''' 
               SELECT DISTINCT Title, Author 
                FROM Books
                LEFT JOIN Borrow ON Books.Book_id = Borrow.Book_id
                WHERE Genre = ? AND Books.Available == True
                ''')
 
        cursor = conn.execute(query, (Genre,))
        return cursor.fetchall()
        

#connects to the database and calls the function 'book_genre' based on user input
conn = sqlite3.connect("library.db")
if user_option == "2":
        user_genre = input("What type of genre would you like to search for?")
        print(book_genre(conn, user_genre))


#Allows the user to borrow a book
def take_out_book (conn, Member_id):

        #Selects all available books 
        query = ('''
        SELECT  Books.Book_id, Title 
        FROM Books
        LEFT JOIN Borrow ON Books.Book_id = Borrow.Book_id
        WHERE Return_date != "N/A" OR Return_date IS NULL
        ''')
        cursor = conn.execute(query)

        #Displays available books 
        print("Available Books:")
        for book in cursor.fetchall():
                print(book)
        
        Book_id=input("Please enter the number of the book you would like to borrow?")

        #Calculates borrow date and return date
        borrow_date = datetime.now().date()
        due_date = borrow_date + timedelta(days=30)
        borrow_date = borrow_date.strftime("%d/%m/%y")
        due_date = due_date.strftime("%d/%m/%y")

        #Inserts this information into the borrow table 
        query = ('''
        INSERT INTO Borrow(Date_borrowed, Due_date, Return_date, Member_id, Book_id)
        VALUES (?,?,?,?,?)
        ''')

        #Puts the values into the columns
        conn.execute(query, (
        borrow_date,
        due_date,
        "N/A",
        Member_id,
        Book_id
        ))

        query = (''' 
                UPDATE Books
                SET Available = False
                WHERE Books.book_id = Book_id
        ''')
        conn.execute(query,)
        print(cursor.fetchall())
        conn.commit()

##connects to the database and calls the function 'take_out_book' based on member id
conn = sqlite3.connect("library.db")
if user_option == "3":
        member_id = input("What is your member id?")
        print(take_out_book(conn, member_id))
        
