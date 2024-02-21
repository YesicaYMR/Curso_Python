mi_archivo=open('prueba.txt')

todas=mi_archivo.readlines()
print(todas)

for l in mi_archivo:
    print("Aqui dice: "+l)


una_linea=mi_archivo.readline()
print(una_linea.upper())

una_linea=mi_archivo.readline()
print(una_linea.rstrip())

una_linea=mi_archivo.readline()
print(una_linea)

print(mi_archivo.read())

mi_archivo.close()