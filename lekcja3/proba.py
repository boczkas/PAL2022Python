import math


def policzSume(a, b):
    suma = a + b
    return suma

def poleKwadratu(bok):
    return bok**2

def poleTrojkata(a, h):
    return 0.5 * a * h

def podziel(a, b):
    return a/b

def poleKola(r):
    return math.pi * r**2

def czyPaczysta(liczba):
    return liczba % 2 == 0

# 1. W Scratchu można dodawać tylko dane wejściowe. Nas może interesować też żeby te metody coś
#   zwracały.
# policzone = policzSume(5, 8)
# print(policzone)

# Napisz metodę, która policzy pole kwadratu i zwróci tą wartość. Pole kwadratu a**2
# Wypisz wartość

# print(poleKwadratu(5))
# Nie musimy tworzyć zmiennej
# print(policzSume(10, 20))

# Wywołaj swoją metodę do liczenia pola kwadratu i wypisz jej wynik bez tworzenia zmiennej na wynik

# 2. Za pomocą metody poleKwadratu() oblicz sumę pól kwadratów o bokach długości 5 i 10
# sumaPol = poleKwadratu(5) + poleKwadratu(10)
# print("sumaPol", sumaPol)

# print(poleTrojkata(5, 10))
# Przerób swoją metodę do liczenia pola trójkąta tak, aby zwracała tą wartość. Policz i wypisz sumę pól trójkątów:
# a = 1 h = 2, a = 2 h = 4, a = 5 b = 2

# print(poleTrojkata(1, 2) + poleTrojkata(2,4) + poleTrojkata(5, 2))

# (14 / 7) + (6 / 3)
# print(policzSume(podziel(14,7), podziel(6, 3)))

# print(poleKola(5))

print(czyPaczysta(6))
#
# 3. Napisz metodę suma, która zsumuje dwie liczby i zwróci wynik.
#    Napisz metodę, która podzieli przez siebie dwie liczby i zwróci wynik
# 4. Za pomocą powyższych metod przeprowadź działanie i wypisz wynik. Nie wolno używać printa poza metodami:
# (14 / 7) + (6 / 3)
# 5. Napisz metodę, która obliczy pole koła. Poszukaj jak zdobyć wartość PI - biblioteka math
# 6. Napisz metodę, która sprawdzi czy dana liczba jest parzysta czy nie parzysta
#     i zwróci tą informację