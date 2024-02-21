def saludar_persona(nombre):
    '''
    comentario
    :return:
    '''
    #esta linea tb es comentario
    print('Hola '+nombre)

saludar_persona('Juan')


'''def chequear_3_cifras(numero):
    return numero in range(100,1000)'''

suma=40+86



'''def chequear_3_cifras(lista):
    for numero in lista:
        if numero in range(100,1000):
            return numero
        else:
            pass
        
        return False'''

def chequear_3_cifras(lista):
    lista_3_cifras=[]
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras
resultado=chequear_3_cifras([555,99,600])
print(resultado)

precios_cafe=[('capuchino',1.5),('Expresso', 1.2),('Moka',1.9)]

def cafe_mas_caro(lista_precios):
    precio_mayor=0
    cafe_mas_caro=""

    for cafe,precio in lista_precios:
        if precio>precio_mayor:
            precio_mayor=precio
            cafe_mas_caro=cafe
        else:
            pass
    return (cafe_mas_caro,precio_mayor)

print(cafe_mas_caro(precios_cafe))
cafe, precio=cafe_mas_caro(precios_cafe)
print(f'El cafe más caro es {cafe} y cuesta {precio}')