# functie care primeste nr nedefinit de parametrii
# si returneaza suma parametrilor care sunt numere
# intregi sau reale
def your_function(*args, **kwargs):
    sum = 0
    if not args:
        return 0
    for i in args:
        if isinstance(i, int) or isinstance(i, float):
            sum += i
    return sum


print("Test primul subpunct: ")
print(your_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(your_function())
print(your_function(2, 4, 'abc', param_1=2))

suma = 0
suma_nr_pare = 0
suma_nr_impare = 0


# functie recursiva care returneaza suma, suma
# numerelor impare si suma numerelor pare de la
# 0 la n
def f_recursiva(n):
    global suma, suma_nr_impare, suma_nr_pare
    if n == 0:
        suma_nr_impare = suma - suma_nr_pare
        sume = [suma, suma_nr_impare, suma_nr_pare]
        suma = 0
        suma_nr_pare = 0
        suma_nr_impare = 0
        return sume
    suma += n
    if n % 2 == 0:
        suma_nr_pare += n

    return f_recursiva(n - 1)


print("Test al doilea subpunct: ")
sume_1 = f_recursiva(5)
print(f"Suma numerelor este: {sume_1[0]}, suma numerelor pare este: {sume_1[2]}, iar suma numerelor impare este: {sume_1[1]}")
sume_2 = f_recursiva(10)
print(f"Suma numerelor este: {sume_2[0]}, suma numerelor pare este: {sume_2[2]}, iar suma numerelor impare este: {sume_2[1]}")


# functie care verifica daca numarul dat
# este intreg
def verif_int(n):
    if isinstance(n, int):
        return n
    else:
        return 0


print("Test al treilea subpunct: ")
print(verif_int(2.5))
print(verif_int(-21))
print(verif_int([1, 2, 3]))