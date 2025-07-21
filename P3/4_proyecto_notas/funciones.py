def borrarPantallas():
    import os
    os.system("cls")


def esperarTecla():
    input("\n\\---⚠️Oprima cualquer tecla para continuar⚠️---")    
   
def menu_principal():
    COLOR_ROJO = "\033[91m"
    
    COLOR_RESET = "\033[0m" # Para resetear el color a la configuración por defecto de la terminal



    print(f"\n\t..::: 🗃️ Sistema de Gestión de Notas 🗃️ :::...\n 1️⃣.- Ingresar  \n 2️⃣.- Registro   \n 3️⃣.- {COLOR_ROJO}SALIR{COLOR_RESET} ")
    opcion=input("\t👉 Elige una opción: 👈 ").upper()    
    return opcion
