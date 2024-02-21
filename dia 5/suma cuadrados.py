def suma_cuadrados(*args):
    total = 0
    for arg in args:
        total += arg ** 2
    return total


print(suma_cuadrados(1, 2, 3))