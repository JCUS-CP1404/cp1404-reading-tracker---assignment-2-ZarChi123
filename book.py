"""..."""
REQUIRED_TO_READ = "r"
COMPLETED = "c"


class Book:
    """..."""

    def __init__(self, title="", author='', pages=0, is_completed=False):

        self.title = title
        self.author = author
        self.pages = int(pages)

        if isinstance(is_completed, bool):
            self.is_completed = is_completed
        elif is_completed in {REQUIRED_TO_READ, COMPLETED}:
            self.is_completed = True if is_completed == COMPLETED else False
        else:
            raise ValueError

    def __str__(self):
        """String formatting """
        return '{0} by {1},{2} pages {3}'.format(self.title or '"Empty Book', self.author or 'Unknown Author',
                                                 self.pages, '(completed)' if self.is_completed else '', )

    def mark_completed(self):
        """Mark the book as completed"""
        self.is_completed = True

    def mark_required(self):
        """Mark books that are required to read"""
        self.is_completed = False

    def convert_str_to_csv(self):
        """Convert  new book data to csv file"""
        return ','.join(
            (self.title, self.author, str(self.pages), COMPLETED if self.is_completed else REQUIRED_TO_READ))

    def is_long(self):
        """Checks if the book has more than 500 pages and mark long"""
        if self.pages > 500:
            return True
        else:
            return False
