# Import required modules
import json
import os


# Define the Book class
class Book:
    def __init__(self, book_id, title, author, status="available"):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status

    def to_dict(self):
        # Convert book object to dictionary (for JSON saving)
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "status": self.status,
        }


# Define the user class


class User:
    def __init__(self, user_id, name, issued_books=None):
        self.user_id = user_id
        self.name = name
        self.issued_books = issued_books if issued_books is not None else []
        """
        If issued_books has a value → use it
        If issued_books is None → use an empty list []
        """

    def to_dict(self):
        # Convert user object to dictionary (for JSON saving)
        return {
            "user_id": self.user_id,
            "name": self.name,
            "issued_books": self.issued_books,
        }
    

# Define the Library Management System class

class Library:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.load_data() # Load data from JSON files on initialization
        
    def load_data(self):
        # load books data from JSON file
        if os.path.exists("books.json"):
            with open("books.json", "r") as f:
                books_data = json.load(f)
                for book_id, book_info in books_data.items():
                    self.books[book_id] = Book(**book_info)
    
        # load users data from JSON file
        if os.path.exists("users.json"):
            with open("users.json", "r") as f:
                users_data = json.load(f)
                for user_id, user_info in users_data.items():
                    self.users[user_id] = User(**user_info)
    
    def save_data(self):
        # save books data to json file
        with open("books.json", "w") as f:
            books_data = {book_id: book.to_dict() for book_id, book in self.books.items()}
            json.dump(books_data, f, indent=4)
        
        # save users data to json file
        with open("users.json", "w") as f:
            users_data = {user_id: user.to_dict() for user_id, user in self.users.items()}
            json.dump(users_data, f, indent=4)
            
    def add_book(self):
        book_id = input("Enter Book ID: ")

        if book_id in self.books:
            print("Book ID already exists!")
            return

        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        self.books[book_id] = Book(book_id, title, author)
        self.save_data()
        print("Book added successfully!")

    def add_user(self):
        user_id = input("Enter User ID: ")

        if user_id in self.users:
            print("User ID already exists!")
            return

        name = input("Enter User Name: ")

        self.users[user_id] = User(user_id, name)
        self.save_data()
        print("User added successfully!")
        
    def issue_book(self):
        user_id = input("Enter User ID: ")
        book_id = input("Enter Book ID to issue: ")
        
        if user_id not in self.users:
            print("User ID does not exist!")
            return
        
        if book_id not in self.books:
            print("Book ID does not exist!")
            return
        
        book = self.books[book_id]
        user = self.users[user_id]
        
        if book.status == "issued":
            print("Book is already issued!")
            return
        
        # Restric t user to issue max 3 books
        if len(user.issued_books)>=3:
            print("User has already issued maximum number of books!")
            return
        
        book.status = "issued"
        user.issued_books.append(book_id)
        self.save_data()
        print("Book issued successfully!")
        
        
        def return_book(self):
            user_id = input("Enter User ID: ")
            book_id = input("Enter Book ID to return: ")
            
            if user_id not in self.users:
                print("User ID does not exist!")
                return
        
            if book_id not in self.books:
                print("Book ID does not exist!")
                return
            
            book = self.books[book_id]
            user = self.users[user_id]
            if book_id not in user.issued_books:
                print("This book was not issued to this user!")
                return
            
            book.status = "available"
            user.issued_books.remove(book_id)
            self.save_data()
            print("Book returned successfully!")
            
            # Available books
            def list_available_books(self):
                print("Available Books:")
                for book in self.books.values():
                    if book.status == "available":
                        print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}")
            
            # Issued books
            def list_issued_books(self):
                print("Issued Books:")
                for book in self.books.values():
                    if book.status == "issued":
                        print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}")
            
            # user list
            def list_users(self):
                print("Registered Users:")
                for user in self.users.values():
                    print(f"ID: {user.user_id}, Name: {user.name}, Issued Books: {user.issued_books}")
                    

def main():
    library = Library()
    while True:
        print("\n====== LIBRARY MANAGEMENT SYSTEM ======")
        print("1. Add Book")
        print("2. Add User")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. List Available Books")
        print("6. List Issued Books")
        print("7. List Users")
        print("8. Exit")
    
        choice = input("Enter your choice: ")
        
        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.add_user()
        elif choice == "3":
            library.issue_book()
        elif choice == "4":
            library.return_book()
        elif choice == "5":
            library.list_available_books()
        elif choice == "6":
            library.list_issued_books()
        elif choice == "7":
            library.list_users()
        elif choice == "8":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")