from library import Library


def load_sample_data(library):
    library.add_book("001", "Crime and Punishment", "Fyodor Dostoevsky", 1866)
    library.add_book("002", "1984", "George Orwell", 1949)
    library.add_book("003", "Animal Farm", "George Orwell", 1945)
    library.add_book("004", "The Little Prince", "Antoine de Saint-Exupery", 1943)
    library.add_book("005", "Kurk Mantolu Madonna", "Sabahattin Ali", 1943)
    library.add_member("M1", "Alihan")
    library.add_member("M2", "Ayse")


def print_books(books):
    if not books:
        print("No books found.")
        return
    for book in books:
        print(book)


def show_menu():
    print("\n===== LIBRARY MENU =====")
    print("1. List all books")
    print("2. List available books")
    print("3. Search books")
    print("4. Add a book")
    print("5. Add a member")
    print("6. List members")
    print("7. Borrow a book")
    print("8. Return a book")
    print("9. Statistics")
    print("0. Exit")


def read_year():
    while True:
        value = input("Year: ")
        if value.isdigit():
            return int(value)
        print("Please enter a valid year.")


def main():
    library = Library("City Library")
    load_sample_data(library)
    print(f"Welcome to {library.name}!")

    while True:
        show_menu()
        choice = input("Your choice: ").strip()

        if choice == "1":
            print_books(list(library.books.values()))
        elif choice == "2":
            print_books(library.available_books())
        elif choice == "3":
            keyword = input("Title or author: ")
            print_books(library.search(keyword))
        elif choice == "4":
            isbn = input("ISBN: ")
            title = input("Title: ")
            author = input("Author: ")
            year = read_year()
            print(library.add_book(isbn, title, author, year))
        elif choice == "5":
            member_id = input("Member ID: ")
            name = input("Name: ")
            print(library.add_member(member_id, name))
        elif choice == "6":
            for member in library.members.values():
                print(member)
                for book in member.borrowed_books:
                    print("   -", book.title)
        elif choice == "7":
            member_id = input("Member ID: ")
            isbn = input("Book ISBN: ")
            print(library.borrow_book(member_id, isbn))
        elif choice == "8":
            member_id = input("Member ID: ")
            isbn = input("Book ISBN: ")
            print(library.return_book(member_id, isbn))
        elif choice == "9":
            stats = library.statistics()
            print(f"Total books: {stats['total_books']}")
            print(f"Available:   {stats['available']}")
            print(f"Borrowed:    {stats['borrowed']}")
            print(f"Members:     {stats['members']}")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
