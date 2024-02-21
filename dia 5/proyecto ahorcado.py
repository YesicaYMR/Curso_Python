from random import choice

letras_incorrectas = []


def eleccion_palabras(*args):
    lista = list(args)
    palabra = choice(lista)
    return palabra


def num_letras(palabra):
    num_letras = len(palabra)
    codigo = '-' * num_letras
    print(str(codigo))
    return list(codigo)


def pedir_letra():
    letra = input("introduce una letra: ")
    while len(letra) != 1 or letra.isalpha() == False:
        letra = input("introduce una letra: ")
    return letra


def buscar_letra(num_vidas, letra_elegida, palabra_elegida, codigo_actualizado):
    if letra_elegida not in palabra_elegida:
        num_vidas -= 1
        print('Error')
        print(f'Te quedan {num_vidas} vidas')

        if num_vidas == 0:
            print('game over')
            exit()

    else:
        for pos, leter in enumerate(palabra_elegida):
            if leter == letra_elegida:
                codigo_actualizado[pos] = letra_elegida

    print(str(codigo_actualizado))
    return num_vidas


vidas = 6
elegida = eleccion_palabras('agua', 'lista', 'parrilla', 'mastil', 'mesa')
codigo = (num_letras(elegida))
while '-' in codigo:
    letra = pedir_letra()
    vidas=buscar_letra(vidas, letra, elegida, codigo)
print(f'¡Enhorabuena, has descubierto la palabra: {elegida}')
