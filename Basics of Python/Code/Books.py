# Create a class Book with attributes title, author, and price. Create a list of 5 Book objects. Write a method to:
# Print the Title of all the books above price of 500
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
#Create a list of five books
Book1 = Book("Book One", "Author A", 600)
Book2 = Book("Book Two", "Author B", 450)
Book3 = Book("Book Three", "Author C", 700)
Book4 = Book("Book Four", "Author D", 300)
Book5 = Book("Book Five", "Author E", 800)
l1 = [Book1, Book2, Book3, Book4, Book5]
# Method to print titles of books above price of 500
def print_books_above_price(books, price_threshold):
    for book in books:
        if book.price > price_threshold:
            print(f"Title: {book.title}, Author: {book.author}, Price: {book.price}")
# Call the method to print books above price of 500
print_books_above_price(l1, 500)