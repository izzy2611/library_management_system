import sqlite3
import sys

print("1. See a which books you've borrowed"\
      " 2. See all the available books of a genre")

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

conn = sqlite3.connect("library.db")
if user_option == " 1":    
        user_id = input("What is your Member_id?")
        print(borrowed_books(conn, user_id))
 


#Return a list of all the available books in the specific genre
def book_genre(conn, Genre):
        query = (''' 
               SELECT DISTINCT Title, Author 
                FROM Books
                LEFT JOIN Borrow ON Books.Book_id = Borrow.Book_id
                WHERE Genre = ? AND Return_date != "N/A"
                ''')
 
        cursor = conn.execute(query, (Genre,))
        return cursor.fetchall()
        


conn = sqlite3.connect("library.db")
if user_option == " 2":
        user_genre = input("What type of genre would you like to search for?")
        print(book_genre(conn, user_genre))
#print(borrowed_books(conn,2))
#print(book_genre(conn, "Romance"))

#Allows the user to borrow a book
def take_out_book (conn):
        query = ('''
        SELECT Title 
        FROM Books
        LEFT JOIN Borrow ON Books.Book_id = Borrow.Book_id
        WHERE Return_date != "N/A" OR Return_date IS NULL
        ''')
        print("Available books:")
        cursor = conn.execute(query,)
        print(cursor.fetchall())

conn = sqlite3.connect("library.db")
if user_option == " 3":
        take_out_book(conn)
        user_book = input("What book would you like to borrow?")
        print(take_out_book(conn, user_book))
        