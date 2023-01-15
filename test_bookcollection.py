"""(Incomplete) Tests for BookCollection class."""
from bookcollection import BookCollection
from book import Book


def run_tests():
    """Test BookCollection class."""

    # Test empty BookCollection (defaults)
    print("Test empty BookCollection:")
    book_collection = BookCollection()
    print(book_collection)
    assert not book_collection.books  # PEP 8 suggests not using len() to test for empty lists

    # Test loading books
    print("Test loading books:")
    book_collection.load_books('books.csv')
    print(book_collection)
    assert book_collection.books  # assuming CSV file is non-empty, length should be non-zero

    # Test adding a new Book with values
    print("Test adding new book:")
    book_collection.add_book(Book("War and Peace", "William Shakespeare", 999, False))
    print(book_collection)

    # Test sorting books
    print("Test sorting - author:")
    book_collection.sort("author")
    print(book_collection)
    book_collection.sort("title")
    print(book_collection)
    book_collection.sort("pages")
    print(book_collection)
    book_collection.sort("is_completed")
    print(book_collection)

    print("Test get_required_pages():")
    new_book_collection = BookCollection()
    print("Add required book")
    new_book_collection.add_book(Book("War and Peace", "William Shakespeare", 999, False))
    assert new_book_collection.get_required_pages() == 999
    assert new_book_collection.get_required_books() == 1
    print(new_book_collection)
    print("\n Add required book")
    new_book_collection.add_book(Book("The 360 Degree Leader", "John Maxwell", 369, False))
    assert new_book_collection.get_required_pages() == 1368
    assert new_book_collection.get_required_books() == 2
    print(new_book_collection)
    print("\n Add completed book")
    new_book_collection.add_book(Book("In Search of Lost Time", "Marcel Proust", 93, True))
    assert new_book_collection.get_required_pages() == 1368
    assert new_book_collection.get_required_books() == 2
    print(new_book_collection)

    print("\nTest saving books:")
    book_collection.sort("author")
    book_collection.save_books('book_collection.csv')
    print(book_collection)
    new_book_collection.save_books("new_book_collection.csv")
    print(new_book_collection)

    # Test the max_string length
    # Testing with book collection csv
    print("\nTest max_string_length():")
    book_collection.sort("is_completed")
    # print(book_collection)
    assert book_collection.max_string_length(book_collection.TITLE) == 38
    assert book_collection.max_string_length(book_collection.AUTHOR) == 19
    assert book_collection.max_string_length(book_collection.PAGES) == 3
    print(book_collection)

    # Test the max string length for new book collection
    # Testing with new book collection csv

    assert new_book_collection.max_string_length(new_book_collection.TITLE) == 22
    assert new_book_collection.max_string_length(new_book_collection.AUTHOR) == 19
    assert new_book_collection.max_string_length(book_collection.PAGES) == 3
    print(new_book_collection)


run_tests()