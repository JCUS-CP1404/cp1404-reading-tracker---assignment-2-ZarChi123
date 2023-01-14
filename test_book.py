"""Tests for Book classes"""
from book import Book


def run_tests():
    """Test Book class."""

    # Test empty book (defaults)
    print("Test empty book:")
    default_book = Book()
    print(default_book)
    assert default_book.title == ""
    assert default_book.author == ""
    assert default_book.pages == 0
    assert not default_book.is_completed  # assert "not" added because of False
    print(default_book)
    # output should look like Empty Book by Unknown Author,0 pages

    # Test initial-value book
    print("Test initial-value book:")
    new_book = Book("Fish Fingers", "Dory", 501, True)
    assert new_book.title == "Fish Fingers"
    assert new_book.author == "Dory"
    assert new_book.pages == 501
    assert new_book.is_completed
    assert str(new_book) == 'Fish Fingers by Dory, 501 pages (completed)'
    print(new_book)

    # TODO: Write tests to show this initialisation works

    # Test mark_required()
    # TODO: Write tests to show the mark_required() method works

    # Test is_long()
    # TODO: Write tests to show the is_long() method works

    # TODO: Add more tests, as appropriate


run_tests()
