import imgkit
from html2image import Html2Image
hti = Html2Image()
import os

class archivo():
    def __init__(self,imagen):
        self.imagen = imagen

    def generar(self):
        if self.imagen.verificar():
            altoPx = self.imagen.alto/self.imagen.filas
            anchoPx = self.imagen.ancho/self.imagen.columnas
            contenido = ""
            contenido += "<HTML>"
            contenido += f"\n<title align=\"center\"  > {self.imagen.titulo} </title>"
            contenido += "\n<head>"
            contenido += "<style>table{"+"width: "+str(self.imagen.ancho)+"px;height: "+str(self.imagen.alto)
            contenido += "px;border: 1px solid black;border-collapse: collapse;}td"+"{border: 1px solid black;width: "+str(anchoPx)+"px;height: "+str(altoPx)+"px;"+"}</style>"
            
            #contenido += "\n<link rel=\"stylesheet\" href=\"estilo.css\" type=\"text/css\"></head>"
            contenido += "\n<body>"
            contenido += "\n<div style=\"text-align:center;\">"
            contenido += "\n<table style=\"margin: 0 auto;\">"
            contenido += "\n"
            for i in range(self.imagen.filas):
                contenido += "<tr>"
                for a in range(self.imagen.columnas):
                    celdaTmp = self.imagen.buscarCelda(i,a)
                    if celdaTmp is not None:
                        if celdaTmp.pintar:
                            contenido += f" \n<td WIDTH=\"{anchoPx}\"  HEIGHT=\"{altoPx}\" bgcolor=\"{celdaTmp.color}\"></td>" 
                        else:
                            contenido += f" \n<td WIDTH=\"{anchoPx}\"  HEIGHT=\"{altoPx}\"></td>" 
                contenido += "\n</tr>"
            contenido +="\n</table>"
            contenido += "\n<body>"
            contenido += "\n</html>"

            #aca mando el contenido
            self.escribirArchivo(self.imagen.titulo,contenido)

        else:
            print("\nNo se pudo generar el arhcivo 'HTML' su archivo de entrada no contiene todo lo necesario o contiene un error.\n")

    def escribirArchivo(self,titulo,contenido):
        ruta = "Reportes//"+titulo+".html"
        validacion = False
        try:
            with open(ruta, 'w', encoding='utf-8') as file:
                file.write(contenido)
                print('\nSe genero el archivo correctamente\n')
                ruta = os.path.abspath(ruta)
                validacion = True

        except:
            print('\nNo se pudo generar el archivo :c\n')
        # self.generarImagen(ruta,"imagenes//"+titulo+".png")
        if validacion:
            carpeta = os.path.abspath("imagenes")
            self.generarImagen(ruta,carpeta,titulo)

    def generarImagen(self,rHtml,rCarpeta,nombre):
        hti.output_path = rCarpeta
        # hti.screenshot(html_file=rHtml, css_file='Reportes\\estilo.css',save_as=nombre+".png",size=(self.imagen.ancho,self.imagen.alto))
        hti.screenshot(html_file=rHtml,save_as=nombre+".png",size=(self.imagen.ancho,self.imagen.alto))