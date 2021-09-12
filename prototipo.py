import re

def automataCadena(valor):
    print("valor a evaluar:",valor)
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

a = "tomas morales     "
b = "prueba dos #$#@#!@# 123"
c = "12"
d = "\"prueba capo\""
# print(automataCadena(a))
# print(automataCadena("\""+b+"\""))
# print(automataCadena("\""+b))
# print(automataCadena(c))
# print(automataCadena(d))
# print(automataCadena(a))
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
        #celda del eje y
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
                    print("fue aceptada")
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
