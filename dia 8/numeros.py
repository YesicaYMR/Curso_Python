def decorar_saludo(funcion):
    print('Su turno es:')
    print(funcion)
    print('Espere a ser atendido')


@decorar_saludo
def cosmetica():
    x = 1
    while True:
        x += 1
        yield f'c- {x}'


@decorar_saludo
def farmacia():
    x = 1
    while True:
        x += 1
        yield f'f- {x}'


@decorar_saludo
def perfumeria():
    x = 1
    while True:
        x += 1
        yield f'p- {x}'
