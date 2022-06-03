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
# print("Jak masz na imie?")
# imie = input()
# print("Jak masz na nazwisko?")
# nazwisko = input()
#
# print("Siema", imie, nazwisko, "!")

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

# pierwsze = input("Jakie pierwsze słowo?")
# drugie = input("Jakie drugie słowo?")
#
# dlugoscPierwsze = len(pierwsze)
# dlugoscDrugie = len(drugie)
#
# if dlugoscPierwsze > dlugoscDrugie:
#     print("Pierwsze slowo jest dluzsze")
# elif dlugoscDrugie > dlugoscPierwsze:
#     print("Drugie slowo jest dluzsze")
# else:
#     print("Slowa sa rowne")
# 4. Napisz program który zapyta użytkownika jakie dodać liczby. Na zasadzie.
#   Podaj pierwsza liczbe, podaj druga liczbe.
#   Program wypisze sume.
# https://scratch.mit.edu/projects/688971159/editor/

# pierwszaLiczba = input("Jaka pierwsza liczba?")
# drugaLiczba = input("Jaka druga liczba?")
#
# suma = int(pierwszaLiczba) + int(drugaLiczba)
# print("Suma = ", suma)

# liczba1 = input("Jaka liczba1?")
# liczbaJakoLiczba = int(liczba1)
# liczba2 = input("Jaka druga liczba?")
# liczbaJakoLiczba2 = int(liczba2)
#
# print(liczba1 + liczba2)

# 5. Słowo kluczowe break

# for liczba in range(5):
#     if liczba == 3:
#         break
#     print(liczba)


# 6. Słowo kluczowe continue
for liczba in range(5):
    if liczba == 3:
        continue
    print(liczba)
#
# text = "*"

# print(5 * text)

# 7. Napisz kalkulator.
# - program pyta o to jakie działanie wykonać.
# - program pyta o pierwszą liczbę
# - program pyta o drugą liczbę
# - program wypisuję wynik działania na zasadzie:
# 2 + 2 = 4

# - program ma się nie kończyć

# - dodatkowa funkcjonalność: jak się wpiszę "q" w ramach działania to cały program ma się zakończyć
# - dodatkowa funkcjonalność: jak się wpiszę "q" w dowolnym momencie to program kończy działanie


# _***** ***_

# zmienna = "_"
#
# for i in range(5):
#     zmienna += "*"
#
# zmienna += " "
#
# for i in range(3):
#     zmienna += "*"
#
# zmienna += "_"
#
# cos = input("Elo")
# print(cos)
#
# print(zmienna)