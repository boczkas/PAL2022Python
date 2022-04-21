import random
def suma(liczba1, liczba2):
    liczba = liczba1 + liczba2
    print(liczba)


def policzSume(liczba1, liczba2):
    suma = liczba1 + liczba2
    return suma


def poleKwadratu(a):
    return a**2


if __name__ == '__main__':
    print("Elo!")

    # 1. Metoda suma(liczba1, liczba2) - niech to zacznie nareszcie coś robić!
    # https://scratch.mit.edu/projects/678366305/editor/
    # suma(7, 5)

    # Napisz metodę poleTrojkata(a, h), która po wywołaniu wypisze na ekran wartość pola trójkąta
    # o boku a i wysokości h. Wzór na pole trójkąta 0.5 * a * h

    # 2. W Scratchu można dodawać tylko dane wejściowe. Nas może interesować też żeby te metody coś
    #   zwracały.
    # policzone = policzSume(8, 5)
    # print(policzone)

    # Napisz metodę, która policzy pole kwadratu i zwróci tą wartość. Pole kwadratu a**2
    # Wypisz wartość

    # Nie musimy tworzyć zmiennej
    # print(policzSume(10, 20))

    # Wywołaj swoją metodę do liczenia pola kwadratu i wypisz jej wynik bez tworzenia zmiennej na wynik

    # 3. Za pomocą metody poleKwadratu() oblicz sumę pól kwadratów o bokach długości 5 i 10
    # sumaPol = poleKwadratu(5) + poleKwadratu(10)
    # print("sumaPol", sumaPol)

    # Przerób swoją metodę do liczenia pola trójkąta tak, aby zwracała tą wartość. Policz i wypisz sumę pól trójkątów:
    # a = 1 h = 2, a = 2 h = 4, a = 5 b = 2

    ##########
    # Zadanie
    # 1. Napisz metodę, która podzieli przez siebie dwie liczby i zwróci wynik
    # 2. Napisz metodę, która obliczy pole koła. Poszukaj jak zdobyć wartość PI - biblioteka math
    # 3. Napisz metodę, która sprawdzi czy dana liczba jest parzysta czy nie parzysta
    #     i zwróci tą informację
    # 4. Za pomocą pierwszej metody przeprowadź działanie :
    # (14 / 7) + (6 / 3)
    # i wypisz jego wynik



    # Czytanie z klawiatury - łącznie z przerabianiem na int(). Zadanie napisać guessTheNumber(liczba)
    # Liczba jest losowa od 0 do 100 random.randint()
    # Różne metody wbudowane - random.randint()
    # https://scratch.mit.edu/projects/678924474/editor/
    # Kolekcje
    # List, Set, Dictionary
    # Policz sumę liczb w liście
    # Obsługa wyjątków