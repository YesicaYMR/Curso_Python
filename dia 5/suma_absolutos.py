def suma_absolutos(*args):
    total = 0
    for arg in args:
        numero = abs(arg)
        total += numero

    return total


print(suma_absolutos(1, -2, 3, -4, 5))