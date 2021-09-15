from datos.celda import celda

class imagen():
    def __init__(self,datos):
        self.datos = datos #texto
        self.titulo = "titulo no encontrado"
        self.ancho = None
        self.alto = None
        self.filas = None
        self.columnas = None
        self.celdas = None #solo es texto . completo {[[][][]]}
        self.filtros = None
        self.listadoCeldas = None
    
    def verificar(self):
        if self.datos is not None:
            if self.ancho is not None:
                if self.alto is not None:
                    if self.filas is not None:
                        if self.columnas is not None:
                            if self.celdas is not None:
                                return True
        return False

    def mostrarDatos(self):
        print("------------------------------------------------------")
        print("TITULO",self.titulo)
        print("ANCHO",self.ancho)
        print("ALTO",self.alto)
        print("FILAS",self.filas)
        print("COLUMNAS",self.columnas)
        print("FILTROS",self.filtros)

    def quitarSaltos(self,contenido):
        actual = ""
        for i in contenido:
            if i !="\n" and i !="\t" and i !=" ":
                actual += i
        return actual

    def automataCorchete(self,celdas):
        actual = ""
        estado = 0
        lista = []
        for i in celdas:
            if estado == 0:
                if i =="]":
                    estado =1
                    actual += "]"
                    continue
                else:
                    actual += i
                    continue
            if estado == 1:
                if i ==",":
                    lista.append(actual)
                    actual = ""
                    estado = 0
                    continue
        lista.append(actual)
        return lista

    def autoLlenado(self):
        #en dato voy a mandar lo de las llaves{}
        actual = self.celdas
        actual = actual.strip()
        actual = actual.replace("{", "")
        actual = actual.replace("}", "")
        actual = actual.strip()
        actual = self.quitarSaltos(actual)
        #hasta aca ya tenemos todo por corchetes y comas.
        lista = self.automataCorchete(actual)
        lCeldas = []
        for i in lista:
            try:
                nuevo = celda(i)
                nuevo.autoLlenado()
                lCeldas.append(nuevo)
            except:
                pass
        self.listadoCeldas = lCeldas

    def mostrarListado(self):
        print("============================ sus celdas son =========================")
        contador = 1
        for i in self.listadoCeldas:
            print(f"------Celda #{contador}------")
            print(">>>>fila",i.fila)
            print(">>>>columna",i.columna)
            print(">>>>pintar",i.pintar)
            print(">>>>color",i.color)
            contador += 1

    def buscarCelda(self,fila,columna):
        listado = self.listadoCeldas
        for i in listado:
            try:
                if i.fila == fila and i.columna == columna:
                    return i
            except:
                pass
        if fila <= self.filas and columna <= self.columnas:
            #[0,1,FALSE,#000000]
            nuevo = celda(f"[{columna},{fila},FALSE,#FFFFFF]")
            nuevo.autoLlenado()
            self.listadoCeldas.append(nuevo)
            return nuevo
        else:
            #en caso de que la fila y columna buscada no existan y exceda los limites de filas y columnas solicitadas
            return None
    
    
