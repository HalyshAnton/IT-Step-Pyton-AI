import bintrees


class Book:
    def __init__(self, title, author, year):
       self.title = title
       self.author = author
       self.year = year

    def __str__(self):
        return f'"{self.title}" by {self.author}, {self.year}'


class Library:
    def __init__(self):
        self.tree = bintrees.AVLTree()

    def insert(self, title, author, year):
        book = Book(title, author, year)
        self.tree.insert(key=title, value=book)

    def search(self, title):
        if title in self.tree:
            return self.tree[title]
        else:
            print('Немає книги у бібліотеці')

    def delete(self, title):
        if title in self.tree:
            self.tree.remove(title)
        else:
            print('Немає книги у бібліотеці')

    def display(self):
        for book in self.tree.values():
            print(book)

    def count(self):
        return len(self.tree)


library = Library()

library.insert("1984", "George Orwell", 1949)
library.insert("To Kill a Mockingbird", "Harper Lee", 1960)
library.insert("Pride and Prejudice", "Jane Austen", 1813)

print("Books in library:")
library.display()

print("\nSearching for '1984':")
book = library.search("1984")
print(book)

library.delete("To Kill a Mockingbird")
print("\nBooks in library after deletion:")
library.display()

print("\nTotal number of books:", library.count())
