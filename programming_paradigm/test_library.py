from library_management import Book, Library

def test_library_system():
    print("=== LIBRARY MANAGEMENT SYSTEM TEST ===\n")
    
    # Create library and books
    library = Library()
    
    # Add books
    book1 = Book("Brave New World", "Aldous Huxley")
    book2 = Book("1984", "George Orwell")
    book3 = Book("To Kill a Mockingbird", "Harper Lee")
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    print(f"Total books in library: {library.get_total_books()}")
    
    # Test initial state
    print("\n1. Initial available books:")
    library.list_available_books()
    
    # Test checking out books
    print("\n2. Checking out '1984' and 'To Kill a Mockingbird':")
    library.check_out_book("1984")
    library.check_out_book("To Kill a Mockingbird")
    library.list_available_books()
    
    # Test returning a book
    print("\n3. Returning '1984':")
    library.return_book("1984")
    library.list_available_books()
    
    # Test checking out unavailable book
    print("\n4. Trying to check out already checked out book:")
    success = library.check_out_book("To Kill a Mockingbird")
    print(f"Checkout successful: {success}")
    
    # Test returning all books
    print("\n5. Returning all books:")
    library.return_book("To Kill a Mockingbird")
    library.list_available_books()
    
    # Test edge cases
    print("\n6. Edge cases:")
    print(f"Check out non-existent book: {library.check_out_book('Unknown Book')}")
    print(f"Return non-existent book: {library.return_book('Unknown Book')}")

if __name__ == "__main__":
    test_library_system()