from conexionBD import *
import hashlib
import datetime

def hash_password(constrasena):
    return hashlib.sha256(constrasena.encode()).hexdigest()

def registrar(nombre,apellidos,email,contrasena):
    try:
        fecha=datetime.datetime.now()
        contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
        sql="INSERT INTO usuarios (nombre,apellidos,email,password,fecha) VALUES (%s,%s,%s,%s,%s)"
        val=(nombre,apellidos,email,contrasena,fecha)
        cursor.execute(sql,val)
        conexion.commit()
        return True
    except:
        return False


def iniciar_sesion(email,contrasena):
    try:
        sql="select * from usuarios where email=%s and password=%s"
        contrasena=hashlib.sha256(contrasena.encode()).hexdigest()

        val=(email,contrasena)
        cursor.execute(sql,val)
        registros=cursor.fetchone()
        if registros:
            return registros
        else:
            return None
        
    except:
        return None





