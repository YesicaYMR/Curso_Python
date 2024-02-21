from random import choice

def lanzar_moneda():
    lados = ['cara', 'cruz']
    lado = choice(lados)
    return lado


def probar_suerte(lista, lado):
    if lado == 'cara':
        print('La lista se autodestruirá')
        lista.clear()
        return lista

    else:
        print('La lista fue salvada')
        return lista


lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado = lanzar_moneda()
probar_suerte(lista_numeros, resultado)
print(lista_numeros)
