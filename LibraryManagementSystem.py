class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    def borrow(self):
        if self.available:
            self.available = False
            return True
        else:
            return False

    def return_book(self):
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def track_available_books(self):
        available_books = []
        for book in self.books:
            if book.available:
                available_books.append(book.title)
        return available_books


class Member:
    def __init__(self, name):
        self.name = name
        self.membership_status = True
        self.borrowed_books = []

    def borrow_book(self, book):
        if self.membership_status and book.borrow():
            self.borrowed_books.append(book.title)
            return True
        else:
            return False

    def return_book(self, book):
        if book.title in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book.title)
            return True
        else:
            return False


# Example usage:
book1 = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

library = Library()
library.add_book(book1)
library.add_book(book2)

member = Member("John Doe")

print(library.track_available_books())
Output: ['Harry Potter and the Sorcerer's Stone', 'To Kill a Mockingbird']

member.borrow_book(book1)
print(book1.available)
# Output: False
print(member.borrowed_books)
# Output: ["Harry Potter and the Sorcerer's Stone"]

member.return_book(book1)
print(book1.available)
# Output: True
print(member.borrowed_books)
# Output: []
