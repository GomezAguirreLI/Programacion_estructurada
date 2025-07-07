import peliculas_dago


opcion=True
while opcion:
    peliculas_dago.borrarPantalla()
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n 1.- Agregar  \n 2.- Eliminar \n 3.- Actualizar \n 4.- Consultar \n 5.- Buscar \n 6.- Vaciar \n 7.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas_dago.agregarPeliculas()
            
        case "2":
            peliculas_dago.eliminarPeliculas()

            
        case "3":
            peliculas_dago.modificarPeliculas()
            peliculas_dago.esperarTecla() 
               
        case "4":
             peliculas_dago.consultarPeliculas()     
             peliculas_dago.esperarTecla()        
        case "5":
            peliculas_dago.buscarPeliculas()
            peliculas_dago.esperarTecla()
        
        case "6":
            peliculas_dago.vaciarPeliculas()
            peliculas_dago.esperarTecla()
        case "7":
            opcion=False
            peliculas_dago.borrarPantalla()    
            print("\n\tTerminaste la ejecucion del SW")
        case _:
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")