from conexionBD import *
import datetime
def crear(usuario_id,titulo,descripcion):
    try:
        sql="insert into notas (usuario_id,titulo,descripcion,fecha) values(%s ,%s , %s, NOW())"
        val=(usuario_id,titulo,descripcion)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except:
        return False
    
def mostrar(usuario_id):
    try:
        sql="select * from notas where usuario_id=%s"
        val=(usuario_id,)
        cursor.execute(sql, val)
        return cursor.fetchall()
    except:
        return []

def cambiar(id,titulo,descripcion):
    try:
        sql="UPDATE notas SET titulo=%s, descripcion=%s, fecha=NOW() WHERE id=%s"
        val=(titulo,descripcion,id)
        cursor.execute(sql,val)
        conexion.commit()  
        return True
    except:
        return False
    
def eliminar(id):
    try:
        sql="delete from notas where id=%s "
        val=(id,)
        cursor.execute(sql, val)
        conexion.commit()  
        return True
    except:
        return False
                       
    