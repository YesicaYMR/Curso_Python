texto = input("introduce un texto: ")
letras = []

texto = texto.lower()

letras.append(input('introduce una letra').lower())
letras.append(input('introduce una letra').lower())
letras.append(input('introduce una letra').lower())

print("\n")
print("Cantidad de letras")
n_letra1 = texto.count(letras[0])
n_letra2 = texto.count(letras[1])
n_letra3 = texto.count(letras[2])

print(f'"{letras[0]}" aparece {n_letra1}')
print(f'"{letras[1]}" aparece {n_letra2}')
print(f'"{letras[2]}" aparece {n_letra3}')