from book import Book
from member import Member


class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}
        self.members = {}

    def add_book(self, isbn, title, author, year):
        if isbn in self.books:
            return f"A book with ISBN {isbn} already exists."
        self.books[isbn] = Book(isbn, title, author, year)
        return f"'{title}' was added."

    def add_member(self, member_id, name):
        if member_id in self.members:
            return f"A member with ID {member_id} already exists."
        self.members[member_id] = Member(member_id, name)
        return f"Member '{name}' was added."

    def borrow_book(self, member_id, isbn):
        member = self.members.get(member_id)
        book = self.books.get(isbn)

        if member is None:
            return "Member not found."
        if book is None:
            return "Book not found."
        if not member.can_borrow():
            return f"{member.name} cannot borrow more than {Member.MAX_BOOKS} books."
        if not book.borrow():
            return f"'{book.title}' is already borrowed."

        member.add_book(book)
        return f"'{book.title}' was lent to {member.name}."

    def return_book(self, member_id, isbn):
        member = self.members.get(member_id)
        book = self.books.get(isbn)

        if member is None:
            return "Member not found."
        if book is None:
            return "Book not found."
        if not member.has_book(book):
            return f"{member.name} does not have '{book.title}'."

        member.remove_book(book)
        book.return_book()
        return f"'{book.title}' was returned by {member.name}."

    def search(self, keyword):
        keyword = keyword.lower()
        return [
            book for book in self.books.values()
            if keyword in book.title.lower() or keyword in book.author.lower()
        ]

    def available_books(self):
        return [book for book in self.books.values() if book.is_available]

    def statistics(self):
        total = len(self.books)
        available = len(self.available_books())
        return {
            "total_books": total,
            "available": available,
            "borrowed": total - available,
            "members": len(self.members),
        }
