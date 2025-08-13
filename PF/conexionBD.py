import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="libreria"
    )
    cursor = conexion.cursor(buffered=True)
except mysql.connector.Error as e:
    print(f"En este momento no es posible comunicarse con el sistema, inténtelo más tarde...")
    print(f"Error: {e}")