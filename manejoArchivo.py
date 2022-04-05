import os
from platform import node
from matplotlib import style
from listaDobleEnlazada import ListaDobleEnlazada
import xml.etree.ElementTree as ET
from graphviz import Digraph
from datoxml import Ciudad,UnidadM,Robot,UnidadCivil,UnidadMilitar,UnidadRecurso
from nodo import Nodo



class ManejoArchivo:

    listCiudades = ListaDobleEnlazada()
    listRobots = ListaDobleEnlazada()

    def getCiudadActual(self, nombre="", num=0):

        if nombre != "":

            for ciudadN in self.getListaCiudades():
                if ciudadN.nombre == nombre:
                    return ciudadN
        
        elif num != 0:            
            return self.getListaCiudades().buscarPosicion(num-1)

        else:
            return "Ciudad no encontrada"

            
    def getUnidadMltrActual(self, posx, posy):
        return True

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
        
      
        udsMilitar = ListaDobleEnlazada()        
        tree = ET.parse('Entrada_Ejemplo.xml')
        raiz = tree.getroot()           
        
        #en la posicion 0 de la raiz estaran la lista de ciudades
        ciudades = raiz[0]   

        #en la posicion 1 de la raiz estaran los robots
        robots = raiz[1]
                
        #guarda cada ciudad
        for i in ciudades:
            
            #llevaran el control de cuantas unidades civiles, miliares y de recursos hay en cada ciudad, con su respectiva posicion x,y
            listaDeUnidadesMilitar = ListaDobleEnlazada()
            listaDeUnidadesRecurso = ListaDobleEnlazada()
            listaDeUnidadesCivil = ListaDobleEnlazada()
            listaDeUnidadesEntrada = ListaDobleEnlazada()
            #numero de unidades segun su tipo en la ciudad
            nUndsMilitar = 0
            nUndsRecurso = 0
            nUndsCivil = 0
            nUndsEntrada = 0

            nombreCiudad = i.findtext('nombre') #Para evaluar si una ciudad ya existe podemos buscar en los nombres y si ya existe no guardar la ciudad

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
                    
                    unMilitar = UnidadMilitar(fila,columna)
                    listaDeUnidadesMilitar.agregarFinal(unMilitar)
                    self.setUMilitar(udsMilitar)   
                                                       
            
            for x in range(len(i)):                
                filaMapa = ListaDobleEnlazada()
                
                if i[x].tag == "fila": 
                    f =  (i[x].text).strip("\"")
                   
                    for pos in range(len(f)):

                        if self.setCrdUm(x,(pos+1))[0]:
                            filaMapa.agregarFinal(self.setCrdUm(x,(pos+1))[1]) 
                            nUndsMilitar += 1      

                        else: 

                            #numero de unidades en cadaciudad por tipo
                            if f[pos] == "E":                               
                                nUndsEntrada += 1
                            elif f[pos] == "C":
                                nUndsCivil += 1
                            elif f[pos] == "R":
                                nUndsRecurso +=1

                            filaMapa.agregarFinal(f[pos])   #Guarda caracter por caracter en un lista, esa es la fila n
                   
                matrizMapa = ListaDobleEnlazada()
                matrizMapa.agregarFinal(filaMapa)   #Guarda cada fila en una lista/ aqui se completa las posiciones del mapa
            ciudad = Ciudad(nombreCiudad,filas,columnas,matrizMapa,listaDeUnidadesMilitar,nUndsCivil,nUndsRecurso,nUndsMilitar,nUndsEntrada)

            self.setListaCiudades(ciudad) #ingresa la ciudad en el metodo set para las ciudades    

        for r in robots:
            for rb in r:
                nombreR = rb.text            
                print(nombreR)
                tipoR =  rb.attrib["tipo"]
                
                if rb.attrib["tipo"] == "ChapinFighter":
                    capacidadR = rb.attrib["capacidad"]
                    robotObj =  Robot(nombreR, tipoR, capacidadR)
                    self.listRobots.agregarFinal(robotObj)
                else:
                    robotObj = Robot(nombreR, tipoR)
                    self.listRobots.agregarFinal(robotObj)
                
    def misionRescate(self, entrada, robot, unidadARescatar):
        print("dkdkd")
            







       
      

# no = ManejoArchivo()

# no.manejoXML()

# no.getListaRobots().recorrerInicio()

