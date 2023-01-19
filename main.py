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

class BookButton(Button):
    def init(self, book, **kwargs):
        super().init(**kwargs)
        self.book = book

    def on_click(self, book):
        """
            Click mark completed or required by changing the background color and display the top and bottom labels
        """
        if book.is_completed:
            book.mark_required()  # mark the click book as required
            if  book.is_long():
                bottom_label = "You need to read {}. Get Started!".format(str(book.title).strip())
            else:

                bottom_label = "You need to read {}.".format(str(book.title).strip())
        else:
            book.mark_completed()  # mark the clicked book as completed
            if book.is_long():
                bottom_label = "You completed {}. Great Job!".format(str(book.title).strip())
            else:
                bottom_label = "You completed {}.".format(str(book.title).strip())

        self.display_top_label()
        self.display_bottom_label(bottom_label)


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

        def display_top_label(self):
            """Label that shows pages to be read"""
            self.root.ids.top_label.text = "Pages to read:{}".format(self.books.get_required_pages())

        def display_bottom_label(self, bottom_label):
            """Label that display in the bottom of the GUI"""
            self.root.ids.bottom_label.text = bottom_label

        def sort_book_list(self, key='author'):
            """Sort the book list"""
            if key.lower() == 'completed':
                key = 'is_completed'
            self.books.sort(key.lower())  # sort books
            self.root.ids.book_list.clear_widgets()  # clear widgets
            book_list = []


            def change_state(button):
                for selected_book in book_list:  # matching the button.text and clicked book
                    if selected_book.title in button.text:
                        BookButton.on_click(self, selected_book)
                        if book.is_completed:
                            self.state = 'normal'  # change button state
                            button.background_color = COMPLETED_COLOR  # change background color
                        else:
                            self.state = 'down'  # change button state
                            button.background_color = REQUIRED_COLOR  # change background color
                        button.text = str(selected_book)  # change text on button
                        self.sort_book_list(key)  # sort the books again for dynamic sorting

            for book in self.books:
                # convert book into a list for sorting
                book_list.append(book)
                # initialize the books' states
                if book.is_completed:
                    self.state = 'normal'
                else:
                    self. state = 'down'
                # add the books
                self.root.ids.book_list.add_widget(BookButton(book=book, text=str(book), on_press=change_state,
                                                              background_color=
                                                              {'normal': COMPLETED_COLOR, 'down': REQUIRED_COLOR}[
                                                                  self.state]
                                                              ))
        def add_new_book(self ,input_title,input_author,input_pages):
            """Handle Add New Book"""
            title,author,pages=map(str.strip,(input_title.text,input_author.text,input_pages))

            #check if all fields are filled
            if not title or not author or not pages:
                self.display_bottom_label("All fields must be completed")
                return
            #check if the input pages are valid
            try:
                pages=int(pages)
            except ValueError:
                self.display_bottom_label("Please enter a valid number")
                return
            #check if the input page is greater than 0
            if pages<1:
                self.display_bottom_label("Pages must be >0")
                return

            self.sort_book_list()
            title=title +" "
            self.books.add_book(Book(title,author,pages))
            self.top_label_text()
            self.display_bottom_label(f"{title} by {author},({pages}pages)added to Reading Tracker")
            self.sort_book_list(self.root.ids.sorter.text)
            self.clear_input_fields(input_title, input_author, input_pages)
        @staticmethod
        def clear_input_fields(title,author,pages):
            """Clear the user inputs fields of title,author and pages"""
            title.text=''
            author.text=''
            pages.text=''


if __name__ == '__main__':
