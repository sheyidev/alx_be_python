class Book:

   def __init__(self, title, author):
      self.title = title
      self.author = author

class EBook(Book):
   def __init__(self, title, author, file_size) :
      self.file_size = int(file_size)
      super().__init__(title, author)
      

class PrintBook(Book):
   ##def __init__(self, page_count) -> int:
   def __init__(self, title, author, page_count):
      self.page_count = int(page_count)
      super().__init__(title, author)

class Library:
   def __init__(self):
      self.books = []
   
   def add_book(self, book):
       self.books.append(book)

   def list_books(self):
      for book in self.books:
         print(book)

    
