from dominio.entidades import *
import mysql.connector as mc
from dao.conexion import *
class CrudStudent:

    def __init__(self):
        self.cone = Conexion()

    def insertStudent(self,base,datos):
        msg = ""
        try:
            con = self.cone.conecta(base)
            cursor1 = con.cursor()
            sql = "insert into estudiante(cedula,nombres,apellidos," \
                  "correo,cod_mat,carrera,id_usuario,estado) values("\
                  "%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor1.execute(sql,datos)
            con.commit()
            con.close()
            msg = "Registro exitoso "+str(cursor1.rowcount)+"(s)!"
        except(mc.errors.IntegrityError) as ex:
            msg = str(ex)
        return msg

    def getStudent(self,base,datos):
        obj= None
        try:
            con = self.cone.conecta(base)
            cursor1 = con.cursor()
            query ="select * from estudiante where cedula=%s and estado=%s"
            cursor1.execute(query,datos)
            result = cursor1.fetchall()
            con.close()
            if len(result)>0:
                obj = Estudiantes(result[0][0],result[0][1],
                      result[0][2],result[0][3],result[0][4],
                      result[0][5],result[0][6],result[0][7])
        except:
            obj=None
        return obj

    def updateStudent(self,base,datos):
        msg = ""
        try:
            con = self.cone.conecta(base)
            cursor1 = con.cursor()
            sql = "update estudiante set nombres=%s," \
                  " apellidos=%s,correo=%s,carrera=%s where cedula=%s"
            cursor1.execute(sql,datos)
            con.commit()
            con.close()
            msg = str(cursor1.rowcount)+ " actualizado con exito!"
        except(mc.errors.IntegrityError) as ex:
            msg = str(ex)
        return msg

    def deleteUser(self,base,datos):
        msg=""
        try:
            con= self.cone.conecta(base)
            cursor1= con.cursor()
            sql = "update estudiante set estado=%s where cedula=%s"
            cursor1.execute(sql,datos)
            con.commit()
            con.close()
            msg = str(cursor1.rowcount)+" eliminado con exito!"
        except(mc.errors.IntegrityError) as ex:
            msg= str(ex)
        return msg

    def getAllStudents(self,base, datos):
        lista = []
        try:
            con = self.cone.conecta(base)
            cursor1 = con.cursor()
            query = "select * from estudiante where estado=%s order by apellidos"
            cursor1.execute(query,datos)
            result = cursor1.fetchall()
            con.close()
            if len(result)>0:
                for i in range(len(result)):
                    obj = Estudiantes(result[i][0],result[i][1],
                                  result[i][2],result[i][3],
                                  result[i][4],result[i][5],
                                      result[i][6],result[i][7])
                    lista.append(obj)
        except:
            lista=[]
        return lista

# Codigo prueba



