class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' added to the library.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book with ISBN {isbn} removed from the library.")
                return
        print(f"No book found with ISBN {isbn}.")

    def display_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)


def input_book_details():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    isbn = input("Enter the ISBN: ")
    return Book(title, author, isbn)


def menu():
    print("\nMenu:")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Display all books")
    print("4. Quit")


if __name__ == "__main__":
    library = Library()

    while True:
        menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            new_book = input_book_details()
            library.add_book(new_book)
        elif choice == "2":
            isbn_to_remove = input("Enter the ISBN of the book you want to remove: ")
            library.remove_book(isbn_to_remove)
        elif choice == "3":
            library.display_books()
        elif choice == "4":
            print("Quitting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
