class Book:
    def __init__(self,title,author):
        if not title or not isinstance(title,str):
            raise ValueError("Title must be a non-empty string")
        if not author or not isinstance(author,str):
            raise ValueError("Author must be a non empty string")
        
        self.title =title
        self.author =author
    
    def display_info(self):
        print(f"Title:{self.title},Author:{self.author}")

book = Book("To Kill a Mockingbird","Harper Lee")
book.display_info()