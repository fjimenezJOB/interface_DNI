from tkinter import *
from tkinter import messagebox

# Zonas
# ************************* Raiz ***************************
raiz = Tk()
raiz.anchor()
raiz.title('Verificador de Dni')
raiz.resizable(0, 0)
raiz.geometry('900x500')

# **************** Funciones ******************************
def ventanaPregunta():
    valor = messagebox.askokcancel('Cerrar', 'Quieres salir?')
    if valor == True:
        raiz.destroy()

def letraDNI():
    dni = int(introducirDni.get())
    # CONJUNTO DE LETRAS CREADO POR LA POLICIA NACIONAL
    listaLetras = 'TRWAGMYFPDXBNJZSQVHLCKE'
    # BUSQUEDA DE LA LETRA
    letra = listaLetras[dni % 23]
    # IMPRIMIR NUMEROS + LETRA
    respuesta = (f'{dni}-{letra}'.upper())
    resultado.config(text=respuesta)

# ********************************************************

# ************************* MENU ***************************

barraMenu = Menu(raiz)
raiz.config(menu=barraMenu)
cerrar = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label='Cerrar', command=ventanaPregunta)

# ********************************************************

# ********************** Frame header ***********************
frameHead = Frame(raiz)
frameHead.pack(fill='x', expand='True', anchor='n')
frameHead.config(height='80')

# Foto Miniserio
ministerio_imagen = PhotoImage(file='static/img/descarga.png')
fotoMinisterio = Label(frameHead, image=ministerio_imagen)
fotoMinisterio.config(height='80')
fotoMinisterio.pack()

# ********************************************************
# ********************** Frame main Izquierdo ************
#
frameMainIz = Frame(raiz)
frameMainIz.place(x=0, y=80)
frameMainIz.config(width=450, height=260, pady=10, padx=10)

# Foto dni
fotoDni = PhotoImage(file='static\img\dni.png')
Label(frameMainIz, image=fotoDni).pack()

# ********************************************************
# ****************** Frame main Derecho ******************

zonaBuscar = StringVar()
frameMainDe = Frame(raiz)
frameMainDe.place(x=420, y=100)
frameMainDe.config(width=400, height=260, padx=30, pady=30)

# Titulo
titulo = Label(frameMainDe, text='Buscamos tu letra', font=('Arial', 30))
titulo.grid(row=0, column=0, columnspan=2)


# Input
introducirDni = Entry(frameMainDe, textvariable=zonaBuscar)
introducirDni.config(font=('Arial', 15))
introducirDni.grid(row=1, column=0, pady=30)


# Boton
resultadoDni = Button(frameMainDe, text='Comprobar', command=letraDNI)
resultadoDni.config(font=('Arial', 15))
resultadoDni.grid(row=1, column=1)


# Resultado
resultado = Label(frameMainDe)
resultado.config(font=('Arial', 15))
resultado.grid(row=2, column=0)
# ********************************************************
# ****************** Frame Footer ******************
frameFooter = Frame(raiz)
frameFooter.pack(fill='x', expand='True', anchor='s')
frameFooter.config(height='80', bg='red')

raiz.mainloop()
