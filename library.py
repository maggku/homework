"""

Klasa bazowa Publikacja

Stwórz klasę Publikacja, która będzie ogólnym typem dla różnych rodzajów materiałów (książek, magazynów, audiobooków itp.).

Atrybuty:

    tytul (str)
    autor (str)
    rok_wydania (int)
    dostepna (bool) – domyślnie True

Metody:

    __init__ – konstruktor ustawiający powyższe atrybuty,
    __str__ – zwraca czytelny opis np. "Publikacja: 'Wiedźmin' (Andrzej Sapkowski, 1993)",
    wypozycz() – ustawia dostepna = False i zwraca komunikat,
    zwróć() – ustawia dostepna = True.

Dziedziczenie: klasy potomne

Utwórz klasy, które dziedziczą po Publikacja:
Klasa Ksiazka

Dodatkowe atrybuty:

    liczba_stron (int)

Nadpisz:

    __str__ – dodaj informację o liczbie stron.
    Dla wypozycz() dodaj dodatkowy komunikat np. „Miłej lektury!”.

Klasa Magazyn

Dodatkowe atrybuty:

    numer_wydania (int)

Nadpisz:

    __str__ – dodaj numer wydania,
    wypozycz() – ma zwracać komunikat „Magazyny nie podlegają wypożyczeniu.”

Klasa Audiobook

Dodatkowe atrybuty:

    dlugosc_minut (int)

Dodatkowa metoda:

    @property czas_godziny – zwraca długość w godzinach (dlugosc_minut / 60, zaokrąglona do 2 miejsc).

Klasa Biblioteka

Klasa, która zarządza kolekcją publikacji.

Atrybuty:

    nazwa (str)
    publikacje (lista obiektów klasy Publikacja)
    liczba_bibliotek (atrybut klasowy, zwiększany przy każdym nowym obiekcie)

Metody:

    __init__ – inicjalizuje nazwę i pustą listę publikacji,
    __len__ – zwraca liczbę publikacji,
    __str__ – np. "Biblioteka 'Centralna' (3 publikacje)",
    dodaj_publikacje(publikacja) – dodaje obiekt do listy,
    usun_publikacje(tytul) – usuwa po tytule (jeśli istnieje),
    wyszukaj_autora(autor) – zwraca listę publikacji autora,
    @classmethod utworz_pusta(cls, nazwa) – alternatywny konstruktor do publikacji
    @staticmethod powitaj() – zwraca komunikat powitalny dla użytkownika.

"""

class Publication:
    def __init__(self, title, author, publishing_year, available = True):
        self.title = title
        self.author = author
        self.publishing_year = publishing_year
        self.available = available


    def __str__(self):
        return f"Publication: {self.title} ({self.author}, {self.publishing_year})"


    def lend_out(self):
        self.available = False
        return f"You have three weeks to read {self.title}. Enjoy! "


    def returned(self):
        self.available = True


class Book(Publication):
    def __init__(self, title, author, publishing_year, page_count, available = True):
        super().__init__(title, author, publishing_year, available)
        self.page_count = page_count


    def __str__(self):
        return f"{self.title} has {self.page_count} pages."


    def lend_out(self):
        main_message = super().lend_out()
        extra_message = f"Please return it in the timely manner."
        return f"{main_message}{extra_message}"



class Magazine(Publication):
    def __init__(self, title, author, publishing_year, issue_number, available = True):
        super().__init__(title, author, publishing_year, available)
        self.issue_number = issue_number


    def __str__(self):
        main_info = super().__str__()
        extra_info = f", issue number: {self.issue_number}"
        return f"{main_info}{extra_info}"


    def lend_out(self):
        return f"Magazines cannot be borrowed, but you're welcome to read it here. We're open 9am-6pm daily."

my_magazine = Magazine("National Geographic", "Various", 2024, 152)
print(my_magazine)
print(my_magazine.lend_out())

class Audiobook(Publication):
    def __init__(self, title, author, publishing_year, length_minutes, available):
        super().__init__(title, author, publishing_year, available)
        self.length_minutes = length_minutes


@property
def length_hours(self):
    return round(self.length_minutes / 60, 2)


class Library:
    no_of_libraries = 0

    def __init__(self, name):
        self.name = name
        self.list_of_publications = []
        Library.no_of_libraries += 1


    def __len__(self):
        return len(self.list_of_publications)


    def __str__(self):
        return f"{self.name} Library ({len(self.list_of_publications)})"


    def add_publication(self, publication):
        self.list_of_publications.append(publication)

    def remove_publication(self, title):
        new_list = []
        for publication in self.list_of_publications:
            if publication.title != title:
                new_list.append(publication)
        self.list_of_publications = new_list

    def author_search(self, author):
        selected = []
        for a in self.list_of_publications:
            if a.author == author:
                selected.append(a)
        print(selected)


@staticmethod
def greeting():
    print(f"Welcome to our Library!")


mybook = Book("1984", "George Orwell", "1984", "444")
print(mybook)
print(mybook.publishing_year)
print(mybook.lend_out())


