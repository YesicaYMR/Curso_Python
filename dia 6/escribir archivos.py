archivo=open('prueba.txt','w')
archivo.write('soy el nuevo texto')
archivo.close()

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
archivo=open('registro.txt','a')
for elemento in registro_ultima_sesion:
    archivo.writelines(elemento+'\t')
archivo.close()

archivo=open('registro.txt','r')
print(archivo.read())