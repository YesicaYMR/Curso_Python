import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

# crear base de datos
ruta = 'empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

# cargar lista imagenes y nombres de los empleados
for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])


# codificar imagenes
def codificar(imagenes):
    # crear lista nueva
    lista_codificada = []

    # pasar imagenes a rgb
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        # codificar las caras
        codificado = fr.face_encodings(imagen)[0]

        # agregar a la lista
        lista_codificada.append(codificado)

    # devolver lista codificada
    return lista_codificada

#regiastrar hora ingreso
def registrar_ingreso(persona):
    f=open('registro.csv','r+')
    lista_datos=f.readlines()
    nombres_registro=[]
    for linea in lista_datos:
        ingreso=linea.split(',')
        nombres_registro.append(ingreso[0])

    if persona not in nombres_registro:
        ahora=datetime.now()
        string_ahora=ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona}, {string_ahora}')


lista_empleados_codificada = codificar(mis_imagenes)

#tomar imagen de la camara web
captura=cv2.VideoCapture(0,cv2.CAP_DSHOW)

#leer imagen camara
exito, imagen_capturada=captura.read()

if not exito:
    print('No se ha podido tomar la captura')
else:
    #reconocer cara en captura
    cara_captura=fr.face_locations(imagen_capturada)

    #codificar cara capturada
    cara_captura_codificada=fr.face_encodings(imagen_capturada, cara_captura)

    #buscar coincidencias en la base de datos
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias=fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias=fr.face_distance(lista_empleados_codificada,caracodif)

        indice_coincidencia=numpy.argmin(distancias)

        #mostrar coincidencias si las hay
        if distancias[indice_coincidencia]>0.6:
            print('No hay coincidencias')

        else:

            #buscar el nombre de la coincidencia
            nombre=nombres_empleados[indice_coincidencia]

            y1,x2,y2,x1=caraubic
            cv2.rectangle(imagen_capturada,
                          (x1,y1),
                          (x2,y2),
                          (0,255,0),
                          2)
            cv2.rectangle(imagen_capturada,
                          (x1,y2 -35),
                          (x2,y2),
                          (0,255,0),
                          cv2.FILLED)
            cv2.putText(imagen_capturada,
                        nombre,
                        (x1+6,y2-6),
                        cv2.FONT_HERSHEY_COMPLEX,
                        1,
                        (255,255,255))

            registrar_ingreso(nombre)

            #mostrar imagen obtenida
            cv2.imshow('imagen web', imagen_capturada)

            #mantener ventana abierta
            cv2.waitKey(0)




