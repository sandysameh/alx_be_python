class Book:
    def __init__(self,title,author,is_checked_out=False):
        self.title = title
        self.author = author
        self.__is_checked_out = is_checked_out
    
    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out= True
            # print(f"The book '{self.title}' by {self.author} has been checked out.")

    def book_return(self):
        if self.__is_checked_out:
           self.__is_checked_out = False
        #    print(f"The book '{self.title}' by {self.author} has been returned.")
        # else: 
        #     print(f"The book '{self.title}' by {self.author} is already returned.")
    
    def isBookAvailable(self):
        return not self.__is_checked_out

        
class Library:
    def __init__(self):
        self.__books = []

    def add_book(self,book:Book):
         self.__books.append(book)

    def check_out_book(self,title):
        for book in self.__books:
            if book.title == title:
                book.check_out()
                return
    
    def return_book(self,title):
        for book in self.__books:
            if book.title == title:
                book.book_return()
                return
            
    def list_available_books(self):
        for book in self.__books:
            if book.isBookAvailable():
               print(f"{book.title} by {book.author}")