class Member:
    MAX_BOOKS = 3

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def can_borrow(self):
        return len(self.borrowed_books) < Member.MAX_BOOKS

    def add_book(self, book):
        self.borrowed_books.append(book)

    def remove_book(self, book):
        self.borrowed_books.remove(book)

    def has_book(self, book):
        return book in self.borrowed_books

    def __str__(self):
        return f"[{self.member_id}] {self.name} ({len(self.borrowed_books)}/{Member.MAX_BOOKS} books)"
