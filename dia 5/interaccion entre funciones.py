from random import shuffle

# lista inicial
palitos = ['-', '---', '--', '----']


# mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista


# pedir intento
def probar_suerte():
    intento = ''

    while intento not in ['1', '2', '3', '4']:
        intento = input("Elige un numero del 1 al 4: ")

    return int(intento)


# comprobar intento
def comprobar_intento(lista, intento):
    if lista[intento - 1] == '-':
        print('A fregar!!')

    else:
        print('Te salvaste')

    print(f'Te ha tocado {lista[intento - 1]}')


palitos_mezclado = mezclar(palitos)
seleccion = probar_suerte()
comprobar_intento(palitos_mezclado, seleccion)
