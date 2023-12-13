def your_function(*args, **kwargs):
    if not args:
        return 0
    suma = 0
    for element in args:
        try:
            int(element)
            is_dig = True
        except ValueError:
            is_dig = False
        except TypeError:
            is_dig = False
        finally:
            if is_dig:
                suma += int(element)
    return suma


print(your_function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(your_function())
print(your_function(2, 4, 'abc', param_1=2))


suma = 0
suma_nr_pare = 0
suma_nr_impare = 0


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


sume_1 = f_recursiva(5)
print(f"Suma numerelor este: {sume_1[0]}, suma numerelor pare este: {sume_1[2]}, iar suma numerelor impare este: {sume_1[1]}")
sume_2 = f_recursiva(10)
print(f"Suma numerelor este: {sume_2[0]}, suma numerelor pare este: {sume_2[2]}, iar suma numerelor impare este: {sume_2[1]}")


def verif_int(n):
    try:
        if isinstance(n, str):
            return 0
    except ValueError:
        return 0
    except AttributeError:
        return 0
    finally:
        if isinstance(n, float):
            return 0
        else:
            return n


print(verif_int('2.5'))