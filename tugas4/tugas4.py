class Book:
    def __init__(self, title, author, publisher):
        self.title = title
        self.author = author
        self.publisher = publisher
        
class Library:
    def __init__(self, books):
        self.books = books
        
    def add_book(self, book):
        self.books.append(book)
        
    def remove_book(self, book):
        self.books.remove(book)
        
class Shelf:
    def __init__(self, library):
        self.library = library
        self.books = self.library.books
        
    def display_books(self):
        for book in self.books:
            print(book.title)
            
library_books = [Book('The Great Gatsby', 'F. Scott Fitzgerald', 'Scribner'),
                 Book('To Kill a Mockingbird', 'Harper Lee', 'J. B. Lippincott & Co.'),
                 Book('1984', 'George Orwell', 'Secker & Warburg')]

library = Library(library_books)
shelf = Shelf(library)

print("Books in the library:")
shelf.display_books()

new_book = Book('Animal Farm', 'George Orwell', 'Secker & Warburg')
library.add_book(new_book)

print("Books in the library after adding a book:")
shelf.display_books()

removed_book = library_books[0]
library.remove_book(removed_book)

print("Books in the library after removing a book:")
shelf.display_books()
