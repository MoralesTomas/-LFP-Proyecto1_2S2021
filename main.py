import  tkinter as tk
from tkinter import filedialog, image_names
import pathlib
import sys
from datos.imagen import imagen
from archivo import archivo
import re
import sys


Contenido = ""
listaImagen = []

def automataFiltros(valor):
    estado = 0
    actual = ""
    contador = 0
    for i in valor:
        contador += 1
        if estado == 0:
            if i != ",":
                continue
            else:
                if contador == len(valor):
                    return False
                estado = 1
                continue
        if estado == 1:
            if i == " " or i=="\n" or i=="\t" or i =="":
                return False 
            else:
                estado = 0
                continue
    filtros = splitear(valor,",")
    for i in filtros:
        if i == "MIRRORX" or i == "MIRRORY" or i == "DOUBLEMIRROR":
            pass
        else:
            return False
    return True

def splitear(contenido,caracter):
    listado = []
    actual= ""
    for i in contenido:
        if i != caracter:
            actual += i
        else:
            listado.append(actual.strip())
            actual = ""
    if actual != "":
        listado.append(actual.strip())
    return listado

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

def automataCadena(valor):
    estado = 0
    actual = ""
    valor = valor.strip()
    valor += "#"
    longitud = len(valor)
    contador = 0
    for i in valor:
        contador += 1
        if estado == 0 :
            if i == "\"":
                estado = 1
                continue
            else:
                return False
        if estado == 1:
            if i != "\"":
                actual += i
                continue
            else:
                estado = 2
                continue
        if estado == 2:
            if contador == longitud:
                if i == "#":
                    return True
    return False

def separarToken(imagen):
    listado = splitear(imagen.datos,";")
    for i in listado:
        subListado  = splitear(i,"=")
        if len(subListado) == 2:
            token = subListado[0].strip()
            valor = subListado[1].strip()
            if token == "TITULO":
                if automataCadena(valor):
                    valor = valor.replace("\"","")
                    imagen.titulo = valor.strip()
            elif token == "ANCHO":
                valor = valor.strip()
                if valor.isdigit():
                    imagen.ancho = int(valor)
            elif token == "ALTO":
                valor = valor.strip()
                if valor.isdigit():
                    imagen.alto = int(valor)
            elif token == "FILAS":
                valor = valor.strip()
                if valor.isdigit():
                    imagen.filas = int(valor)
            elif token == "COLUMNAS":
                valor = valor.strip()
                if valor.isdigit():
                    imagen.columnas = int(valor)
            elif token == "CELDAS":
                if automataCeldas(valor):
                    imagen.celdas = valor #solo texto
            elif token == "FILTROS":
                if automataFiltros(valor):
                    imagen.filtros = valor

def automataCeldas(celdas):
    estado = 0
    actual = ""
    celdas = celdas.strip()
    contador = 0
    for i in celdas:
        contador += 1
        if estado == 0:
            if i == "{":
                estado = 1
                continue
            else:
                return False
        if estado == 1:
            if i == "[":
                estado =2
                continue
            if i =="\n" or i == "\t" or i == " ":
                    continue
            else:
                return False
        #celda del eje x
        if estado == 2:
            if i.isdigit():
                estado = 3
                continue
            else:
                return False
        if estado == 3:
            if i !=",":
                if i.isdigit():
                    continue
                else:
                    return False
            else:
                estado = 4
                continue
        #celda del eje y filas
        if estado == 4:
            if i.isdigit():
                estado = 5
                continue
            else:
                return False
        if estado == 5:
            if i !=",":
                if i.isdigit():
                    continue
                else:
                    return False
            else:
                estado = 6
                continue
        if estado == 6: 
            if i != ",":
                actual += i
                continue
            else:
                if actual == "TRUE" or actual =="FALSE":
                    actual = ""
                    estado = 7
                    continue
                else:
                    return False
        if estado ==7:
            if i != "]":
                actual += i
                continue
            else:
                if re.search("^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$",actual):
                    estado = 8
                    actual = ""
                    continue
                else:
                    return False
        if estado == 8 :
            if contador == len(celdas):
                if i == "}":
                    return True
                else:
                    return False
            if i != ",":
                if i =="\n" or i == "\t" or i == " ":
                    continue
                else:
                    return False
            if i == ",":
                estado = 1
                continue
    return False

def asignarDatos():
    global listaImagen,Contenido
    separado = separarArroba(Contenido)
    for i in separado:
        nuevo = imagen(i)
        listaImagen.append(nuevo)
    for i in listaImagen:
        separarToken(i)
    for i in listaImagen:
        i.autoLlenado()
        # i.mostrarDatos()
        # i.mostrarListado()
    contador = 1
    for i in listaImagen:
        try:
            repTmp = archivo(i)
            repTmp.generar()
        except:
            print(f"No se pudo generar el reporte de la imagen #{contador}")
        contador += 1

#solo para la carga y la lectura.
op1()

#para analizar los datos de la lectura // crea el html y las imagenes en png
asignarDatos()

