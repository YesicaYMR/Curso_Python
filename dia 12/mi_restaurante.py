from tkinter import *
import random
import datetime
from tkinter import filedialog,messagebox

operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94]


def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)


def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''


def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0, END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1

    x = 0
    for c in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0, END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1


def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    sub_total_postres = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1

    subtotal = sub_total_comida + sub_total_bebida + sub_total_postres
    impuestos = subtotal * 0.7
    total = subtotal + impuestos

    var_gastos_comida.set(f'{round(sub_total_comida,2)} €')
    var_gastos_bebida.set(f'{round(sub_total_bebida,2)} €')
    var_gastos_postres.set(f'{round(sub_total_postres,2)} €')
    var_subtotal.set(f'{round(subtotal,2)} €')
    var_impuesto.set(f'{round(impuestos,2)} €')
    var_total.set(f'{round(total,2)} €')


def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos: {num_recibo} \t\t {fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, 'art.\t\tCant.\tPrecio\n')
    texto_recibo.insert(END, f'-' * 54 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t'
                                     f'{int(comida.get()) * precios_comida[x]} €\n')
        x += 1

    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t'
                                     f'{int(bebida.get()) * precios_bebida[x]} €\n')
        x += 1

    x = 0
    for postres in texto_postres:
        if postres.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postres.get()}\t'
                                     f'{int(postres.get()) * precios_postres[x]} €\n')
        x += 1

    texto_recibo.insert(END, f'-' * 54 + '\n')
    texto_recibo.insert(END, f'Subtotal:\t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos:\t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Importe:\t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*' * 47 + '\n')
    texto_recibo.insert(END, f'Gracias por su visita')

def guardar():
    info_recibo=texto_recibo.get(1.0,END)
    archivo=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Información','El recibo ha sido guardado')

def limpiar():
    texto_recibo.delete(0.1,END)

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebida:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    for v in variables_comida:
        v.set('0')
    for v in variables_bebida:
        v.set('0')
    for v in variables_postres:
        v.set('0')

    var_gastos_comida.set('')
    var_gastos_bebida.set('')
    var_gastos_postres.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')




# iniciar tkinter
aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry('1125x630+0+0')

# evitar maximizar
aplicacion.resizable(0, 0)

# titulo ventana
aplicacion.title('Mi restaurante - Sistema de facturación')

# cambiar color de fondo
aplicacion.config(bg='PaleTurquoise')

# panel superior
panel_superior = Frame(aplicacion,
                       bd=1,
                       relief=FLAT)
panel_superior.pack(side=TOP)

# etiqueta titulo
etiqueta_titulo = Label(panel_superior,
                        text='Sistema de facturación',
                        fg='blue2',
                        font=('Dosis', 50),
                        bg='PaleTurquoise',
                        width=27)
etiqueta_titulo.grid(row=0,
                     column=0)

# panel izquierdo
panel_izquierdo = Frame(aplicacion,
                        bd=1,
                        relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# panel gastos
panel_gastos = Frame(panel_izquierdo,
                     bd=1,
                     relief=FLAT,
                     bg='azure4',
                     padx=70)
panel_gastos.pack(side=BOTTOM)

# panel comidas
panel_comidas = LabelFrame(panel_izquierdo,
                           text='Comida',
                           font=('Dosis', 19, 'bold'),
                           bd=1,
                           relief=FLAT,
                           fg='PaleTurquoise')
panel_comidas.pack(side=LEFT)

# panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo,
                           text='Bebidas',
                           font=('Dosis', 19, 'bold'),
                           bd=1,
                           relief=FLAT,
                           fg='PaleTurquoise')
panel_bebidas.pack(side=LEFT)

# panel postres
panel_postres = LabelFrame(panel_izquierdo,
                           text='Postres',
                           font=('Dosis', 19, 'bold'),
                           bd=1,
                           relief=FLAT,
                           fg='PaleTurquoise')
panel_postres.pack(side=LEFT)

# panel derecha
panel_derecha = Frame(aplicacion,
                      bd=1,
                      relief=FLAT)
panel_derecha.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame(panel_derecha,
                          bd=1,
                          relief=FLAT,
                          bg='burlywood')
panel_calculadora.pack()

# panel recibo
panel_recibo = Frame(panel_derecha,
                     bd=1,
                     relief=FLAT,
                     bg='burlywood')
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_derecha,
                      bd=1,
                      relief=FLAT,
                      bg='burlywood')
panel_botones.pack()

# lista de productos
lista_comidas = ['pollo', 'cordero', 'salmon', 'merluza', 'pasta', 'arroz', 'pizza']
lista_bebidas = ['agua', 'batidos', 'zumos', 'refresco', 'creveza', 'vino', 'cubata']
lista_postres = ['helado', 'fruta', 'flan', 'mousse', 'tarta chocolate', 'tarta de queso', 'yogur']

# generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    # crear check buttons
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W)

    # crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)

    contador += 1

# generar items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    # crear check buttons
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis', 19, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador],
                         command=revisar_check)
    bebida.grid(row=contador,
                column=0,
                sticky=W)

    # crear cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('dosis', 18, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)

    contador += 1

# generar items postres
variables_postres = []
cuadros_postres = []
texto_postres = []
contador = 0
for postres in lista_postres:
    # crear check buttons
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres,
                          text=postres.title(),
                          font=('Dosis', 19, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=variables_postres[contador],
                          command=revisar_check)
    postres.grid(row=contador,
                 column=0,
                 sticky=W)

    # crear cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,
                                      font=('dosis', 18, 'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador,
                                   column=1)

    contador += 1

# variables
var_gastos_comida = StringVar()
var_gastos_bebida = StringVar()
var_gastos_postres = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# eitquetas de gastos y campos de entrada
etiqueta_gastos_comida = Label(panel_gastos,
                               text='Gastos de comida',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_gastos_comida.grid(row=0, column=0)

texto_gastos_comidas = Entry(panel_gastos,
                             font=('Dosis', 12, 'bold'),
                             bd=1,
                             width=10,
                             state='readonly',
                             textvariable=var_gastos_comida)
texto_gastos_comidas.grid(row=0,
                          column=1,
                          padx=41)

etiqueta_gastos_bebida = Label(panel_gastos,
                               text='Gastos de bebida',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_gastos_bebida.grid(row=1, column=0)
texto_gastos_bebidas = Entry(panel_gastos,
                             font=('Dosis', 12, 'bold'),
                             bd=1,
                             width=10,
                             state='readonly',
                             textvariable=var_gastos_bebida)
texto_gastos_bebidas.grid(row=1,
                          column=1,
                          padx=41)
etiqueta_gastos_postres = Label(panel_gastos,
                                text='Gastos de postres',
                                font=('Dosis', 12, 'bold'),
                                bg='azure4',
                                fg='white')
etiqueta_gastos_postres.grid(row=2, column=0)
texto_gastos_postres = Entry(panel_gastos,
                             font=('Dosis', 12, 'bold'),
                             bd=1,
                             width=10,
                             state='readonly',
                             textvariable=var_gastos_postres)
texto_gastos_postres.grid(row=2,
                          column=1,
                          padx=41)

etiqueta_subtotal = Label(panel_gastos,
                          text='Subtotal',
                          font=('Dosis', 12, 'bold'),
                          bg='azure4',
                          fg='white')
etiqueta_subtotal.grid(row=0, column=2)
texto_subtotal = Entry(panel_gastos,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_subtotal)
texto_subtotal.grid(row=0,
                    column=3,
                    padx=41)
etiqueta_impuesto = Label(panel_gastos,
                          text='Impuestos',
                          font=('Dosis', 12, 'bold'),
                          bg='azure4',
                          fg='white')
etiqueta_impuesto.grid(row=1, column=2)
texto_impuesto = Entry(panel_gastos,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_impuesto)
texto_impuesto.grid(row=1,
                    column=3,
                    padx=41)

etiqueta_total = Label(panel_gastos,
                       text='Total',
                       font=('Dosis', 12, 'bold'),
                       bg='azure4',
                       fg='black')
etiqueta_total.grid(row=2, column=2)
texto_total = Entry(panel_gastos,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=10,
                    state='readonly',
                    textvariable=var_total)
texto_total.grid(row=2,
                 column=3,
                 padx=41)

# botones
botones = ['Total', 'Recibo', 'Guardar', 'Borrar']
botones_creados = []
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Dosis', 14, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=7)
    botones_creados.append(boton)
    boton.grid(row=0,
               column=columnas)
    columnas += 1
botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=limpiar)

# crear recibo
texto_recibo = Text(panel_recibo,
                    bd=1,
                    font=('Dosis', 12, 'bold'),
                    width=42,
                    height=10)
texto_recibo.grid(row=0,
                  column=0)

# calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 16, 'bold'),
                          width=32,
                          bd=1, )
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'x', '=', 'ce', '0', '/']

botones_guardados = []
fila = 1
columna = 0

for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Dosis', 16, 'bold'),
                   fg='white',
                   bg='azure4',
                   bd=1,
                   width=7)
    botones_guardados.append(boton)

    boton.grid(row=fila,
               column=columna)
    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click_boton('0'))
botones_guardados[15].config(command=lambda: click_boton('/'))

# evitar que la pantalla se cierre
aplicacion.mainloop()
