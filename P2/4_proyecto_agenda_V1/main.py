import agenda as ag

def main():
    agenda_contactos={}
    opcion=True
    while opcion:
        try:
            ag.borrarPantalla()
            print("\n\t📚  .:: SISTEMA DE GESTION DE AGENDA DE CONTACTOS ::.  📚\n" +
              "\n 1️⃣  Agregar contacto\n 2️⃣  Mostrar todos los contactos\n 3️⃣  Buscar contacto por nombre\n Modificar contactos \n Eliminar Contacto \n4️⃣ Salir 🛑")
            opcion=int(input("\n	👉 Elige una opción: (1-4) "))

            match opcion:
                case 1:
                    ag.agregar_contacto(agenda_contactos)
                case 2:
                    pass
                    ag.mostrar_contactos(agenda_contactos)
                case 3:
                    pass
                    ag.buscar_contacto(agenda_contactos)
                case 4:
                    ag.modificar_contactos(agenda_contactos)
                case 5:
                    ag.eliminar_contacto(agenda_contactos)             
                case 6:
                    print("\n\t👋 ..::SALIENDO DEL SW::.. 👋")
                    opcion=False
                case _:
                    print("⚠️  .::Escoje una opción válida::. ⚠️")    
                    ag.esperarTecla()
        except ValueError:
            print("⚠️  .::Ingrese un dato numérico::. ⚠️")
            ag.esperarTecla()




if __name__ == "__main__":
    main()