class Book: 
    def __init__(self,title, author, pages) :
        self.title = title
        self.author = author 
        self.pages = pages

    def __str__(self) :
        return f"This Books has a title :{self.title} and the author is {self.author} and has number of pages {self.pages}"
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"
    
book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
print(book2)
print(repr(book2))