"""
Name:Zar Chi Oo
Date:12/1/2023
Brief Project Description:Reading Tracker Program Assignment 2
GitHub URL:https://github.com/JCUS-CP1404/cp1404-reading-tracker---assignment-2-ZarChi123.git
"""
# Create your main program in this file, using the ReadingTrackerApp class


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button

from book import Book
from bookcollection import BookCollection

FILENAME = 'books.csv'
COMPLETED_COLOR = (1, 1, 1, 0.6,)
REQUIRED_COLOR = (0, 1, 0.8, 0.7)


class ReadingTrackerApp(App):
    """..."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.books = BookCollection()

    def build(self):
        """Build the Reading Tracker 2.0 App from the app.kv file"""
        self.title = "Reading Tracker 2.0"
        self.root = Builder.load_file('app.kv')
        try:
            self.books.load_books(FILENAME)  # load books from book.csv
            self.top_label_text()
            self.bottom_label_text("Welcome to Reading Tracker 2.0")
            self.sort_book_list("author")
        except (FileNotFoundError, LookupError):
            self.top_label_text()
            self.bottom_label_text("Welcome to Reading Tracker 2.0..Unable to load books.csv")
            return self.root

        def top_label_text(self):
            """Label that shows pages to be read"""
            self.root.ids.top_label.text = "Pages to read:{}".format(self.books.get_required_pages())

        def bottom_label_text(self, bottom_label):
            """Label that display in the bottom of the GUI"""
            self.root.ids.bottom_label.text = bottom_label

        def sort_book_list(self, key='author'):
            """Sort the book list"""
            if key.lower() == 'completed':
                key = 'is_completed'
            self.books.sort(key.lower())  # sort books




if __name__ == '__main__':
    ReadingTrackerApp().run()
