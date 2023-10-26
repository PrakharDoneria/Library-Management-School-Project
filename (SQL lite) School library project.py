
import sqlite3

# Connect to the database
conn = sqlite3.connect('school_library.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS books
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT,
              author TEXT,
              year INTEGER,
              status TEXT)''')

# Function to add a new book to the library
def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = int(input("Enter the year of publication: "))

    c.execute("INSERT INTO books (title, author, year, status) VALUES (?, ?, ?, ?)",
              (title, author, year, "Available"))
    conn.commit()
    print("Book added successfully!")

# Function to display all books in the library
def display_books():
    c.execute("SELECT * FROM books")
    books = c.fetchall()

    if not books:
        print("No books found in the library.")
    else:
        print("\nBOOKS IN THE LIBRARY:")
        print("---------------------")
        print("ID   | Title                | Author               | Year  | Status")
        print("-----|----------------------|----------------------|-------|--------")
        for book in books:
            print(f"{book[0]:<4} | {book[1]:<20} | {book[2]:<20} | {book[3]} | {book[4]}")

# Function to search for a book by title
def search_book():
    title = input("Enter the title of the book to search: ")

    c.execute("SELECT * FROM books WHERE title LIKE ?", ('%' + title + '%',))
    books = c.fetchall()

    if not books:
        print("No matching books found.")
    else:
        print("\nMATCHING BOOKS:")
        print("---------------")
        print("ID   | Title                | Author               | Year  | Status")
        print("-----|----------------------|----------------------|-------|--------")
        for book in books:
            print(f"{book[0]:<4} | {book[1]:<20} | {book[2]:<20} | {book[3]} | {book[4]}")

# Function to delete a book from the library
def delete_book():
    book_id = int(input("Enter the ID of the book to delete: "))

    c.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    print("Book deleted successfully!")

# Function to issue a book
def issue_book():
    book_id = int(input("Enter the ID of the book to issue: "))

    c.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    book = c.fetchone()

    if not book:
        print("Book not found.")
    elif book[4] == "Issued":
        print("Book already issued.")
    else:
        c.execute("UPDATE books SET status = ? WHERE id = ?", ("Issued", book_id))
        conn.commit()
        print("Book issued successfully!")

# Function to return a book
def return_book():
    book_id = int(input("Enter the ID of the book to return: "))

    c.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    book = c.fetchone()

    if not book:
        print("Book not found.")
    elif book[4] == "Available":
        print("Book is already available.")
    else:
        c.execute("UPDATE books SET status = ? WHERE id = ?", ("Available", book_id))
        conn.commit()
        print("Book returned successfully!")

# Main menu loop
while True:
    print("\nSCHOOL LIBRARY MANAGEMENT SYSTEM")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Quit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        add_book()
    elif choice == '2':
        display_books()
    elif choice == '3':
        search_book()
    elif choice == '4':
        delete_book()
    elif choice == '5':
        issue_book()
    elif choice == '6':
        return_book()
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
conn.close()


