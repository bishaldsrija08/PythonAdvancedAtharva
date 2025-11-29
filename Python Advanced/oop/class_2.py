class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# method to display book information
    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}")

# object instantiation      
book1 = Book("Harry potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
book3 = Book("The SEO Battlefield", "Jon Doe")

book1.display_info()