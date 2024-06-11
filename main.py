
from book import Book
from patron import Patron
from librarian import Librarian
from library import Library

# Create books
book1 = Book("Araba Sevdası", "Recaizade Mahmut Ekrem", "3162932522")
book2 = Book("Nutuk", "Mustafa Kemal Atatürk", "0987654321")
book3 = Book("Çalı Kuşu", "Reşat Nuri Güntekin", "1122334455")

# Create patrons
patron1 = Patron("Rümeysa", "P1")
patron2 = Patron("Samet", "P2")

# Create librarian
librarian = Librarian("Rıfat Ilgaz", "L1")

# Create library
library = Library("Millet Kütüphanesi")

# Librarian adds books to the library
librarian.add_book(library, book1)
librarian.add_book(library, book2)
librarian.add_book(library, book3)

# Librarian adds patrons to the library
librarian.add_patron(library, patron1)
librarian.add_patron(library, patron2)

# Patron borrows a book
patron1.borrow_book(book1)
patron1.borrow_book(book2)

# Patron returns a book
patron1.return_book(book1)

# List all books and patrons in the library
print("Books in the library:")
for book in library.list_books():
    print(book)

print("\nPatrons in the library:")
for patron in library.list_patrons():
    print(patron)
