def powiedz():
    print("Cześć!")


def wypiszLiczbe(liczba):
    print(liczba)


def suma(liczba1, liczba2):
    print(liczba1 + liczba2)


def policzSume(liczba1, liczba2):
    suma = liczba1 + liczba2
    return suma


if __name__ == '__main__':
    # 1. Reszta z dzielenia
    # https://scratch.mit.edu/projects/678361093/editor/
    # W taki sposób możemy powiedzieć czy liczba jest parzysta czy nie

    # liczba = 9
    # if liczba % 2 == 0:
    #     print("Liczba jest parzysta")
    # else:
    #     print("Liczba jest nieparzysta")
    #
    # 4. for
    # https://scratch.mit.edu/projects/675687157/editor/
    # for liczba in range(5):
    #     print(liczba)


    # 5. Napisz program wykorzystujący pętlę for do przejścia przez liczby od 0 do 9 i sprawdzający za każdym razem
    # czy liczba jest parzysta czy nie
    # https://scratch.mit.edu/projects/675688629/editor/

    # ==============================================================
    # 6. while z warunkiem
    # liczba = 0
    # while liczba < 10:
    #     print(liczba)
    #     liczba += 1
    #
    # Napisz program, który będzie wykonywał pętle while dopóki liczba będzie mniejsza niż 100,
    # a liczbe będzie większał o 10 za każdym obiegiem pętli. Początkowa wartość liczby to 0

    # 7. Metoda powiedz
    # https://scratch.mit.edu/projects/678363876/editor/
    # powiedz()

    # Napisz metodę siema(), która po wywołaniu wypisze na ekran "Siema!"

    # 8. Metoda wypisz liczbe
    # https://scratch.mit.edu/projects/678365172/editor/
    zmienna = 100
    wypiszLiczbe(zmienna)

    # Można bez zmiennej
    wypiszLiczbe(7)

    # Napisz metodę wypiszTekst(tekst), która po wywołaniu wypiszę na ekran zawartość zmiennej tekst

    # 9. Metoda suma(liczba1, liczba2) - niech to zacznie nareszcie coś robić!
    # https://scratch.mit.edu/projects/678366305/editor/
    suma(3, 5)

    # Napisz metodę poleTrojkata(a, h), która po wywołaniu wypisze na ekran wartość pola trójkąta
    # o boku a i wysokości h. Wzór na pole trójkąta 0.5 * a * h

    # 10. W Scratchu można dodawać tylko dane wejściowe. Nas może interesować też żeby te metody coś
    #   zwracały.
    policzone = policzSume(7, 5)
    print(policzone)

    # Napisz metodę, która policzy pole kwadratu i zwróci tą wartość. Pole kwadratu a**2
    # Wypisz wartość

    # Nie musimy tworzyć zmiennej
    print(policzSume(10, 20))

    # Wywołaj swoją metodę do liczenia pola kwadratu i wypisz jej wynik bez tworzenia zmiennej na wynik


    ##########
    # Zadanie
    # 1. Napisz metodę, która podzieli przez siebie dwie liczby i zwróci wynik
    # 2. Napisz metodę, która obliczy pole koła. Poszukaj jak zdobyć wartość PI - biblioteka math
    # 3. Napisz metodę, która sprawdzi czy dana liczba jest parzysta czy nie parzysta
    #     i zwróci tą informację
    