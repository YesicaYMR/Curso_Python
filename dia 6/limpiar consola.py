from os import system
from pathlib import Path


nombre=input("Dime tu nombre: ")
edad= input ("dime tu edad: ")

system('cls')

print(f"Tu nombre es {nombre} y tienes {edad} años")

ruta = Path('C:/Users/Usuario/Desktop/Curso Python') / 'Cuestionario Día 6' / 'Pregunta 1'
carpeta = ruta.parents[3]
print(carpeta)