def dlugie(a,b,c,d,e,f):
    print(a,b,c,d,e,f,)


def przyjmujeTablice(tablica):
    for element in tablica:
        print(element)


# 1. Napisz metodę, która przyjmuje 6 argumentów i wypisuej je
# dlugie("q", "w", "e", "r", "t", "y")
a = 1
b = 2
c = 3
tablica = [1, 2, 3]

# 2. To musi być leiej ogarnięte, ano jest - mamy Array
podstawka = ["zolty", "czarny", "niebieski", "czerwony"]

for kolor in podstawka:
    print(kolor)


truskawki = [1, 7, 2, 3, 4, 5, 6, 5, 5]

iloscPiatek = 0
for reka in truskawki:
    if reka == 5:
        iloscPiatek += 1

print("iloscPiatek", iloscPiatek)
#
# liczby = [1, 1, 2, 2, 3, 4, 5, 6]
#
# suma = 0
# for reka in truskawki:
#     print("truskawka = ", reka)
#     suma += reka
#     print("suma = ", suma)
#
# elo = ["a", "s", "d", "f", "g", "h", "i", "j", "kaczka"]
#
# a = 1
# b = 2
# c = 3
# liczby = [1, 2, 3]
#
# for i in elo:
#     print(i)

# przyjmujeTablice(elo)

# 3. Pokazówka
# tablicaCebul = ["zwykla", "bardzoRosnie", "zwykla", "troszkeRosnie", "rosnie"]
#
# for cebula in tablicaCebul:
#     print(cebula)


# 3. Wiemy po co to teraz się z nimi pobawmy
# liczby = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# suma = 0
# for liczba in liczby:
#     print(liczba)
#     suma += liczba
# print("suma =", suma)

# 4. Policz ile jest piątek w tablicy
# tablica = [0, 1, 2, 5, 3, 6, 5, 5, 5]

# 5. Stwórz na podstawie powyższej tablicy nową tablicę wyłącznie z liczbami nieparzystymi
nowaTablica = []
print(nowaTablica)
nowaTablica.append(5)
nowaTablica.append(3)
nowaTablica.append(2)
nowaTablica.append(1)
print(nowaTablica)
#
# for liczba in nowaTablica:
#     print(liczba)
#
# print(nowaTablica)
# liczba = 3
#
# if liczba % 2 != 0:
#     print("NieParzysta")
# 6. Stwórz tablicę bez duplikatów

