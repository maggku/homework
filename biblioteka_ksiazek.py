"""
Stwórz program "Biblioteka książek".
Klasa Ksiazka
Powinna mieć:
atrybuty:
tytul (str)
autor (str)
rok_wydania (int)

metodę str(), która ładnie wypisze informacje o książce, np.
"Harry Potter (J.K. Rowling, 1997)"

Klasa Biblioteka
Powinna mieć:
atrybut ksiazki – listę obiektów klasy Ksiazka,

metody:

dodaj_ksiazke(ksiazka) – dodaje książkę do listy,
usun_ksiazke(tytul) – usuwa książkę o podanym tytule (jeśli istnieje),
wyszukaj_po_autorze(autor) – zwraca listę książek danego autora,
wyswietl_wszystkie() – wypisuje wszystkie książki w bibliotece.

"""

class Book():
    def __init__(self, title, author, publishing_year):
        self.title = title
        self.author = author
        self.publishing_year = publishing_year


    def __str__(self):
        return f"{self.title} ({self.author}, {self.publishing_year})"



class Library():
    def __init__(self, books=None):
        if books == None:
            self.books = []
        else:
            self.books = books

    def add_book(self, book):
        self.books.append(book)



    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                return

    def author_search(self, author):
        found = []
        for book in self.books:
            if book.author == author:
                found.append(book)

        if found:
            return found
        else:
            print("There are no books by this author.")
            return []



    def wyswietl_wszystkie(self):
        for ksiazka in self.ksiazki:
            print(ksiazka)



