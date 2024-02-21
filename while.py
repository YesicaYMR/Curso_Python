monedas=5

while monedas>0:
    print(f'Tengo {monedas} monedas')
    monedas-=1
else:
    print('no tengo mas monedas')

respuesta='s'
while respuesta=='s':
    respuesta=input("Quieres seguir?(s/n)")
else:
    print("Gracias")

