#Create a library management system that allows users to add, remove, and search for books.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book}")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Removed: {book}")
                return
        print("Book not found.")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"Found: {book}")
                return
        print("Book not found.")

    def show_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("\n--- Library Books ---")
        for book in self.books:
            print(book)
            def main():
               library = Library()
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Show All Books")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(Book(title, author))
        elif choice == '2':
            title = input("Enter book title to remove: ")
            library.remove_book(title)
        elif choice == '3':
            title = input("Enter book title to search: ")
            library.search_book(title)
        elif choice == '4':
            library.show_books()
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
        \  print("Invalid choice. Please try again.")
       