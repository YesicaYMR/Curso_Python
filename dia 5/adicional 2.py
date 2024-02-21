def deletrea_ordena(palabra):
    letras = list(set(palabra[::1]))

    letras.sort()
    print(letras)


deletrea_ordena('agua')

