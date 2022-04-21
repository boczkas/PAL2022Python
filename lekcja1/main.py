import math
import time


def start():
    # 1. Zawsze

    # print("Costam")
    # https://scratch.mit.edu/projects/675675913/editor/
    # while True:
    #     print("Cześć")
    #     time.sleep(1)
    # Napisz program, który wypisuje "Siema!" co 2s

    # 2. Jeżeli

    # https://scratch.mit.edu/projects/675677711/editor/
    # liczba = 5
    # if liczba > 4:
    #     print("Liczba większa niż 4")

    # Napisz program, który sprawdza czy liczba jest mniejsza niż 3

    # 3. Jeżeli/w przeciwnym razie
    # https://scratch.mit.edu/projects/675679820/editor/
    # liczba = 6
    # if liczba > 4:
    #     print("Liczba większa niż 4")
    # else:
    #     print("Liczba mniejsza bądź równa 4")

    # Napisz program, który sprawdza czy liczba jest jest większa niż 10.
    # Jeśli tak, wypisuje "Liczba większa niż 10",  w przeciwnym razie wypisuje "Liczba mniejsza niż 10"

    # print("0 == 1", 0 == 1)
    # liczba = 1
    # if liczba == 0:
    #     print("Liczba jest równa 0")
    #
    # if liczba != 0:
    #     print("Liczba jest różna od 0")

    # 4. Operacje arytmetyczne
    a = 4
    b = 2
    c = a + b
    print("a + b = ", c)

    c = a - b
    print("a - b = ", c)

    c = a * b
    print("a * b = ", c)

    c = a / b
    print("a / b = ", c)

    c = a**2
    print("a**2 = ", c)

    # pierwastek = math.sqrt(4)
    # print(pierwastek)

    # "Nigdy mi się nie przyda rozwiązywanie równań kwadratowych!"
    # 7. Napisz program rozwiązujący równanie kwadratowe (o ile istnieje)

    # https://www.matemaks.pl/rownania-kwadratowe-w-postaci-ogolnej.html

    a = 1
    b = 2
    c = -3

    pierwiastek = math.sqrt(4)
    print(pierwiastek)
    # delta = b^2 - 4ac
    delta = b**2 - 4 * a * c
    # print(delta)
    #
    if (delta < 0):
        print("Rownanie kwadratowe nie ma rozwiazania")
    elif(delta > 0):
        math.sqrt(delta)
        print("To macie napisać")
        # x1 = (-b - math.sqrt(delta)) / (2 * a)
        # x2 = (-b + math.sqrt(delta)) / (2 * a)
        # print("Rozwiązania to: ", x1, x2)
    else:
        x = -b / 2*a
        print("x", x)

if __name__ == '__main__':
    start()
