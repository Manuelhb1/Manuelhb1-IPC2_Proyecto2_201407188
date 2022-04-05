from manejoArchivo import ManejoArchivo


class Control:

    def inicio():
       
        salirMenu = True
        entradaArchivo = True

        print("\n")
        print(f"{'':<5}{'+-------------------------------------------+':<40}\n{'':<5}{'|':<4}{'Selecciona una opcion':<40}|\n{'':<5}{'|':<4}{'':<40}|\n{'':<5}{'|':<4}{'1 Cargar archivo de configuracion':<40}|\n{'':<5}{'|':<4}{'2 Realizar una mision':<40}|\n{'':<5}{'|':<4}{'3 Ver ciudades cargadas en sistema':<40}|\n{'':<5}{'|':<4}{'4 Salir':<40}|\n{'':<5}{'+-------------------------------------------+':<40}\n")                  
        
        while salirMenu:            
        
            entrada = int(input("Ingresa una opcion:  " ))
            print("")
        
            if entrada == 1:
                entradaMision = input("Selecciona un tipo de mision: ")
                if (entradaMision.isdigit()==True and entradaMision=="1") or (entradaMision == "Mision de rescate"):
                    print("mision de rescate")#Debe pedir ciudad, entrada, robot, unidad a rescatar

                    

                            
            elif entrada == 2:
                pass                
        
            elif entrada == 3:                
                pass
                       
            elif entrada == 4:
                print("Saliendo...")
                print("\n\n\n")
                salirMenu = False
                exit()
            entrada = 0
    inicio()