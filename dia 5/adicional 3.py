def dos_ceros(*args):
    codigo = str(args)
    print(codigo)
    resultado = '0, 0' in codigo
    return resultado


print(dos_ceros(1, 5, 0, 0, 7, 8))


def ceros_vecinos(*args):
    contador = 0

    for n in args:

        if contador + 1 ==len(args):
            return False
        elif args[contador] == 0 and args[contador + +1] == 0:
            return True
        else:
            contador +=1
    return False

print(ceros_vecinos(1, 5, 0, 0, 7, 8))