import bs4
import requests

# crear url sin numero de pagina
url_base = 'http://books.toscrape.com/catalogue/page-{}.html'

# lista de titulos con 4 o 5  estrellas
titulos_rating_alto = []

# loop paginas
for pagina in (1, 50):

    # crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # seleccionar libros
    libros = sopa.select('.product_pod')

    # iterar libror
    for libro in libros:

        # comprobar calificacion alta
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            # guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']

            # agregar libro a lista
            titulos_rating_alto.append(titulo_libro)

# ver libros 4 o 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)
