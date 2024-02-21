lista_numeros = [1, 2, 15, 7, 2, 8]


def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    return lista


def promedio(lista):
    valor_medio = sum(lista) / len(lista)
    return valor_medio

lista_reducida=reducir_lista(lista_numeros)
media=promedio(lista_reducida)
print(lista_reducida)
print(media)
