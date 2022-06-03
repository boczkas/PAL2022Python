# 1. Dictionary - przechowuje wartości na zasadzie klucz -> wartość
slownik = {"imie": "name",
           "dom": "house"}

print(slownik)

# 2. Stórz słownik z tłumaczeniami "pies" -> "dog", "kot" -> "cat"


# 3. Wyciąganie po kluczu
get = slownik.get("imie")
print(get)

# 4. Wyciągnij ze swojego słownika wartość dla klucza "pies"


# 5. Zmiana wartości w słowniku
slownik["imie"] = "Der Name"
print(slownik)

# 6. Zaktualizuj w swoim słowniku wartość dla klucza "pies" na "Hund"

# 7. Dodamy nowy element do słownika
slownik["kamien"] = "stone"
print(slownik)

# 8. Dodaj do swojego słownika nowe mapowanie "slonce" -> "sun"

# 9. Usuwanie elementow ze slownika
slownik.pop("kamien")
print(slownik)

# 10. Usuń ze swojego słownika ostatnio dodane mapowanie

# 11. Iterowanie po slowniku

for x in slownik:
    print("x = ", x)


for x in slownik:
    print("slownik.get(x) =", slownik.get(x))

# 12. Przeiteruj sie przez swoj slownik