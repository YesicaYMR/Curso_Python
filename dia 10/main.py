import pygame
import random
import math
from pygame import mixer
import io


# convierte la fuente en bytes
def fuente_bytes(fuente):
    # abre el archivo TTF en modo de lectura binaria
    with open(fuente, 'rb') as f:
        # lee todos los bytes del archivo y los almacena en una variable
        ttf_bytes = f.read()
        # crea un objeto  BytesIO a partir de los bytes del archivo TTF
        return io.BytesIO(ttf_bytes)


# inicializar pygame
pygame.init()

# crea la pantalla
pantalla = pygame.display.set_mode((800, 600))

# titulo e icono de la ventana
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('fondo.jpg')

# agregar musica
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# variables del jugador y coordenadas
img_jugador = pygame.image.load('astronave.png')
coordenada_x = 368
coordenada_y = 500
coordenada_x_cambio = 0

# variables del marciano y coordenadas
img_marciano = []
coordenada_marciano_x = []
coordenada_marciano_y = []
coordenada_marciano_x_cambio = []
coordenada_marciano_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_marciano.append(pygame.image.load('marciano.png'))
    coordenada_marciano_x.append(random.randint(0, 736))
    coordenada_marciano_y.append(random.randint(50, 200))
    coordenada_marciano_x_cambio.append(0.1)
    coordenada_marciano_y_cambio.append(50)

# variables de la bala y coordenadas
img_bala = pygame.image.load('bala.png')
coordenada_bala_x = 0
coordenada_bala_y = 500
coordenada_bala_x_cambio = 0
coordenada_bala_y_cambio = 1
bala_visible = False

# puntuacion
puntuacion = 0
fuente_como_bytes = fuente_bytes('orange.ttf')
fuente = pygame.font.Font('orange.ttf', 40)
texto_x = 10
texto_y = 10

# texto final del juego
fuente_final = pygame.font.Font('orange.ttf', 45)


# funcion para mostrar texto
def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (200, 200))


# funcion mostrar puntuacion
def mostrar_puntuacion(x, y):
    texto = fuente.render(f'Puntos: {puntuacion}', True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# funcion jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# funcion marciano
def marciano(x, y, marc):
    pantalla.blit(img_marciano[marc], (x, y))


# funcion para disparar bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


# funcion detectar impacto
def hay_impacto(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False


# mantener ventana abierta
se_ejecuta = True

while se_ejecuta:
    # color de fondo
    # pantalla.fill((4, 23, 112))

    # establecer imagen de fondo
    pantalla.blit(fondo, (0, 0))

    # iterar eventos
    for evento in pygame.event.get():
        # evento comprueba cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # evento presionar flechas y disparar
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                coordenada_x_cambio = -0.1
            if evento.key == pygame.K_RIGHT:
                coordenada_x_cambio = 0.1
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.play()
                if not bala_visible:
                    coordenada_bala_x = coordenada_x
                    disparar_bala(coordenada_bala_x, coordenada_bala_y)

        # evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                coordenada_x_cambio = 0

    # modificar ubicacion cohete
    coordenada_x += coordenada_x_cambio

    # mantener cohete dentro de la pantalla
    if coordenada_x <= 0:
        coordenada_x = 0
    elif coordenada_x >= 736:
        coordenada_x = 736

    # modificar ubicacion marciano
    for e in range(cantidad_enemigos):

        # fin del juego
        if coordenada_marciano_y[e] > 500:
            for k in range(cantidad_enemigos):
                coordenada_marciano_y[k] = 1000
            texto_final()
            break

        coordenada_marciano_x[e] += coordenada_marciano_x_cambio[e]

        # mantener marciano dentro de la pantalla
        if coordenada_marciano_x[e] <= 0:
            coordenada_marciano_x_cambio[e] = 0.1
            coordenada_marciano_y[e] += coordenada_marciano_y_cambio[e]
        elif coordenada_marciano_x[e] >= 736:
            coordenada_marciano_x_cambio[e] = -0.1
            coordenada_marciano_y[e] += coordenada_marciano_y_cambio[e]

        # impacto
        impacto = hay_impacto(coordenada_marciano_x[e], coordenada_marciano_y[e], coordenada_bala_x, coordenada_bala_y)
        if impacto:
            sonido_colision = mixer.Sound('Golpe.mp3')
            sonido_colision.play()
            coordenada_bala_y = 500
            bala_visible = False
            puntuacion += 1
            coordenada_marciano_x[e] = random.randint(0, 736)
            coordenada_marciano_y[e] = random.randint(50, 200)

        marciano(coordenada_marciano_x[e], coordenada_marciano_y[e], e)

    # movimiento bala
    if coordenada_bala_y <= -32:
        coordenada_bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(coordenada_bala_x, coordenada_bala_y)
        coordenada_bala_y -= coordenada_bala_y_cambio

    jugador(coordenada_x, coordenada_y)
    mostrar_puntuacion(texto_x, texto_y)

    # actualizar la pantalla
    pygame.display.update()
