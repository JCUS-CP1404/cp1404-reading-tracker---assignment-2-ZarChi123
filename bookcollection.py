"""..."""
from operator import attrgetter
from book import Book
import random

# Create your BookCollection class in this file

TITLE_INDEX = 0
AUTHOR_INDEX = 1
PAGES_INDEX = 2
COMPLETED_INDEX = 3


class BookCollection:
    """Implements the BookCollection class."""

    TITLE = 'title'
    AUTHOR = 'author'
    PAGES = 'pages'

    def __init__(self):
        self.books = []
        self.filename = ''

    def __str__(self):
        """List command implementation."""
        string = ''
        for num, book in enumerate(self.books, start=1):
            # Displaying a list of books
            string += ('{0}{1}. {2:<{5}} by {3:<{6}}  {4:>{7}} page{8}\n'.format(
                # REQUIRED or COMPLETED label
                ' ' if book.is_completed else '*',
                # Book number in the list
                num,
                # Book data
                book.title,
                book.author,
                book.pages,
                # Lengths for aligning strings
                self.max_string_length(BookCollection.TITLE),
                self.max_string_length(BookCollection.AUTHOR),
                self.max_string_length(BookCollection.PAGES),
                '' if book.pages == 1 else 's'
            ))

        if string:
            required = ('You need to read {0} pages in {1} books.'.format(
                self.get_required_pages(),
                self.get_required_books()
            ))
            return string + required
        else:
            return 'Collection of books is empty.'

    def max_string_length(self, attr):
        """Calculates the maximum length of string to align."""
        length = 0
        for book in self.books:
            ln = len(str(getattr(book, attr)))
            if ln > length:
                length = ln
        return length

    def load_books(self, filename=''):

        """Read csv file and creates list of books."""

        self.filename = filename
        try:
            with open(filename, 'r', encoding='UTF-8') as book_file:
                for line in book_file.readlines():
                    self.books.append(Book(*line.rstrip().split(',')))
        except FileNotFoundError:
            print(f"The file \"{filename}\" isn't found.")

    def save_books(self, filename=''):
        """Save csv file for list of books."""
        filename = filename or self.filename
        try:
            with open(filename, 'w', encoding='UTF-8') as book_file:
                for book in self.books:
                    print(book.convert_str_to_csv(), file=book_file)
        except FileNotFoundError:
            print(f"The file \"{filename}\" isn't found.")

    def display_quotes(self, filename=''):
        """Display random quotes after the program end"""
        try:
            with open(filename, "r", encoding="utf-8-sig") as quotes_file:
                quotes = quotes_file.readlines()
                random_quote = quotes[random.randint(0, len(quotes) - 1)]
                return random_quote
        except FileNotFoundError:
            print(f"The file \"{filename}\" isn't found.")

    def add_book(self, book):
        """Add book in collection."""
        self.books.append(book)

    def sort(self, key):
        """Sort books in collection by field."""
        self.books.sort(key=attrgetter(key, BookCollection.TITLE))

    def get_required_pages(self):
        """Get the required number of pages."""
        # Total number of pages to read
        page_nums = 0
        for book in self.books:
            # Count pages that you need to read
            if not book.is_completed:
                page_nums += book.pages
        return page_nums

    def get_required_books(self):
        """Get the required number of books."""
        # Total number of books to read
        book_nums = 0
        for book in self.books:
            # Count books that you need to read
            if not book.is_completed:
                book_nums += 1
        return book_nums

    def __len__(self):
        """Returns length of collection."""
        return len(self.books)

    def __getitem__(self, key):
        """Returns book from collection."""
        return self.books[key]

    def __iter__(self):
        """PyCharm requirements."""
        return iter(self.books)
