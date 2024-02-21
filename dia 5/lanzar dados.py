from random import randint


# Lanzar dados
def lanzar_dados():
    dado = randint(1, 7)

    return (dado)


# evaluar jugada
def evaluar_jugada(dado1, dado2):
    mensaje = ''
    suma = dado1 + dado2
    if suma <= 6:
        mensaje = f"La suma de tus dados es {suma}. Lamentable"
    elif suma > 6 and suma < 10:
        mensaje = f"La suma de tus dados es {suma}. Tienes buenas chances"
    else:
        mensaje = f"La suma de tus dados es {suma}. Parece una jugada ganadora"
    return mensaje

jugada1 = lanzar_dados()
jugada2 = lanzar_dados()
print(evaluar_jugada(jugada1, jugada2))

