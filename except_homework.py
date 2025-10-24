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

# With input
def division1():
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


if __name__ == "__main__":
    division1()


# With parameters and tests
def division2(x, y):
        try:
            print(x / y)
            return x / y
        except (ValueError, TypeError):
            print("Podano nieprawidłowe dane! / Incorrect input!")
            return None
        except ZeroDivisionError:
            print("Nie można dzielić przez zero! / Division with 0 is not possible!")
            return None

def test_division2():
    assert division2(10,2) == 5
    assert division2(10, 0) == None
    assert division2(10, "dog") == None


test_division2()
print("All tests passed")