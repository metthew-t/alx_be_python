class Book:
    """
    A class to represent a Book in the library system.
    
    Attributes:
        title (str): The title of the book (public)
        author (str): The author of the book (public)
        _is_checked_out (bool): Private attribute to track availability
    """
    
    def __init__(self, title, author):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute
    
    def check_out(self):
        """Check out the book if it's available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        """Return the book to make it available again."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
    
    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out
    
    def __str__(self):
        """String representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """
    A class to represent a Library that manages a collection of books.
    
    Attributes:
        _books (list): Private list to store Book instances
    """
    
    def __init__(self):
        """Initialize a Library with an empty book collection."""
        self._books = []  # Private list
    
    def add_book(self, book):
        """
        Add a book to the library collection.
        
        Args:
            book (Book): A Book instance to add to the library
        """
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("Only Book instances can be added to the library")
    
    def check_out_book(self, title):
        """
        Check out a book by title if it's available.
        
        Args:
            title (str): The title of the book to check out
            
        Returns:
            bool: True if book was successfully checked out, False otherwise
        """
        for book in self._books:
            if book.title.lower() == title.lower() and book.is_available():
                book.check_out()
                return True
        return False
    
    def return_book(self, title):
        """
        Return a book by title if it was checked out.
        
        Args:
            title (str): The title of the book to return
            
        Returns:
            bool: True if book was successfully returned, False otherwise
        """
        for book in self._books:
            if book.title.lower() == title.lower() and not book.is_available():
                book.return_book()
                return True
        return False
    
    def list_available_books(self):
        """List all books that are currently available for checkout."""
        available_books = [book for book in self._books if book.is_available()]
        
        if not available_books:
            print("No books available in the library.")
        else:
            for book in available_books:
                print(book)
    
    def find_book(self, title):
        """
        Find a book by title (case-insensitive).
        
        Args:
            title (str): The title to search for
            
        Returns:
            Book or None: The book if found, None otherwise
        """
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def get_total_books(self):
        """Get the total number of books in the library."""
        return len(self._books)
    
    def get_checked_out_books(self):
        """Get a list of all checked out books."""
        return [book for book in self._books if not book.is_available()]