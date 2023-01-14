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

    # Test initial value book for is required function
    print("\nTest initial value book for required function")
    another_new_book = Book("Developing the Leader Within You", "John Maxwell", 225, False)
    assert another_new_book.title == "Developing the Leader Within You"
    assert another_new_book.author == "John Maxwell"
    assert another_new_book.pages == 225
    assert not another_new_book.is_completed
    assert str(another_new_book) == 'Developing the Leader Within You by John Maxwell, 225 pages '
    print(another_new_book)

    print("\nTest mark required function")
    new_book.mark_required()
    assert not new_book.is_completed
    print(new_book)
    print("\n Test mark_completed")
    new_book.mark_completed()
    assert new_book.is_completed
    print(new_book)

    print("\n Test mark required function for another book")
    another_new_book.mark_required()
    assert not another_new_book.is_completed
    print(another_new_book)
    print("\n Test mark_completed ")
    another_new_book.mark_completed()
    assert another_new_book.is_completed
    print(another_new_book)

    # Test is_long()

    print("\n Test is_long")
    default_book.is_long()
    new_book.is_long()
    another_new_book.is_long()
    print(default_book.is_long())
    print(new_book.is_long())
    print(another_new_book.is_long())
    new_book.mark_required()
    print(new_book.is_long())
    another_new_book.mark_required()
    print(another_new_book.is_long())



    # Test mark_required()



run_tests()
