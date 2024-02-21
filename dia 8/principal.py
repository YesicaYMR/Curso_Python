import numeros
departamentos=['perfumeria', 'farmacia', 'cosmetica']
def mostrar_departamentos():
    x = 1
    for departamento in departamentos:
        print(f"{x} - {departamento}")
        x+=1


def pedir_departamento():
    while True:
        try:
            eleccion=int(input('A que departamento desea ir: '))
        except:
            print('ingrese una opcion valida')
        else:
            return eleccion

def comprobar_departamento(numero):
    if numero>0 and numero<len(departamentos):
        return True
    else:
        return False


print('******Bienvenido******')
mostrar_departamentos()
elegido=pedir_departamento()
valido=comprobar_departamento(elegido)
while not valido:
    print('Departamento no valido')
    elegido=pedir_departamento()
    valido=comprobar_departamento()

if valido==1:
    print(next(numeros.perfumeria))

elif valido==2:
    numeros.farmacia

elif valido==3:
    numeros.cosmetica







