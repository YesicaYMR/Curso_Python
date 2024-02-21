def devolver_distintos(num1, num2, num3):
    lista = [num1, num2, num3]

    lista.sort()

    if sum(lista) > 15:
        return lista[2]
        #return max(lista)
    elif sum(lista) < 10:
        return lista[0]
    else:
        return lista[1]
        #return min(lista)


print(devolver_distintos(5, 12, 2))
