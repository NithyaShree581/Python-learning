"""Topic: OOP: Classes, __init__, Inheritance & Polymorphism 
Build a class hierarchy for a library system: 
(a) Base class LibraryItem: title, author, year, describe() method. 
(b) Subclass Book: add pages and genre, override describe(). 
(c) Subclass Magazine: add issue_number and is_monthly, override describe(). 
(d) Create a list with one Book and one Magazine, loop and call describe() -- demonstrate polymorphism. 
(e) Predict the output: class Animal:     def __init__(self, name): self.name = name     def speak(self): return f'{self.name} speaks' class Dog(Animal):     def speak(self): return f'{self.name} says Woof!' for a in [Animal('Cat'), Dog('Rex')]:     print(a.speak()) 
"""
class LibrarySystem:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def describe(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"
class Book(LibrarySystem):
    def __init__(self, title, author, year, pages, genre):
        super().__init__(title, author, year)
        self.pages = pages
        self.genre = genre
    def describe(self):
        return f"Book: {self.title}, Author: {self.author}, Pages: {self.pages}, Genre: {self.genre}"
class Magazine(LibrarySystem):
    def __init__(self, title, author, year, issue_number, is_monthly):
        super().__init__(title, author, year)
        self.issue_number = issue_number
        self.is_monthly = is_monthly
    def describe(self):
        return f"Magazine: {self.title}, Issue: {self.issue_number}, Monthly: {self.is_monthly}"
book = Book("Python Basics", "John", 2025, 300, "Programming")

magazine = Magazine("Tech Today", "Jane", 2026, 25, True)
items = [book, magazine]

for item in items:
    print(item.describe())
