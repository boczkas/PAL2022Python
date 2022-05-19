# 1. Chce przerobic na liczba, a wpisuje szyszka
# tekst = input("Jaka liczba?")
# liczba = int(tekst)
# print(liczba)
# Obsługa wyjątków

# 2. Wyjatek

# tekst = input("Jaka liczba?")
# try:
#     liczba = int(tekst)
#     print(liczba)
# except:
#     print("To nie liczba")

# 3. Napisz program, który będzie wczytywał liczbę i ją wypisywał.
#   Jeżeli użytkownik poda niewłaściwą wartość program go o tym poinformuje i ponownie
#   poprosi o wpisanie liczby.
#   Program ma działać w nieskończoność.
#   Jeżeli użytkownik wpisze "q" program ma się zakończyć.

# while True:
#     tekst = input("Jaka liczba?")
#     if tekst == "q":
#         print("Koncze!")
#         break
#     try:
#         liczba = int(tekst)
#         print("Liczba to:", liczba)
#     except:
#         print(tekst, " - to nie liczba")

# 4. Przerób swój kalkulator tak, aby obsługiwał błędnie wpisane liczby czy działanie
#   Jeśli nie masz kalkulatora to rób kalkulator :)
#
# dzialanie = input("Jakie dzialanie?") # +
#
# prawidlowe = False
#
# if dzialanie == "+":
#     prawidlowe = True
# if dzialanie == "-":
#     prawidlowe = True
# if dzialanie == "*":
#     prawidlowe = True
# if dzialanie == "/":
#     prawidlowe = True
#
# if dzialanie == "+" or dzialanie =="-" or dzialanie == "*" or dzialanie == "/":
#     prawidlowe = True
#
# print("Czy to prawidłowe?", prawidlowe)
#
while True:
    # dzialanie = input("Jakie działanie?")

    # tekst = input("Jaka pierwsza liczba?")
    #
    # try:
    #     liczba1 = int(tekst)
    #     print(liczba1, "- to liczba")
    # except:
    #     print(tekst, "- to nie liczba")
    #     continue
    #
    # tekst = input("Jaka druga liczba?")
    #
    # try:
    #     liczba2 = int(tekst)
    #     print(liczba2, "- to liczba")
    # except:
    #     print(tekst, "- to nie liczba")
    #     continue
    #
    # print(liczba1 + liczba2)
    #
    # print("Dom")
    # print("Krzak")


    dzialanie = input("Jakie dzialanie?")

    prawidlowe = False
    if dzialanie == "+" or dzialanie == "-" or dzialanie == "*" or dzialanie == "/":
        prawidlowe = True

    if prawidlowe == True:
        print("Prawidłowe działanie")
    else:
        print("Nieprawidłowe działanie")
        continue




    #
    # if dzialanie == "+":
    #     print(liczba1 + liczba2)
    # if dzialanie == "-":
    #     print(liczba1 - liczba2)
    # if dzialanie == "u":
    #     continue
# 5. GuessTheNumber
# Liczba jest losowa od 0 do 100 random.randint()
# Różne metody wbudowane - random.randint()
# https://scratch.mit.edu/projects/678924474/editor/
# Kolekcje
# List, Set, Dictionary
# Policz sumę liczb w liście
