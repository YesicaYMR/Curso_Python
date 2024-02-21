import cv2
import face_recognition as fr

# cargar imagenes
foto_control = fr.load_image_file('fotoA.jpg')
foto_prueba = fr.load_image_file('fotoB.jpg')

# pasar imagenes a rgb
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# localizar cara contorl
lugar_caraA = fr.face_locations(foto_control)[0]
cara_codificada_A = fr.face_encodings(foto_control)[0]

# localizar cara prueba
lugar_caraB = fr.face_locations(foto_prueba)[0]
cara_codificada_B = fr.face_encodings(foto_prueba)[0]

# mostrar rectangulos en cara
cv2.rectangle(foto_control,
              (lugar_caraA[3], lugar_caraA[0]),
              (lugar_caraA[1], lugar_caraA[2]),
              (0, 255, 0),  # color del rectangulo
              2)  # grosor del rectangulo

cv2.rectangle(foto_prueba,
              (lugar_caraB[3], lugar_caraB[0]),
              (lugar_caraB[1], lugar_caraB[2]),
              (0, 255, 0),  # color del rectangulo
              2)  # grosor del rectangulo

# realizar comparacion de caras
resultado = fr.compare_faces([cara_codificada_A], cara_codificada_B)
print(resultado)

# medida distancia entre rostros
distancia = fr.face_distance([cara_codificada_A], cara_codificada_B)
print(distancia)

# mostrar resultados
cv2.putText(foto_prueba,
            f'{resultado} {distancia.round(2)}',
            (50, 50),  # donde se va a ubicar
            cv2.FONT_HERSHEY_COMPLEX,
            1,  # tamaño
            (0, 255, 0),  # color
            2)  # grosor

# mostrar imagenes
cv2.imshow('Foto Control', foto_control)
cv2.imshow('Foto prueba', foto_prueba)

# mantener el priograma abierto
cv2.waitKey(0)
