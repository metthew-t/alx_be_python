class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return f"{self.title} by {self.author} ({self.year})"
    def __repr__(self)-> str:
        return f"book('{self.title}', '{self.author}', {self.year})"
    def __del__(self):
        print(f"Deleting {self.title}")
        
    

    