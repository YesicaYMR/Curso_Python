def contar_primos(numero):
    lista = range(0, numero + 1)
    contador_primos = 0
    for numero in lista:
        divisor = 1
        divisores = 0
        while divisor < numero:
            if numero % divisor == 0:
                divisores += 1
                divisor += 1
            else:
                divisor += 1
        if divisores == 1:
            print(numero)
            contador_primos += 1
    return contador_primos



print(contar_primos(5))
