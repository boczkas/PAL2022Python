def dlugie(a,b,c,d,e,f):
    print(a,b,c,d,e,f,)


def przyjmujeTablice(tablica):
    for element in tablica:
        print(element)


# 1. Napisz metodę, która przyjmuje 6 argumentów i wypisuej je
# dlugie("q", "w", "e", "r", "t", "y")

# 2. To musi być leiej ogarnięte, ano jest - mamy Array
# elo = ["a", "s", "d", "f", "g", "h", "i", "j", "kaczka"]
#
# for i in elo:
#     print(i)

# przyjmujeTablice(elo)

# 3. Pokazówka
tablicaCebul = ["zwykla", "bardzoRosnie", "zwykla", "troszkeRosnie", "rosnie"]

for cebula in tablicaCebul:
    print(cebula)


# 3. Wiemy po co to teraz się z nimi pobawmy
liczby = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

suma = 0
for liczba in liczby:
    print(liczba)
    suma += liczba
print("suma =", suma)

# 4. Policz ile jest piątek w tablicy
tablica = [0, 1, 2, 5, 3, 6, 5, 5, 5]