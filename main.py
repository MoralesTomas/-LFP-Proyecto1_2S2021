import  tkinter as tk
from tkinter import filedialog, image_names
import pathlib
import sys
from datos.imagen import imagen


Contenido = ""
listaImagen = []
def leerArchivo(ruta):
    global Contenido
    print('------- Buscando archivo de entrada -------\n')
    try:
        with open(ruta, encoding='utf-8') as file:
            contenido = file.read()
            print("\n----------- Carga completada ----------\n")
            Contenido = contenido
    except:
        print('No se pudo abrir el fichero de la ruta: ' + ruta)
        print("El eror fue : ",sys.exc_info()[0],"\n")

def cargarArchivo():
    root = tk.Tk()
    root.withdraw()
    filename = filedialog.askopenfilename()
    path = pathlib.Path(filename)
    extension = path.suffix
    if extension == ".pxla" or extension == ".PXLA":
        #continuamos con la ejecucion del programa
        leerArchivo(filename)
    else:
        print("\nEl archivo no es de la extension requerida.")

def op1():
    try:
        cargarArchivo()
    except:
        print("Ocurrio un error, el cual fue ", sys.exc_info()[0])

def separarArroba(contenido):
    global log
    imagenes = []
    actual = ""
    estado = 0
    contador = 0
    longitud = len(contenido)
    for i in contenido:
        contador += 1
        if estado == 0:
            if i == "\"":
                estado =1
            elif i == "@":
                estado =2
                continue
            else:
                actual += i
                continue
        if estado == 1:
            actual += i
            #pasamos al estado tres para comenzar a leer lo que esta dentro de las comillas dobles
            estado = 3
            continue
        if estado == 2:
            if i == "@":
                #el estado 4 es para ver que se hagan los 4 arrobas seguidos 
                estado = 4
                continue
            else:
                actual += "@"+i
                estado = 0
                continue
        if estado == 3:
            if i != "\"":
                actual += i
                continue
            else:
                actual += i
                estado = 0
                continue
        if estado == 4:
            if i == "@":
                #segunda arroba
                estado = 5
                continue
            else:
                estado =0
                actual += "@"+i
                continue
        if estado == 5:
            if i == "@":
                #3 arroba
                estado = 6
                continue
            else:
                estado =0
                actual += "@@"+i
                continue
        if estado ==6:
            if i ==" " or i == "\n" or i == "\t":
                imagenes.append(actual)
                estado = 0
                actual = i
                continue
            else:
                estado = 0
                actual += "@@@@"+i
        
    imagenes.append(actual)
    return imagenes

def separarToken(dato):
    pass

def asignarDatos():
    global listaImagen,Contenido
    separado = separarArroba(Contenido)
    for i in separado:
        nuevo = imagen(i)
        listaImagen.append(nuevo)

op1()
asignarDatos()
