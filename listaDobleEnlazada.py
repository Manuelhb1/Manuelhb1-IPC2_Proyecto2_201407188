from nodo import Nodo

class ListaDobleEnlazada:

    def getTamanio(self):
        return self.tamanio

    def getPrimero(self):
        return self.primero  #solo regresara el nodo sin el dato

    def getUltimo(self):
        return self.ultimo #solo regresara el nodo sin el dato


    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamanio = 0
    
    #tamaño de la lista
    def vacia(self):
        return self.primero == None
    
    #funcion para ingresar datos al final de la lista
    def agregarFinal(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.tamanio += 1

    #Funcion para recorrer la lista, la recorre de inicio a fin    
    def recorrerInicio(self):
        if self.vacia():
            return "Lista vacia"
            
        aux = self.primero
        while aux:
            print(aux.dato,end="")
            aux = aux.siguiente   
        

    #Busca un elememento en la posicion indicada, el recorrido lo hace de inicio a fin    
    def buscarPosicion(self, posicion):
        aux = self.primero        
        posList = 0
        while aux:
            if posicion>(self.tamanio-1):
                return "Error indice fuera de rango" 
                            
            if posList == posicion:
                return aux.dato
            posList += 1
            aux = aux.siguiente
            
        
        