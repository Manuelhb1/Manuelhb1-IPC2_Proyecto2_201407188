

class Ciudad:
    
    def __init__(self, nombre, filas, columnas, matrizMapa):
        self.nombre = nombre
        self.filas = filas
        self.columnas =  columnas
        self.matrizMapa = matrizMapa


class UnidadM():
    
    def __init__(self, nombre = "U", fila = None, columna = None, capacidad = None):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.capacidad = capacidad


class Robot():

    def __init__(self, nombre = "", tipo = "", capacidad = None):
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad