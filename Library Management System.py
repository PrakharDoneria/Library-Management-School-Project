import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="library"
)


cursor = db.cursor()

def create_table():
    
    cursor.execute("CREATE TABLE IF NOT EXISTS books (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), status VARCHAR(10))")

def add_book(title, author):
    
    query = "INSERT INTO books (title, author, status) VALUES (%s, %s, 'Available')"
    values = (title, author)
    cursor.execute(query, values)
    db.commit()
    print("Book added successfully!")

def display_books():
    # Display all books in the 'books' table
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    if books:
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Status: {book[3]}")
    else:
        print("No books found.")

def issue_book(book_id):
    # Update the status of a book to 'Issued'
    query = "UPDATE books SET status = 'Issued' WHERE id = %s AND status = 'Available'"
    values = (book_id,)
    cursor.execute(query, values)
    if cursor.rowcount > 0:
        db.commit()
        print("Book issued successfully!")
    else:
        print("Book not available or invalid ID.")

def return_book(book_id):
    # Update the status of a book to 'Available'
    query = "UPDATE books SET status = 'Available' WHERE id = %s AND status = 'Issued'"
    values = (book_id,)
    cursor.execute(query, values)
    if cursor.rowcount > 0:
        db.commit()
        print("Book returned successfully!")
    else:
        print("Book not issued or invalid ID.")

def delete_book(book_id):
    # Delete a book from the 'books' table
    query = "DELETE FROM books WHERE id = %s"
    values = (book_id,)
    cursor.execute(query, values)
    if cursor.rowcount > 0:
        db.commit()
        print("Book deleted successfully!")
    else:
        print("Invalid ID.")

# Create the 'books' table if it doesn't exist
create_table()

while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        add_book(title, author)

    elif choice == 2:
        display_books()

    elif choice == 3:
        book_id = input("Enter book ID: ")
        issue_book(book_id)

    elif choice == 4:
        book_id = input("Enter book ID: ")
        return_book(book_id)

    elif choice == 5:
        book_id = input("Enter book ID: ")
        delete_book(book_id)

    elif choice == 6:
        break
        db.close()

    else:
        print("Invalid choice. Please try again.")



