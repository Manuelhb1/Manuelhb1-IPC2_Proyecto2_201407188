import os
from platform import node
from matplotlib import style
from listaDobleEnlazada import ListaDobleEnlazada
import xml.etree.ElementTree as ET
from graphviz import Digraph
from datoxml import Ciudad,UnidadM,Robot
from nodo import Nodo



class ManejoArchivo:

    listCiudades = ListaDobleEnlazada()
    listRobots = ListaDobleEnlazada()

    #lista de ciudades de forma global, esto permite guardar datos de varios archivos
    def setListaCiudades(self, ciudad):        
        self.listCiudades.agregarFinal(ciudad) #Guarda la ciudad recibida en la lista dobleEnlazada  

    #Retorna las ciudades en el sistema    
    def getListaCiudades(self):
        return self.listCiudades   

    def getListaRobots(self):
        return self.listRobots     
        
    def setUMilitar(self, udsMilitar):
        self.udsMilitar = udsMilitar
    
    #retorna todas las unidades militares cargadas
    def getUMilitar(self):
        return self.udsMilitar

    #retorna la unidad militar en la coordenada buscada (fila, columna)
    def setCrdUm(self,Fil,Col):        
        comp = False

        for x  in range(self.getUMilitar().getTamanio()):   #Hay que probar 2 mapas que tengan igual numero de filas y columnas para ver cual guarda         
            if (self.getUMilitar().buscarPosicion(x).fila == Fil) and (self.getUMilitar().buscarPosicion(x).columna == Col):
                comp = True
                return [comp , self.getUMilitar().buscarPosicion(x)]
        return [comp]
        
    def manejoXML(self):        
        
        #listaCiudades = ListaDobleEnlazada()
        udsMilitar = ListaDobleEnlazada()        
        tree = ET.parse('Entrada_Ejemplo.xml')
        raiz = tree.getroot()           
        
        #en la posicion 0 de la raiz estaran la lista de ciudades
        ciudades = raiz[0]   

        #en la posicion 1 de la raiz estaran los robots
        robots = raiz[1]
                
        #guarda cada ciudad
        for i in ciudades:

            nombreCiudad = i.findtext('nombre')            
            filas = int(i[0].attrib['filas'])
            columnas = int(i[0].attrib['columnas'])

            for k in range(len(i)):

                if i[k].tag == "unidadMilitar":

                    #guardando la unidad militar                    
                    nombre = "U"
                    fila = int(i[k].attrib["fila"])
                    columna = int(i[k].attrib["columna"])
                    capacidad = int(i[k].text)                    
                    unidadMilitar = UnidadM(nombre,fila,columna,capacidad)                 
                    udsMilitar.agregarFinal(unidadMilitar)  #lista de todas los objetos unidad militar

                    self.setUMilitar(udsMilitar)                                       
            
            for x in range(len(i)):                
                filaMapa = ListaDobleEnlazada()
                
                if i[x].tag == "fila": 
                    f =  (i[x].text).strip("\"")
                   
                    for pos in range(len(f)):

                        if self.setCrdUm(x,(pos+1))[0]:
                            filaMapa.agregarFinal(self.setCrdUm(x,(pos+1))[1])
                        
                        else:                           
                            filaMapa.agregarFinal(f[pos])   #Guarda caracter por caracter en un lista, esa es la fila n
                   
                matrizMapa = ListaDobleEnlazada()
                matrizMapa.agregarFinal(filaMapa)   #Guarda cada fila en una lista/ aqui se completa las posiciones del mapa
            ciudad = Ciudad(nombreCiudad,filas,columnas,matrizMapa)

            self.setListaCiudades(ciudad) #ingresa la ciudad en el metodo set para las ciudades
    


        #print(robots[0][0].text)
        for r in robots:
            for rb in r:
                nombreR = rb.text            
                print(nombreR)
                tipoR =  rb.attrib["tipo"]#no todos tienen capacidad hay que evaluarlo
                
                if rb.attrib["tipo"] == "ChapinFighter":
                    capacidadR = rb.attrib["capacidad"]
                    robotObj =  Robot(nombreR, tipoR, capacidadR)
                    self.listRobots.agregarFinal(robotObj)
                else:
                    robotObj = Robot(nombreR, tipoR)
                    self.listRobots.agregarFinal(robotObj)
                

            







       
      

no = ManejoArchivo()

no.manejoXML()

no.getListaRobots().recorrerInicio()

