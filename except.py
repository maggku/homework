#Napisz funkcję, która dzieli dwie liczby, ale zabezpiecza się przed błędami za pomocą try/except.
#Powinna użyć try/except, aby:
#
#   złapać ZeroDivisionError (dzielenie przez 0) i zwrócić tekst "Nie można dzielić przez zero!",
#  złapać TypeError (np. gdy argumenty nie są liczbami) i zwrócić tekst "Podano nieprawidłowe dane!".

# W przypadku sukcesu zwrócić wynik dzielenia.
#
#Napisz proszę testy do tej f-cji:

#    Czy dzielenie 10, 2 daje 5
#    Obsługa dzielenia przez 0.
#    Obsługa przy podaniu nieprawidłowych danych.

#zadanie na szóstkę:
#Do testów wykorzystaj moduł "pytest". Trzeba będgit zie go zainstalować.


def division():
    while True:
        try:
            x = int(input("What's x?"))
            y = int(input("What's y?"))
            print(x / y)
            return x / y
        except ValueError:
            print("Podano nieprawidłowe dane! / Incorrect input!")
        except ZeroDivisionError:
            print("Nie można dzielić przez zero! / Division with 0 is not possible!")


division()

