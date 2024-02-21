if 5==2:
    print("es correcto")
else:
    print("no es correcto")

mascota="perro"
if mascota=='gato':
    print('Tienes un gato')
elif mascota=='perro':
    print('tienes un perro')
elif mascota=='pez':
    print('Tienes un pez')
else:
    print("no sé que animal tienes")

edad=16
calificacion=9
if edad<18:
    print('Eres menor de edad')
    if calificacion>=7:
        print('Aprobado')
    else:
        print('No aprobado')
else:
    print('Eres adulto')