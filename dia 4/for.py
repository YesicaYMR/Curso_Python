lista=['a','b','c']
for letra in lista:
    numero_letra=lista.index(letra)+1
    print(f"Letra {numero_letra}:{letra}")

lista=['pablo','laura','fede','luis','julia']

for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print('no empieza con L')

numeros=[1,2,3,4,5]
mi_valor=0

for numero in numeros:
    mi_valor=mi_valor+numero
    print(mi_valor)
print(mi_valor)

for a,b in [[1,2],[2,3],[3,4],[5,6]]:
    print(a)
    print(b)

dic={'clave1':'a','clave2':'b','clave3':'c'}

for clave in dic.items():
    print(clave)