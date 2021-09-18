import  tkinter as tk
from tkinter import filedialog, image_names
from pathlib import Path
import pathlib
import sys
from datos.imagen import imagen
from datos.automataRepo import AnalizadorLexico
from archivo import archivo
import webbrowser
import re
import sys
import os

#imports para la interfaz
import sys
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox


Contenido = ""
listaImagen = []
boolCarga = False
boolReportes = False

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
    global Contenido, boolCarga
    Contenido = ""
    print('------- Buscando archivo de entrada -------\n')
    try:
        with open(ruta, encoding='utf-8') as file:
            contenido = file.read()
            print("\n----------- Carga completada ----------\n")
            Contenido = contenido
            boolCarga = True
    except:
        print('No se pudo abrir el fichero de la ruta: ' + ruta)
        print("El eror fue : ",sys.exc_info()[0],"\n")
        return False

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
        return False

def op1():
    global Contenido, boolCarga
    try:
        Contenido = ""
        boolCarga = False
        cargarArchivo()
        return True
    except:
        print("Ocurrio un error, el cual fue ", sys.exc_info()[0])
        return False

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
                # print("encontro los filtros")
                # print(token,valor)
                if automataFiltros(valor):
                    imagen.filtros = valor
            else:
                imagen.lexico = False

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
    listaImagen = []
    try:
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
                print(f"No se pudo generar el reporte de los datos en la posicion #{contador}")
            contador += 1
    except:
        return False

# #solo para la carga y la lectura.
# op1()

# #para analizar los datos de la lectura // crea el html y las imagenes en png
# asignarDatos()
# r = archivo(listaImagen[0])
# r.generar()


class ejemplo_GUI(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("Interfaces//vtnPrincipal.ui", self)
        
        self.btn_Cargar.clicked.connect(self.cargar)
        self.btn_Analizar.clicked.connect(self.analizar)
        self.btn_Salir.clicked.connect(self.terminarPrograma)
        self.btn_visualizar.clicked.connect(self.primero)
        self.btnVistaOriginal.clicked.connect(self.primero)
        self.btnVistaX.clicked.connect(self.segundo)
        self.btnVistaY.clicked.connect(self.tercero)
        self.btnVistaDouble.clicked.connect(self.cuarto)
        self.btn_Reportes.clicked.connect(self.mostrarReportes)
        
    def primero(self):
        self.buscar("")

    def segundo(self):
        self.buscar("_MIRRORX")
    
    def tercero(self):
        self.buscar("_MIRRORY")
    
    def cuarto(self):
        self.buscar("_DOUBLEMIRROR")

    def cargar(self):
        global boolCarga
        if op1() is not None:
            
            if boolCarga:
                QMessageBox.information(self, "Exito","Se cargo el archivo de entrada.\n")
            else:
                QMessageBox.warning(self, "Error","Error, no se pudo cargar el archivo.\nVerifique que el archivo cumpla con la extension requerida.")
        
        else:
            QMessageBox.warning(self, "Error","Error, no se pudo cargar el archivo.\nVerifique que el archivo cumpla con la extension requerida.")
    
    def analizar(self):
        global boolReportes
        analizador = AnalizadorLexico()
        analizador.analizar(Contenido)
        analizador.impTokens()
        analizador.impErrores()
        try:
            listaToken = analizador.obtenerListaToken()
            listaErrores = analizador.obtenerListaErrores()
            boolReportes = True
            repo = archivo(None)
            repo.generarReporte("REPORTE_TOKENS",listaToken,"Lexema")
            repo.generarReporte("REPORTE_ERRORES",listaErrores,"Descripcion")
            
        except:
            pass

        if asignarDatos() is not False:
            for i in listaImagen:
                if i.verificar:
                    self.btnLista.addItem(str(i.titulo))
            
            QMessageBox.information(self, "Exito","Se analizaron los datos del archivo de entrada.\n")
            
        else:
            QMessageBox.warning(self, "Error","Error, para analizar datos se necesita que cargue un archivo inicial.")

    def buscar(self,agregar):
        nombre = self.btnLista.currentText()
        for i in listaImagen:
            if i.verificar:
                if i.titulo == nombre:
                    nombre = nombre + agregar
                    ruta = "imagenes//"+nombre+".png"
                    fileObj = Path(ruta)
                    try:
                        if fileObj.is_file():
                            pixmapImagen = QPixmap(ruta).scaled(400,400,Qt.KeepAspectRatio,Qt.SmoothTransformation)
                            self.areaImagen.setPixmap(pixmapImagen)
                            self.etiquetaDim.setText("Las dimensiones de la imagen son: "+str(i.ancho)+" x "+str(i.alto))
                            return True
                        else:
                            print("No se encontro la imagen")
                            nombre = "Aerror"
                            ruta = "imagenes//"+nombre+".jpg"
                            pixmapImagen = QPixmap(ruta).scaled(400,400,Qt.KeepAspectRatio,Qt.SmoothTransformation)
                            self.areaImagen.setPixmap(pixmapImagen)
                            self.etiquetaDim.setText("Error, no encontramos la imagen. revise que el archivo contenga el filtro")
                            return True
                    except:
                        return False
                        
        QMessageBox.warning(self, "Error","Error, no se pudo mostrar la imagen solicitada.")

    def terminarPrograma(self):
        sys.exit()
    
    def mostrarReportes(self):
        # "Reportes//"+titulo+".html"
        nombreArchivo = "Reportes//REPORTE_TOKENS.html"
        nombreArchivo2 = "Reportes//REPORTE_ERRORES.html"
        nombreArchivo =  os.path.abspath(nombreArchivo)
        nombreArchivo2 =  os.path.abspath(nombreArchivo2)
        webbrowser.open_new_tab(nombreArchivo)
        webbrowser.open_new_tab(nombreArchivo2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ejemplo_GUI()
    GUI.show()
    sys.exit(app.exec_())
