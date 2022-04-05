

class Ciudad:
    
    def __init__(self, nombre, filas, columnas, matrizMapa, listaUdMilitar, listaUdCivil, listaUdRecurso, numeroC,numeroR,numeroM,numeroE):
        self.nombre = nombre
        self.filas = filas
        self.columnas =  columnas
        self.matrizMapa = matrizMapa
        self.listaUdMilitar = listaUdMilitar
        self.listadUdCivil = listaUdCivil
        self.listaUdRecurso = listaUdRecurso
        self.numeroC = numeroC
        self.numeroR = numeroR
        self.numeroM = numeroM
        self.numeroE = numeroE


class UnidadM():
    #las posiciones empiezan en 1,1
    def __init__(self, nombre = "U", fila = None, columna = None, capacidad = None):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.capacidad = capacidad

class UnidadMilitar():
    #las posiciones empieza en 1,1
    def __init__(self, posicionX, posicionY):
        self.posicionX = posicionX
        self.posicionY = posicionY

class UnidadCivil():
    #las posiciones empiezan en 1,1
    def __init__(self, posicionX, posicionY):
        self.posicionX = posicionX
        self.posicionY = posicionY

class UnidadRecurso():
    #las posiciones empiezan en 1,1
    def __init__(self, posicionX, posicionY):
        self.posicionX = posicionX
        self.posicionY = posicionY

class UnidadEntrada():
    #las posiciones empiezan en 1,1
    def __init__(self, posicionX, posicionY):
        self.posicionX = posicionX
        self.posicionY = posicionY

        
class Robot():

    def __init__(self, nombre = "", tipo = "", capacidad = None):
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad