class Book:
    total_books =0

    def __init__(self,name) :
        self.name = name
        Book.total_books+=1
    
    @classmethod
    def  display_total_books(cls):
        return Book.total_books
    

book1 = Book("new book")
book2= Book("new book2")

print(Book.display_total_books())