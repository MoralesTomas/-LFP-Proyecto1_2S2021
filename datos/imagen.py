class imagen():
    def __init__(self,datos):
        self.datos = datos
        self.titulo = "titulo no encontrado"
        self.ancho = None
        self.alto = None
        self.filas = None
        self.columnas = None
        self.celdas = None
        self.filtros = None
    
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
        print("CELDAS",self.celdas)
