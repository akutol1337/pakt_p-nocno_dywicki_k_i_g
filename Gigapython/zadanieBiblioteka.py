class Library:
    def __init__(self):
        self.collection = []

    @property
    def number_of_books(self):
        return len(self.collection)

    def add_book(self, book):
        self.collection += book
        
    def borrow_book(self, book):
        i = 0
        for each in self.collection:
            if each == book:
                self.collection.pop(i)
            i += 1
        
    def show_books(self):
        for each in self.collection:
            print(each)
        print('')

    def show_number_of_books(self):
        print('In the library there are: ' + str(self.number_of_books) + ' books\n')
def nl():
    print("")
library = Library()
library.add_book(['book1', 'book2', 'book3', 'book4'])
library.show_books()
library.show_number_of_books()
library.borrow_book('book2')
library.show_books()
library.show_number_of_books()
library.add_book(['book5'])
library.borrow_book('book4')
library.add_book(['book6', 'book7'])
library.borrow_book('book1')
library.borrow_book('book2')
library.borrow_book('book3')
library.borrow_book('book5')
library.show_books()
library.show_number_of_books()