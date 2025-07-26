import mysql.connector
from mysql.connector import Error
import os

def conectar():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='bd_calificaciones'
        )
        return conexion
    except Error as e:
        print(f"❌ Error al conectar a la base de datos: {e}")
        return None


       
     
lista=[

]
calificaciones={}
def borrarpantalla():
    import os
    os.system("cls")

def esperartecla():
    input("\t 🕓 Oprima cualquier tecla para continuar ...")
    borrarpantalla()
    
def menu_principal():
    print("\n\t\t\t..::: CONSULTA DE CALIFICACIONES :::... \n\t\t..::: Sistema de Gestión de Calificaciones :::...\n\t\t\t 1️⃣  Agregar calificaciones  \n\t\t\t 2️⃣  Mostrar calificaciones \n\t\t\t 3️⃣  Calcular promedios \n\t\t\t 4️⃣  Buscar calificación \n\t\t\t 5️⃣  Salir ")
    opcion = input("\t\t\t\t 👉 Elige una opción: ").upper()
    return opcion

def agregarcalificaciones():
    borrarpantalla()
    print("👤 Agregar Calificaciones")
    nombre = input("📝 Ingresa el nombre del alumno: ").upper().strip()
    calificaciones = []
    for i in range(1, 4):
        while True:
            try:
                cal = float(input(f"📝 Ingresa la calificación {i}: "))
                if 0 <= cal <= 10:
                    calificaciones.append(cal)
                    break
                else:
                    print("❌ Ingresa un número válido entre 0 y 10")
            except ValueError:
                print("❌ Ingresa un valor numérico")

    conexion = conectar()
    if not conexion:
        return  # No se pudo conectar

    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO alumnos (nombre, cal1, cal2, cal3) VALUES (%s, %s, %s, %s)",
                       (nombre, calificaciones[0], calificaciones[1], calificaciones[2]))
        conexion.commit()
        print("✅ Alumno agregado correctamente")
    except Error as e:
        print(f"❌ Error al guardar en la base de datos: {e}")
    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()


def mostrarcalificaciones():
    borrarpantalla()
    print("\t\t📋 Mostrar calificaciones")
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, cal1, cal2, cal3 FROM alumnos")
        resultados = cursor.fetchall()
        if resultados:
            print(f"\n\t{'Nombre':<15} {'Cal 1':<10} {'Cal 2':<10} {'Cal 3':<10}")
            print(f"{'-'*60}")
            for fila in resultados:
                print(f"\t{fila[0]:<15} {fila[1]:<10} {fila[2]:<10} {fila[3]:<10}")
            print(f"{'-'*60}")
            print(f"\tTotal de alumnos: {len(resultados)}")
        else:
            print("❌ No hay calificaciones registradas")
    except Error as e:
        print(f"❌ Error al mostrar datos: {e}")


def calcularpromedios2():
    borrarpantalla()
    print("\t\t📊 Calcular Promedios")
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre, cal1, cal2, cal3 FROM alumnos")
        resultados = cursor.fetchall()
        if resultados:
            print(f"\n\t{'Alumno':<15} {'Promedio':<10}")
            print(f"{'-'*40}")
            suma_total = 0
            for fila in resultados:
                promedio = sum(fila[1:]) / 3
                suma_total += promedio
                print(f"\t{fila[0]:<15} {promedio:<10.2f}")
            promedio_grupal = suma_total / len(resultados)
            print(f"{'-'*40}")
            print(f"\tPromedio grupal: {promedio_grupal:.2f}")
        else:
            print("❌ No hay datos registrados")
    except Error as e:
        print(f"❌ Error al calcular promedios: {e}")

            
def buscarcalificacion():
    borrarpantalla()
    print("\t\t🔍 Buscar Calificación")
    nombre = input("📝 Ingresa el nombre del alumno a buscar: ").upper().strip()
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT cal1, cal2, cal3 FROM alumnos WHERE nombre = %s", (nombre,))
        resultado = cursor.fetchone()
        if resultado:
            print(f"\n\t{'Nombre':<15} {'Cal 1':<10} {'Cal 2':<10} {'Cal 3':<10}")
            print(f"{'-'*60}")
            print(f"\t{nombre:<15} {resultado[0]:<10} {resultado[1]:<10} {resultado[2]:<10}")
            promedio = sum(resultado) / 3
            print(f"\tEl promedio de {nombre} es: {promedio:.2f}")
        else:
            print("❌ Alumno no encontrado")
    except Error as e:
        print(f"❌ Error al buscar calificaciones: {e}")


    
    
        
            
           