import mysql.connector
#from mysql.connector import Error
#muestra cuales son los errores que pasan 

try:
    conexion=mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="bd_notas"
    )
    cursos=conexion.cursor(buffered=True)
    #buffered mantiene el cursor abierto 
except :
    print(f"... ⚠️ En este momento no es posible comunicarse con el sistema, intentelo mas tarde ⚠️ ....")    
    