import os
from os import system
from pathlib import Path

ruta = Path('C:/Users/Yesica/Desktop/Python/Tema 6 - Manipular archivos/Recetas')


def contar_recetas(carpeta):
    contador = 0
    for txt in Path(carpeta).glob('**/*.txt'):
        contador += 1
    print(f'Tienes un total de {contador} recetas\n')


def elegir_opcion():
    print('''\n1- Leer receta
2- Crear receta
3- Crear categoría
4- Eliminar receta
5- Eliminar categoria
6- Finalizar programa''')
    eleccion = input('¿Que opción deseas realizar?: ')
    return eleccion


def limpiar_consola():
    input('pulse una tecla para volver al menú principal')
    system('cls')


def leer_receta(carpeta):
    categoria = elegir_categoria(carpeta)
    ruta_receta = Path(mostrar_recetas(carpeta, categoria))
    receta = open(ruta_receta)
    print(f'\n{receta.read()}\n')


def mostrar_recetas(carpeta, categoria_elegida):
    categorias = os.listdir(Path(carpeta))
    subcarpeta = categorias[int(categoria_elegida) - 1]
    ruta_completa = Path(carpeta, subcarpeta)
    lista_recetas=os.listdir(Path(ruta_completa))

    if len(lista_recetas)<1 :
        print('\nNo hay recetas en esta categoría')
        elegir_categoria(carpeta)
        return carpeta


    else:
        contador = 1
        lista_recetas = os.listdir(Path(ruta_completa))
        for receta in lista_recetas:
            print(f'{contador} - {receta}')
            contador += 1
        eleccion = input('Elige la receta que deseas : ')
        correcto = controlar_numero(eleccion, len(lista_recetas))
        while not correcto:
            print('Elija un código correcto')
            eleccion = input('¿Qué categoria eliges?: ')
            correcto = controlar_numero(eleccion, len(lista_recetas))
        print(f'Has elegido: {lista_recetas[int(eleccion) - 1]}')
        ruta_completa = Path(Path(ruta_completa), lista_recetas[int(eleccion) - 1])
        return ruta_completa


def crear_receta(carpeta):
    categorias = os.listdir(Path(carpeta))
    categoria = elegir_categoria(carpeta)
    ruta_receta = Path(Path(carpeta), categorias[int(categoria) - 1])
    nombre = input('\nNombre de la receta: ') + '.txt'
    contenido = input('\ncontenido de la receta: ')
    nombre_receta = Path(ruta_receta, nombre)
    nueva_receta = open(Path(nombre_receta), 'w')
    nueva_receta.write(contenido)
    print(f'\n{nombre} ha sido creada con éxito en la carpeta {categorias[int(categoria) - 1]}\n')


def crear_categoria(carpeta):
    categorias = os.listdir(Path(carpeta))
    nueva_categoria = input('Nombre de la nueva categoria: ')
    while nueva_categoria in categorias:
        print('Categoria existente')
        nueva_categoria = input('Nombre de la nueva categoria: ')

    os.makedirs(Path(Path(carpeta), nueva_categoria))
    print(f'La nueva categoria {nueva_categoria} ha sido creada con exito')


def eliminar_receta(carpeta):
    categoria = elegir_categoria(carpeta)
    ruta_receta = Path(mostrar_recetas(carpeta, categoria))
    receta = Path(ruta_receta)
    os.remove(Path(ruta_receta))
    print(f'La receta ha sido eliminada con exito')


def eliminar_categoria(carpeta):
    categorias = os.listdir(Path(carpeta))
    categoria = elegir_categoria(carpeta)
    ruta_categoria = Path(carpeta, categorias[int(categoria) - 1])
    os.rmdir(ruta_categoria)
    print(f'La categoria {categorias[int(categoria) - 1]} ha sido eliminada con exito')


def elegir_categoria(carpeta):
    categorias = os.listdir(Path(carpeta))
    contador = 1
    num_categorias = len(categorias)
    print('\n Estas son las categorías disponibles')
    for carpeta in categorias:
        print(f'{contador} - {carpeta}')
        contador += 1
    eleccion = input('¿Qué categoria eliges?: ')
    correcto = controlar_numero(eleccion, num_categorias)
    while not correcto:
        print('Elija un código correcto')
        eleccion = input('¿Qué categoria eliges?: ')
        correcto = controlar_numero(eleccion, num_categorias)
    print(f'Has elegido: {categorias[int(eleccion) - 1]}')
    return eleccion


def controlar_numero(texto, num_categorias):
    if not texto.isdigit():
        return False
    else:
        if int(texto) < 0 or int(texto) > int(num_categorias):
            return False
        else:
            return True


"""-------------------------------------------------------------------------"""
print("Bienvenido")
print(f'Las recetas se encuentran en {ruta}\n')
contar_recetas(ruta)
opcion = elegir_opcion()
while opcion != '6':
    match opcion:
        case '1':
            leer_receta(ruta)
            limpiar_consola()
            opcion = elegir_opcion()
        case '2':
            crear_receta(ruta)
            limpiar_consola()
            opcion = elegir_opcion()
        case '3':
            crear_categoria(ruta)
            limpiar_consola()
            opcion = elegir_opcion()
        case '4':
            eliminar_receta(ruta)
            limpiar_consola()
            opcion = elegir_opcion()
        case '5':
            eliminar_categoria(ruta)
            limpiar_consola()
            opcion = elegir_opcion()
        case '6':
            exit()
        case _:
            print('Elija una opción valida\n')
            opcion = elegir_opcion()
