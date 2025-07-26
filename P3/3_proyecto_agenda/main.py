import agenda

def main():
    opcion = True
    while opcion:
        agenda.borrarpantalla()
        opcion = agenda.menuprincipal()
        match opcion:
            case "1":
                agenda.agregar_contacto()
            case "2":
                agenda.mostrar_contactos()
            case "3":
                agenda.buscar_contacto()
            case "4":
                agenda.modificar_contactos()
            case "5":
                agenda.eliminar_contacto()
            case "6":
                agenda.borrarpantalla()
                print("SALISTE DEL SOFTWARE")
                opcion = False
            case _:
                print("INGRESE UN VALOR CORRECTO")
                agenda.esperartecla()

if __name__ == "__main__":
    main()
