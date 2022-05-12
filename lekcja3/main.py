import math
import random
def suma(liczba1, liczba2):
    liczba = liczba1 + liczba2
    print(liczba)


def policzSume(liczba1, liczba2):
    suma = liczba1 + liczba2
    return suma


def poleKwadratu(a):
    return a**2


def drukujPole(a):
    print(a**2)


def powiedz():
    print("Czesc")

def krzykacz():
    print("Aaaaaaaaaaaaaaaa")

def sumaZmiennychLokalnych():
    liczba1 = 10
    liczba2 = 20
    print(liczba1 + liczba2)

def powiedzLiczbyOd0DoN_1(n):
    for liczba in range(n):
        print(liczba)


def poleTrojkata(a,h):
    return 0.5 * a * h


# print(poleTrojkata(2, 5) + poleTrojkata(4, 10))

# Przerabiamy do Pythona
# 1. https://scratch.mit.edu/projects/681784124/editor/
# 2. https://scratch.mit.edu/projects/681784964/editor/
# 3. https://scratch.mit.edu/projects/681785553/editor/
# 4. https://scratch.mit.edu/projects/681804535/editor/
#  Ma krzyczeć "Aaaaa" a potem "pies+100"
# 5. https://scratch.mit.edu/projects/681806599/editor/
# 6. https://scratch.mit.edu/projects/681786757/editor/

# TO JESZCZE DO SALI
# 7. https://scratch.mit.edu/projects/681792391/editor/
# 8. https://scratch.mit.edu/projects/681797853/editor/
# 9. https://scratch.mit.edu/projects/681811993/editor/

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

#
# 4. Napisz metodę suma, która zsumuje dwie liczby i zwróci wynik.
#    Napisz metodę, która podzieli przez siebie dwie liczby i zwróci wynik
# 5. Za pomocą powyższych metod przeprowadź działanie i wypisz wynik. Nie wolno używać printa poza metodami:
# (14 / 7) + (6 / 3)
# 6. Napisz metodę, która obliczy pole koła. Poszukaj jak zdobyć wartość PI - biblioteka math
# 7. Napisz metodę, która sprawdzi czy dana liczba jest parzysta czy nie parzysta
#     i zwróci tą informację
#
# 8. Należy przerobić ten program Scratchowy do Pythona:
# https://scratch.mit.edu/projects/678920938/editor/


# drukujPole(5)
#
# bok = 10
# drukujPole(bok)
# powiedz()

# krzykacz()

# sumaLiczb = policzSume(1, 2)
# print(sumaLiczb)

# kapelusz = poleTrojkata(5, 10)
# print(kapelusz)