
#Proyecto 3

#Crear un proyecto que permita gestionar gestionar(administrar)calificaciones, colocar un menu de opciones para agregar,mostrar,calcular promedio de un estudiante,


#Notas.
#1.-Utilizar funciones y mandar llamar desde otro archivo(modulos)
#2.-Utilizar list(bidimensional)para almacenar el nombre del alumno como sus tres calificaciones




import calificaciones

def main():
    datos=[]

    opcion=True
    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menu_principal()

        match opcion:
            case "1":

                calificaciones.agregar_Calificaciones(datos)
                
            case "2":
                calificaciones.mostrar_Calificaciones(datos)
                
            case "3":           
                calificaciones.calcular_Promedio(datos)
                

            case "4":
                opcion=False
                calificaciones.borrarPantalla()    
                print("\n\t👋Terminaste la ejecucion del SW👋")
            case _:
                input("\n\t⚠️Opción invalida vuelva a intentarlo ... por favor⚠️ ")



if __name__ == "__main__":
    main()              