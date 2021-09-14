class archivo():
    def __init__(self,imagen):
        self.imagen = imagen

    def generar(self):
        if self.imagen.verificar():
            contenido = ""
            contenido += "<HTML>"
            contenido += f"\n<title align=\"center\"  > {self.imagen.titulo} </title>"
            contenido += "\n<head>"
            contenido += "\n<link rel=\"stylesheet\" href=\"estilo.css\" type=\"text/css\"></head>"
            contenido += "\n<body>"

            #ahora a sacar las dimensiones de cada celda.
            altoPx = self.imagen.alto/self.imagen.filas
            anchoPx = self.imagen.ancho/self.imagen.columnas
            contenido += "\n<div style=\"text-align:center;\">"
            contenido += "\n<table class=\"tablagrafica\" style=\"margin: 0 auto;\">"
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
        try:
            with open("Reportes//"+titulo+".html", 'w', encoding='utf-8') as file:
                file.write(contenido)
                print('\nSe genero el archivo correctamente\n')
        except:
            print('\nNo se generar el archivo :c\n')
                