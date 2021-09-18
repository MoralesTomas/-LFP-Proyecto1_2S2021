import imgkit
from html2image import Html2Image
hti = Html2Image()
import os

class archivo():
    def __init__(self,imagen):
        self.imagen = imagen

    def generar(self):
        if self.imagen.verificar():
            self.imagen.alto = self.imagen.alto - 1
            altoPx = self.imagen.alto/self.imagen.filas
            anchoPx = self.imagen.ancho/self.imagen.columnas
            contenido = ""
            contenido += "<HTML>"
            contenido += f"\n<title align=\"center\"  > {self.imagen.titulo} </title>"
            contenido += "\n<head>"
            contenido += "<style>body {"+"margin: 0px;}table{"+"width: "+str(self.imagen.ancho)+"px;height: "+str(self.imagen.alto)
            contenido += "px;border: 1px solid black;border-collapse: collapse;}td"+"{border: 1px solid black;width: "+str(anchoPx)+"px;height: "+str(altoPx)+"px;"+"}</style>"
            
            contenido += "\n<body>"
            contenido += "\n<table>"
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
            contenido += "\n</body>"
            contenido += "\n</html>"

            self.imagen.alto = self.imagen.alto + 1
            #aca mando el contenido
            self.escribirArchivo(self.imagen.titulo,contenido)
            self.mirrorX()
            self.mirrorY()
            self.doubleMirror()

        else:
            print("\nNo se pudo generar el arhcivo 'HTML' su archivo de entrada no contiene todo lo necesario o contiene un error.\n")

    def mirrorX(self):
        if self.imagen.filtros is not None:
            if "MIRRORX" in self.imagen.filtros:
                self.imagen.alto = self.imagen.alto - 1
                altoPx = self.imagen.alto/self.imagen.filas
                anchoPx = self.imagen.ancho/self.imagen.columnas
                contenido = ""
                contenido += "<HTML>"
                contenido += f"\n<title align=\"center\"  > {self.imagen.titulo}_MIRRORX </title>"
                contenido += "\n<head>"
                contenido += "<style>body {"+"margin: 0px;}table{"+"width: "+str(self.imagen.ancho)+"px;height: "+str(self.imagen.alto)
                contenido += "px;border: 1px solid black;border-collapse: collapse;}td"+"{border: 1px solid black;width: "+str(anchoPx)+"px;height: "+str(altoPx)+"px;"+"}</style>"
                
                #contenido += "\n<link rel=\"stylesheet\" href=\"estilo.css\" type=\"text/css\"></head>"
                contenido += "\n<body>"
                contenido += "\n<table>"
                contenido += "\n"
                for i in range(self.imagen.filas):
                    contenido += "<tr>"
                    x = self.imagen.columnas - 1
                    for a in range(self.imagen.columnas):
                        celdaTmp = self.imagen.buscarCelda(i,x)
                        if celdaTmp is not None:
                            if celdaTmp.pintar:
                                contenido += f" \n<td WIDTH=\"{anchoPx}\"  HEIGHT=\"{altoPx}\" bgcolor=\"{celdaTmp.color}\"></td>" 
                            else:
                                contenido += f" \n<td WIDTH=\"{anchoPx}\"  HEIGHT=\"{altoPx}\"></td>" 
                        x = x -1
                    contenido += "\n</tr>"
                contenido +="\n</table>"
                contenido += "\n</body>"
                contenido += "\n</html>"
                self.imagen.alto = self.imagen.alto + 1

                #aca mando el contenido
                self.escribirArchivo(self.imagen.titulo+"_MIRRORX",contenido)

            else:
                print("\nNo se pudo generar el arhcivo 'HTML' su archivo de entrada no contiene todo lo necesario o contiene un error.\n")

    def mirrorY(self):
        if self.imagen.filtros is not None:
            if "MIRRORY" in self.imagen.filtros:
                self.imagen.alto = self.imagen.alto - 1
                altoPx = self.imagen.alto/self.imagen.filas
                anchoPx = self.imagen.ancho/self.imagen.columnas
                contenido = ""
                contenido += "<HTML>"
                contenido += f"\n<title align=\"center\"  > {self.imagen.titulo}_MIRRORY </title>"
                contenido += "\n<head>"
                contenido += "<style>body {"+"margin: 0px;}table{"+"width: "+str(self.imagen.ancho)+"px;height: "+str(self.imagen.alto)
                contenido += "px;border: 1px solid black;border-collapse: collapse;}td"+"{border: 1px solid black;width: "+str(anchoPx)+"px;height: "+str(altoPx)+"px;"+"}</style>"
                
                #contenido += "\n<link rel=\"stylesheet\" href=\"estilo.css\" type=\"text/css\"></head>"
                contenido += "\n<body>"
                contenido += "\n<table >"
                contenido += "\n"
                x = self.imagen.filas - 1
                for i in range(self.imagen.filas):
                    contenido += "<tr>"
                    for a in range(self.imagen.columnas):
                        celdaTmp = self.imagen.buscarCelda(x,a)
                        if celdaTmp is not None:
                            if celdaTmp.pintar:
                                contenido += f" \n<td WIDTH=\"{anchoPx}\"  HEIGHT=\"{altoPx}\" bgcolor=\"{celdaTmp.color}\"></td>" 
                            else:
                                contenido += f" \n<td WIDTH=\"{anchoPx}\"  HEIGHT=\"{altoPx}\"></td>" 
                    x = x -1
                    contenido += "\n</tr>"
                contenido +="\n</table>"
                contenido += "\n</body>"
                contenido += "\n</html>"
                self.imagen.alto = self.imagen.alto + 1

                #aca mando el contenido
                self.escribirArchivo(self.imagen.titulo+"_MIRRORY",contenido)

            else:
                print("\nNo se pudo generar el arhcivo 'HTML' su archivo de entrada no contiene todo lo necesario o contiene un error.\n")

    def doubleMirror(self):
        if self.imagen.filtros is not None:
            if "DOUBLEMIRROR" in self.imagen.filtros:
                self.imagen.alto = self.imagen.alto - 1
                altoPx = self.imagen.alto/self.imagen.filas
                anchoPx = self.imagen.ancho/self.imagen.columnas
                contenido = ""
                contenido += "<HTML>"
                contenido += f"\n<title align=\"center\"  > {self.imagen.titulo}_DOUBLEMIRROR </title>"
                contenido += "\n<head>"
                contenido += "<style>body {"+"margin: 0px;}table{"+"width: "+str(self.imagen.ancho)+"px;height: "+str(self.imagen.alto)
                contenido += "px;border: 1px solid black;border-collapse: collapse;}td"+"{border: 1px solid black;width: "+str(anchoPx)+"px;height: "+str(altoPx)+"px;"+"}</style>"
                
                #contenido += "\n<link rel=\"stylesheet\" href=\"estilo.css\" type=\"text/css\"></head>"
                contenido += "\n<body>"
                contenido += "\n<table>"
                contenido += "\n"
                x = self.imagen.filas - 1
                for i in range(self.imagen.filas):
                    contenido += "<tr>"
                    f = self.imagen.columnas -1
                    for a in range(self.imagen.columnas):
                        celdaTmp = self.imagen.buscarCelda(x,f)
                        if celdaTmp is not None:
                            if celdaTmp.pintar:
                                contenido += f" \n<td WIDTH=\"{anchoPx}\"  HEIGHT=\"{altoPx}\" bgcolor=\"{celdaTmp.color}\"></td>" 
                            else:
                                contenido += f" \n<td WIDTH=\"{anchoPx}\"  HEIGHT=\"{altoPx}\"></td>" 
                        f = f -1
                    x = x -1
                    contenido += "\n</tr>"
                contenido +="\n</table>"
                contenido += "\n</body>"
                contenido += "\n</html>"
                self.imagen.alto = self.imagen.alto + 1

                #aca mando el contenido
                self.escribirArchivo(self.imagen.titulo+"_DOUBLEMIRROR",contenido)

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

    def escribirReporte(self,titulo,contenido):
        ruta = "Reportes//"+titulo+".html"
        try:
            with open(ruta, 'w', encoding='utf-8') as file:
                file.write(contenido)
                print('\nSe genero el archivo correctamente_Reportes\n')
                ruta = os.path.abspath(ruta)

        except:
            print('\nNo se pudo generar el archivo_Reportes :c\n')

    def generarReporte(self,titulo,listado,primerColumna):
        
        contenido = ""
        contenido += "<HTML>"
        contenido += f"\n<title align=\"center\"  > {titulo} </title>"
        contenido += "\n<head>"
        contenido += "<link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU\" crossorigin=\"anonymous\">"
            
        contenido += "\n<body>"
        contenido += "\n<table class=\"table table-success table-striped\" >"
        contenido += "\n"
        contenido += f'''
        <thead>
        <tr>
        <th scope="col">#</th>
        <th scope="col">{primerColumna}</th>
        <th scope="col">Tipo</th>
        <th scope="col">Linea</th>
        <th scope="col">columna</th>
        </tr>
        </thead>
        '''
        numero = 1
        for i in listado:
                try:
                    contenido += "<tr>"
                    contenido += f"<td>{numero}</td>"
                    numero += 1
                    if primerColumna == "Lexema":
                        contenido += f"\n<td >{i.lexema}</td>" 
                    else:
                        contenido += f"\n<td >{i.descripcion}</td>" 
                    contenido += f"\n<td>{i.tipo}</td>"
                    contenido += f"\n<td>{i.linea}</td>"
                    contenido += f"\n<td>{i.columna}</td>"
                    contenido += "\n</tr>"
                except:
                    pass
        contenido +="\n</table>"
        contenido += "\n</body>"
        contenido += "\n</html>"
        try:
            self.escribirReporte(titulo,contenido)
        except:
            return False
