# Library Management System

A simple command-line library management system written in Python using object-oriented programming.

## Features

- List all books or only available books
- Search books by title or author
- Add new books and members
- Borrow and return books
- Each member can borrow up to 3 books at a time
- A borrowed book cannot be lent to another member
- Library statistics

## Project Structure

| File | Description |
|---|---|
| `book.py` | `Book` class: book details and availability |
| `member.py` | `Member` class: member details and borrowed books |
| `library.py` | `Library` class: manages books, members, borrowing and returning |
| `main.py` | Command-line menu |

## Usage

Requires Python 3.8 or later. No external packages are needed.

```bash
python main.py
```

```
===== LIBRARY MENU =====
1. List all books
2. List available books
3. Search books
4. Add a book
5. Add a member
6. List members
7. Borrow a book
8. Return a book
9. Statistics
0. Exit
Your choice: 7
Member ID: M1
Book ISBN: 002
'1984' was lent to Alihan.
```

## Concepts Used

- Classes, objects and methods
- Class attributes (`Member.MAX_BOOKS`)
- Lists and dictionaries
- List comprehensions
- Input validation
