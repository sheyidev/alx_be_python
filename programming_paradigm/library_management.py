## Objective: Solidify understanding of basic OOP concepts in Python by implementing a system that tracks books in a library, focusing on classes, 
## object instantiation, and method invocation.

##Implement a Book class with public attributes title and author, 
# and a private attribute _is_checked_out to track its availability.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_checked_out(self):
        return self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_checked_out():
                book.check_out()
                return True
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book.is_checked_out():
                book.return_book()
                return True
        return False

    def list_available_books(self):
        available_books = [book for book in self._books if not book.is_checked_out()]
        for book in available_books:
            print(f"{book.title} by {book.author}")

