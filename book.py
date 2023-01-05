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
        return '{0} by {1},{2} pages {3}'.format(self.title or '"Empty Book', self.author or 'Unknown Author',
                                                 self.pages, '(completed)' if self.is_completed else '', )

    def mark_required(self):
        self.is_completed = False

    def mark_completed(self):
        self.is_completed = True

