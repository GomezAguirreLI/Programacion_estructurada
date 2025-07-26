import mysql.connector
from mysql.connector import Error
import os

def conectar():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',  
            database='bd_agenda'  
        )
        return conexion
    except Error as e:
        print(f"Error al conectar con MySQL: {e}")
        return None

def borrarpantalla():
    os.system("cls" if os.name == "nt" else "clear")

def esperartecla():
    input("\t 🕓 Oprima cualquier tecla para continuar ...")
    borrarpantalla()

def menuprincipal():
    opcion = input("\n\t\t..:::Sistema de Gestion de Agenda de Contactos:::..\n\n"
                   "\t\t 1️⃣  Agendar contacto \n\t\t 2️⃣  Mostrar contactos \n\t\t 3️⃣  Buscar contactos por nombre \n"
                   "\t\t 4️⃣  Modificar contactos \n\t\t 5️⃣  Eliminar contacto \n\t\t 6️⃣ Salir \n\n"
                   "\t\t 👉  Elige una opción (1-6): ")
    return opcion

def agregar_contacto():
    borrarpantalla()
    conexion = conectar()
    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        esperartecla()
        return

    nombre = input("\n\t\t Nombre del contacto ").upper().strip()
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre FROM usuarios WHERE nombre = %s", (nombre,))
    if cursor.fetchone():
        print("\n\t\t CONTACTO YA EXISTENTE")
        conexion.close()
        esperartecla()
        return

    telefono = input("\n\t\t Telefono del contacto ").strip()
    email = input("\n\t\t Email del contacto ").lower().strip()

    cursor.execute("INSERT INTO usuarios (nombre, telefono, email) VALUES (%s, %s, %s)",
                   (nombre, telefono, email))
    conexion.commit()
    conexion.close()
    print("\n\t\t ACCION REALIZADA CON EXITO")
    esperartecla()

def mostrar_contactos():
    borrarpantalla()
    conexion = conectar()
    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        esperartecla()
        return

    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, telefono, email FROM contactos ORDER BY nombre")
    resultados = cursor.fetchall()
    if not resultados:
        print("\n\t\t NO EXISTEN CONTACTOS ")
    else:
        for nombre, telefono, email in resultados:
            print(f"\n\tNombre: {nombre} \n\tTelefono: {telefono} \n\tEmail: {email}")
    conexion.close()
    esperartecla()

def buscar_contacto():
    borrarpantalla()
    conexion = conectar()
    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        esperartecla()
        return

    nombre = input("Ingresa el nombre del contacto a buscar: ").upper().strip()
    cursor = conexion.cursor()
    cursor.execute("SELECT telefono, email FROM contactos WHERE nombre = %s", (nombre,))
    resultado = cursor.fetchone()
    if resultado:
        telefono, email = resultado
        print(f"\n\tNombre: {nombre} \n\tTeléfono: {telefono} \n\tEmail: {email}")
    else:
        print(f"\n\t \u274C No se encontró el contacto '{nombre}' \u274C")
    conexion.close()
    esperartecla()

def modificar_contactos():
    borrarpantalla()
    conexion = conectar()
    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        esperartecla()
        return

    print("\n\t\t \U0001F501 .::Modificar Contactos::. \U0001F501")
    nombre = input("Ingresa el nombre del contacto que desea modificar: ").upper().strip()

    cursor = conexion.cursor()
    cursor.execute("SELECT telefono, email FROM contactos WHERE nombre = %s", (nombre,))
    resultado = cursor.fetchone()
    if not resultado:
        print(f"\n\t \u274C No se encontro un contacto con el nombre {nombre} para modificar \u274C")
        conexion.close()
        esperartecla()
        return

    telefono_actual, email_actual = resultado
    print(f"El contacto actual es: \n\t{nombre} \n\ttelefono: {telefono_actual}\n\tE-mail: {email_actual}")

    tel = input("Ingrese el nuevo numero de telefono: ").strip()
    mail = input("Ingrese el nuevo e-mail: ").strip().lower()

    cursor.execute("UPDATE contactos SET telefono=%s, email=%s WHERE nombre=%s", (tel, mail, nombre))
    conexion.commit()
    conexion.close()
    print("\n\t\t CONTACTO MODIFICADO CON EXITO")
    esperartecla()

def eliminar_contacto():
    borrarpantalla()
    conexion = conectar()
    if conexion is None:
        print("No se pudo conectar a la base de datos.")
        esperartecla()
        return

    conta_eliminar = input("Ingresa el nombre del contacto que deseas eliminar: ").upper().strip()
    cursor = conexion.cursor()
    cursor.execute("SELECT telefono, email FROM contactos WHERE nombre = %s", (conta_eliminar,))
    resultado = cursor.fetchone()
    if not resultado:
        print(f"\n\t \u274C No se encontró un contacto con el nombre {conta_eliminar} \u274C")
        conexion.close()
        esperartecla()
        return

    telefono, email = resultado
    print(f"El contacto actual es: \n\t{conta_eliminar} \n\ttelefono: {telefono}\n\tE-mail: {email}")

    confirmar = ""
    while confirmar != "si" and confirmar != "no":
        confirmar = input("¿Estás seguro que deseas eliminar este contacto? (Si/No): ").lower().strip()
        if confirmar != "si" and confirmar != "no":
            print("\n\t\t \u274C Respuesta inválida. Por favor escribe 'Si' o 'No' \u274C")

    if confirmar == "si":
        cursor.execute("DELETE FROM contactos WHERE nombre = %s", (conta_eliminar,))
        conexion.commit()
        print(f"\n\t \u2705 El contacto '{conta_eliminar}' ha sido eliminado exitosamente. \u2705")

    conexion.close()
    esperartecla()
