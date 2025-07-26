#Proyecto 3
#Crear un proyecto que oermita gestionar calificaciones, colocar un menu de opciones para agregar, mostrar, calcular el promedio y consultar calificaciones de un alumno.
#Notas:
#1- Utilizar funciones y llamarlas desde otro archivo.
#2- Utilizar listas (biodimensionales) para almacenar los datos (nombre y 3 calificaciones).



import calificaciones as c

def main():


    opcion = True
    while opcion:
        c.borrarpantalla()    
        opcion = c.menu_principal()
        match opcion:
            case "1":
                c.agregarcalificaciones()
                c.esperartecla()
            case "2":
                c.mostrarcalificaciones()
                c.esperartecla()
            case "3":
                c.calcularpromedios2()
                c.esperartecla()
            case "4":
                c.buscarcalificacion()
                c.esperartecla()
            case "5":
                opcion = False
                c.borrarpantalla()
                print("\n\tTerminaste la ejecucion del SW")
            case _:
                opcion=True
                c.borrarpantalla()
                input("\n\tOpción invalida vuelva a intentarlo ... por favor")
                
if __name__ == "__main__":
    main()  