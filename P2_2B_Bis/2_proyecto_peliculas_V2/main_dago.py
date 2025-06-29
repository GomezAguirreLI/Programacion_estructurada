import peliculas_dago


opcion=True
while opcion:
    peliculas_dago.borrarPantalla()
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n 1.- Crear  \n 2.- Borrar \n 3.- Mostrar \n 4.- Agregar Caracteristicas \n 5.- Modificar caracteristicas \n 6.- Borrar Caracteristicas \n 7.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas_dago.crearPeliculas()
            
        case "2":
            peliculas_dago.borrarPeliculas()

            
        case "3":
            peliculas_dago.mostrarPeliculas()
            peliculas_dago.esperarTecla() 
               
        case "4":
             peliculas_dago.agregarCaracteristicaPeliculas()     
             peliculas_dago.esperarTecla()        
        case "5":
            peliculas_dago.modificarCaracteristicaPeliculas()
            peliculas_dago.esperarTecla()
        
        case "6":
            peliculas_dago.borrarCaracteristicaPeliculas()
            peliculas_dago.esperarTecla()
        case "7":
            opcion=False
            peliculas_dago.borrarPantalla()    
            print("\n\tTerminaste la ejecucion del SW")
        case _:
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")