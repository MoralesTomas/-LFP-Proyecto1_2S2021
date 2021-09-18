import re

class Error:
    def __init__(self, descripcion, tipo, linea, columna):
        self.descripcion = descripcion
        self.tipo = tipo
        self.linea = linea
        self.columna = columna

    def impError(self):
        print(self.descripcion, self.tipo, self.linea, self.columna, 'rojo')

class Token:
    def __init__(self, lexema, tipo,  linea, columna):
        self.lexema = lexema
        self.tipo = tipo
        self.columna = columna 
        self.linea = linea 
        
    def impToken(self):
        print(self.lexema, self.tipo, self.linea, self.columna)

class AnalizadorLexico:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []

    def analizar(self, codigo_fuente):
        self.listaTokens = []
        self.listaErrores = []

        #inicializar atributos
        linea = 1
        columna = 1
        buffer = ''
        centinela = '#'
        estado = 0
        codigo_fuente += centinela

        #automata
        i = 0
        while i< len(codigo_fuente):
            c = codigo_fuente[i]
            if estado == 0:
                if c == '=':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'igual', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '{':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'llaveAbre', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '}':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'llaveCierra', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '[':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'corcheteAbre', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ']':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'corcheteCierra', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ';':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'puntocoma', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == ',':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'coma', linea, columna))
                    buffer = ''
                    columna += 1
                elif c == '\'' or c == '"':
                    buffer += c
                    columna += 1
                    estado = 1
                elif re.search('\d', c):
                    buffer += c
                    columna += 1
                    estado = 2
                elif re.search('[A-Z]', c):
                    buffer += c
                    columna += 1
                    estado = 3
                elif c == '\n':
                    linea += 1
                    columna = 1
                elif c == " ":
                    columna += 1
                elif c == '\t':
                    columna += 1
                elif c == '\r':
                    pass
                elif c == centinela and (i+1) == len(codigo_fuente):
                    print("Se acepto el codigo fuente")
                    break
                elif c == centinela:
                    buffer += c
                    columna += 1
                    estado = 4
                elif c == "@":
                    buffer += c
                    columna += 1
                    estado = 5
                else:
                    buffer += c
                    self.listaErrores.append(Error('Caracter ' + buffer + ' no reconocido en el lenguaje.', 'Léxico', linea, columna))
                    buffer = ''
                    columna += 1
            elif estado == 1:
                if c == '\'' or c == '"':
                    buffer += c
                    self.listaTokens.append(Token(buffer, 'cadena', linea, columna))
                    buffer = ''
                    columna += 1
                    estado = 0
                elif c == '\n':
                    buffer += c
                    linea += 1
                    columna = 1
                elif c == '\r':
                    buffer += c
                else:
                    buffer += c
                    columna += 1
            elif estado == 2:
                if re.search('\d', c):
                    buffer += c
                    columna += 1
                else:
                    self.listaTokens.append(Token(buffer, 'entero', linea, columna))
                    buffer = ''
                    i -= 1
                    estado = 0
            elif estado == 3:
                if re.search('[A-Z]', c):
                    buffer += c
                    columna += 1
                else:
                    if buffer == 'TITULO':
                        self.listaTokens.append(Token(buffer, 'TITULO', linea, columna))
                    elif buffer == 'ANCHO':
                        self.listaTokens.append(Token(buffer, 'ANCHO', linea, columna))
                    elif buffer == 'ALTO':
                        self.listaTokens.append(Token(buffer, 'ALTO', linea, columna))
                    elif buffer == 'FILAS':
                        self.listaTokens.append(Token(buffer, 'FILAS', linea, columna))
                    elif buffer == 'COLUMNAS':
                        self.listaTokens.append(Token(buffer, 'COLUMNAS', linea, columna))
                    elif buffer == 'CELDAS':
                        self.listaTokens.append(Token(buffer, 'CELDAS', linea, columna))
                    elif buffer == 'FILTROS':
                        self.listaTokens.append(Token(buffer, 'FILTROS', linea, columna))
                    elif buffer == 'TRUE' or buffer == "FALSE":
                        self.listaTokens.append(Token(buffer, 'BOOLEANO', linea, columna))
                    elif buffer == 'MIRRORX' or buffer == "MIRRORY" or buffer == "DOUBLEMIRROR":
                        self.listaTokens.append(Token(buffer, 'FILTRO', linea, columna))
                    else:
                        self.listaErrores.append(Error('Cadena ' + buffer + ' no reconocida en el lenguaje.', 'Léxico', linea, columna))
                    buffer = ''
                    i -= 1
                    estado = 0
            elif estado == 4:
                if re.search('[a-fA-F0-9]', c):
                    buffer += c
                    columna += 1
                else:
                    if re.search("^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$",buffer):
                        self.listaTokens.append(Token(buffer, 'COLOR', linea, columna))
                        buffer = ''
                        i -= 1
                        estado = 0
                    else:
                        self.listaErrores.append(Error('Cadena' + buffer + ' no reconocida en el lenguaje.', 'Léxico', linea, columna))
                        buffer = ''
                        i -= 1
                        estado = 0
            elif estado == 5:
                if c == "@":
                    buffer += c
                    columna += 1
                    estado = 6 # en seis ya llevaria dos @
                else:
                    if (i+1) != len(codigo_fuente):
                        self.listaErrores.append(Error('Caracter ' + buffer + ' no reconocido en el lenguaje.', 'Léxico', linea, columna))
                    buffer = ''
                    i -= 1
                    estado = 0
            elif estado == 6:
                if c == "@":
                    buffer += c
                    columna += 1
                    estado = 7 # en seis ya llevaria 3 @
                else:
                    self.listaErrores.append(Error('Cadena ' + buffer + ' no reconocida en el lenguaje.', 'Léxico', linea, columna))
                    buffer = ''
                    i -= 1
                    estado = 0
            elif estado == 7:
                if c == "@":
                    buffer += c
                    siguiente = ""
                    if (i+1) <= len(codigo_fuente):
                        siguiente = codigo_fuente[i+1]
                    if buffer == "@@@@" and siguiente == " " or siguiente == "\n" or siguiente == "\t" or siguiente == "\r" or siguiente == "" or re.search('T|A|F|C|#', siguiente):
                        self.listaTokens.append(Token(buffer, 'SEPARADOR', linea, columna))
                        buffer = ""
                        estado = 0
                    
                    columna += 1
                else:
                    self.listaErrores.append(Error('Cadena ' + buffer + ' no reconocido en el lenguaje.', 'Léxico', linea, columna))
                    buffer = ''
                    i -= 1
                    estado = 0
            
            i += 1
    
    def impTokens(self):
        for t in self.listaTokens:
            t.impToken()

    def impErrores(self):
        if len(self.listaErrores) == 0:
            print('No hubo errores')
        else:
            for e in self.listaErrores:
                e.impError()
    def obtenerListaToken(self):
        return self.listaTokens
    def obtenerListaErrores(self):
        return self.listaErrores

def leerArchivo(ruta):
    archivo = open(ruta, 'r')
    contenido = archivo.read()
    archivo.close()
    return contenido

def escribirArchivo(ruta, contenido):
    archivo = open(ruta, 'w')
    archivo.write(contenido)
    archivo.close()

if __name__ == '__main__':
    # codigo_fuente = leerArchivo('entrada.txt')
    # scanner = AnalizadorLexico()
    # scanner.analizar(codigo_fuente)
    # scanner.impTokens()   
    cadena = "@@@@      a"
    scanner = AnalizadorLexico()
    scanner.analizar(cadena)
    scanner.impTokens()
    scanner.impErrores()