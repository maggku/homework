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

class Ksiazka():
    def __init__(self, tytul, autor, rok_wydania):
        self.tytul = tytul
        self.autor = autor
        self.rok_wydania = rok_wydania


    def __str__(self):
        return f"{self.tytul} ({self.autor}, {self.rok_wydania})"



class Biblioteka():
    def __init__(self, ksiazki=None):
        if ksiazki == None:
            self.ksiazki = []
        else:
            self.ksiazki = ksiazki

    def dodaj_ksiazke(self, ksiazka):
        self.ksiazki.append(ksiazka)



    def usun_ksiazke(self, tytul):
        for ksiazka in self.ksiazki:
            if ksiazka.tytul == tytul:
                self.ksiazki.remove(ksiazka)
                return

    def wyszukaj_po_autorze(self, autor):
        wybrane = []
        for ksiazka in self.ksiazki:
            if ksiazka.autor == autor:
                wybrane.append(ksiazka)

        if wybrane:
            return wybrane
        else:
            print("Nie ma ksiazek tego autora")
            return []



    def wyswietl_wszystkie(self):
        for ksiazka in self.ksiazki:
            print(ksiazka)



