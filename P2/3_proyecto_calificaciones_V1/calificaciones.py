import os
   

def borrarPantalla():

    os.system("cls")

def esperarTecla():
    input("Oprima cualquier tecla para continuar")
    
def menu_principal():
    COLOR_ROJO = "\033[91m"
    
    COLOR_RESET = "\033[0m" # Para resetear el color a la configuración por defecto de la terminal



    print(f"\n\t..::: 🗃️ Sistema de Gestión de Calificaciones 🗃️ :::...\n 1️⃣.- Agregar  \n 2️⃣.- Mostrar  \n 3️⃣.- Calcular Promedios  \n 4️⃣.- {COLOR_ROJO}SALIR{COLOR_RESET} ")
    opcion=input("\t👉 Elige una opción: 👈 ").upper()    
    return opcion


def agregar_Calificaciones(lista):
    borrarPantalla()
    esperarTecla()
    print("📝Agregar Calificaciones📝")
    nombre=input("📝Nombre del Alumno: ").upper().strip()
    calificaciones=[]
    for i in range(1,4):
        continua=True
        while continua:
            try:
                cal=float(input(f"Calificación {i}: "))
                if cal>=0 and cal<11:
                    calificaciones.append(cal)
                    continua=False
                else:
                    print("⚠️Ingresa un número valido⚠️")    
            except ValueError:
                print("🚫Ingresa un valor númerico🚫")
    
    lista.append([nombre]+calificaciones)
    print("💾Accion realizada con exito")
    esperarTecla()


def mostrar_Calificaciones(lista):
    borrarPantalla()
    print("📝Mostrar calificaciones:📝 ")
    if len(lista)>0:
        print(f"{'Nombre':<15}{'Calf 1':<10}{'Calf 2':<10}{'Calf 3':<10}")
        print(f"{'-'*40}")
        for fila in lista:
            print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
        print(f"{'-'*40}")
        cuantos=len(lista)
        print(f"🧑‍🏫Son {cuantos} alumnos🧑‍🏫")
        esperarTecla()

    else:

        print("⚠️No hay calificaciones registradas en el sistema⚠️")



def calcular_Promedios(lista):
    borrarPantalla()
    alumnos=0
    promedios=0
    print("Promedios📝")
    if len(lista)>0:
        
        print(f"{'Nombre':<15}{'Promedio':<10}")
        print(f"{'-'*40}")

        for fila in lista:
            promedio=(fila[1]+fila[2]+fila[3])/3

            print(f"{fila[0]:<15}{promedio:<10}")
            promedios+=promedio
            alumnos+=1
        print(f"{'-'*40}")

        promedios=promedios/alumnos
        print(f"📈Fueron {alumnos} alumnos y el promedio general fue de {promedios}")    
        esperarTecla()
    else:
        print("⚠️No hay calificaciones registradas en el sistema⚠️")

def calcular_Promedio(lista):
    borrarPantalla()
    print(".::Promedios::.")
    if len(lista)>0:
        print(f"{'Alumno':<15}{'Promedio':}")