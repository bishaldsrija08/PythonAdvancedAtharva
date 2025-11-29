# 📘 Mini Project: Library System
# This small project shows how a library works in real life:
# A library has books.
# People (users) can borrow and return books.
# We will make this using Python.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True #Every new book starts as available (meaning no one has borrowed it yet).

# This function tries to borrow the book.
    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
    def return_book(self):
        self.is_available = True

class User:
    def __init__(self,name):
        self.name = name
        self.borrowed_books = [] # List to keep track of borrowed books
    
    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is not available.")
    
    def return_book(self, book):
        book.return_book()
        self.borrowed_books.remove(book)
        print(f"{self.name} returned '{book.title}'")
    

book1 = Book("1984", "George Orwell")
user1 = User("Alice")
user1.borrow_book(book1) # Alice borrows the book
# user1.return_book(book1) # Alice returns the book