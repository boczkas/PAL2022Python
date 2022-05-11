# 1. Czytanie z klawiatury
# https://scratch.mit.edu/projects/685597894/editor/
# print("Jak masz na imie?")
# imie = input()
# print("Siema", imie, "!")
#
# dlugosc = len(imie)
# print(dlugosc)

# 2. Napisz program który zapyta najpierw jak masz na imie, potem jak masz na nazwisko.
#   Wyświetli napis, np. "Cześć Przemek Jakubowski!"
# https://scratch.mit.edu/projects/688968168/editor/


# 3. Napisz program który:
#  napisze coś takiego:
# "Podaj pierwsze słowo"
# -> Wpisujesz pierwsze słowo
# "Podaj drugie słowo"
# -> Wpisujesz drugie słowo
#
# I teraz program zgodnie z prawdą wypisuje:
# "Pierwsze słowo jest dłuższe od drugiego"
# albo
# "Drugie słowo jest dłuższe od pierwszego"
# albo
# "Słowa mają taką samą długość"
#  Przyda się:
# len(slowo)


# 4. Napisz program który zapyta użytkownika jakie dodać liczby. Na zasadzie.
#   Podaj pierwsza liczbe, podaj druga liczbe.
#   Program wypisze sume.
# https://scratch.mit.edu/projects/688971159/editor/

# 5. Napisz kalkulator.
# - program pyta o to jakie działanie wykonać.
# - program pyta o pierwszą liczbę
# - program pyta o drugą liczbę
# - program wypisuję wynik działania na zasadzie:
# 2 + 2 = 4
# - program ma się nie kończyć

# - dodatkowa funkcjonalność: jak się wpiszę "q" w ramach działania to cały program ma się zakończyć
# - dodatkowa funkcjonalność: jak się wpiszę "q" w dowolnym momencie to program kończy działanie

# Czytanie z klawiatury - łącznie z przerabianiem na int(). Zadanie napisać guessTheNumber(liczba)
# Liczba jest losowa od 0 do 100 random.randint()
# Różne metody wbudowane - random.randint()
# https://scratch.mit.edu/projects/678924474/editor/
# Kolekcje
# List, Set, Dictionary
# Policz sumę liczb w liście
# Obsługa wyjątków

# _***** ***_

zmienna = "_"

for i in range(5):
    zmienna += "*"

zmienna += " "

for i in range(3):
    zmienna += "*"

zmienna += "_"

cos = input("Elo")
print(cos)

print(zmienna)