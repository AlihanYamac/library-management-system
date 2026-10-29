class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def borrow(self):
        if not self.is_available:
            return False
        self.is_available = False
        return True

    def return_book(self):
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"[{self.isbn}] {self.title} - {self.author}, {self.year} ({status})"
