class celda():
    def __init__(self,dato):
        self.dato = dato
        self.fila = None
        self.columna = None
        self.pintar = None
        self.color = None
    
    def splitear(self,contenido,caracter):
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

    def autoLlenado(self):
        a = self.dato
        a = a.replace("[", "")
        a = a.replace("]", "")
        lista = self.splitear(a,",")
        try:
            #comentado donde el primero es la columna y el segundo es la fila
            self.columna = int(lista[0])
            self.fila = int(lista[1])
            self.pintar = lista[2]
            if self.pintar.strip() == "FALSE":
                self.pintar = False
            else:
                self.pintar = True
            self.color = lista[3]
            #print("se genero una nueva celda",self.fila,self.columna,self.color)
        except:
            pass
