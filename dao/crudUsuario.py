from dominio.entidades import *
import mysql.connector as mc
from dao.conexion import *
class CrudUser:

    def __init__(self):
        self.cone = Conexion()

    def insertUser(self,base,datos):
        msg = ""
        try:
            con = self.cone.conecta(base)
            cursor1 = con.cursor()
            sql = "insert into usuario(usuario,password,nombres," \
                  "apellidos,correo, profesion,estado) values("\
                  "%s,%s,%s,%s,%s,%s,%s)"
            cursor1.execute(sql,datos)
            con.commit()
            con.close()
            msg = "Registro exitoso "+str(cursor1.rowcount)+"(s)!"
        except(mc.errors.IntegrityError) as ex:
            msg = str(ex)
        return msg

    def getUser(self,base,datos):
        obj= None
        try:
            con = self.cone.conecta(base)
            cursor1 = con.cursor()
            query ="select * from usuario where usuario=%s"
            cursor1.execute(query,datos)
            result = cursor1.fetchall()
            con.close()
            if len(result)>0:
                obj = Usuario(result[0][0],result[0][1],
                      result[0][2],result[0][3],result[0][4],
                      result[0][5],result[0][6])
        except:
            obj=None
        return obj

    def getLoggin(self,base,datos):
        obj= None
        try:
            con = self.cone.conecta(base)
            cursor1 = con.cursor()
            query = "select * from usuario where usuario=%s and password=%s and estado=%s"
            cursor1.execute(query,datos)
            result = cursor1.fetchall()
            con.close()
            if len(result)>0:
                obj = Usuario(result[0][0],result[0][1],result[0][2],
                              result[0][3],result[0][4],result[0][5],result[0][6])
        except:
            obj =None
        return obj

    def updateUser(self,base,datos):
        msg = ""
        try:
            con = self.cone.conecta(base)
            cursor1 = con.cursor()
            sql = "update usuario set password=%s,nombres=%s," \
                  " apellidos=%s,correo=%s, profesion=%s where usuario=%s"
            cursor1.execute(sql,datos)
            con.commit()
            con.close()
            msg = str(cursor1.rowcount)+ " actualizado con exito!"
        except(mc.errors.IntegrityError) as ex:
            msg = str(ex)
        return msg

    def removeUser(self,base,datos):
        msg = ""
        try:
            con = self.cone.conecta(base)
            cursor1= con.cursor()
            sql = "delete from usuario where usuario=%s"
            cursor1.execute(sql,datos)
            con.commit()
            con.close()
            msg = str(cursor1.rowcount)+" registro eliminado permanentemente!"
        except(mc.errors.IntegrityError) as ex:
            msg=str(ex)
        return msg

    def deleteUser(self,base,datos):
        msg=""
        try:
            con= self.cone.conecta(base)
            cursor1= con.cursor()
            sql = "update usuario set estado=%s where usuario=%s"
            cursor1.execute(sql,datos)
            con.commit()
            con.close()
            msg = str(cursor1.rowcount)+" eliminado con exito!"
        except(mc.errors.IntegrityError) as ex:
            msg= str(ex)
        return msg

    def getAllUsers(self,base, datos):
        lista = []
        try:
            con = self.cone.conecta(base)
            cursor1 = con.cursor()
            query = "select * from usuario where estado=%s order by usuario"
            cursor1.execute(query,datos)
            result = cursor1.fetchall()
            con.close()
            if len(result)>0:
                for i in range(len(result)):
                    obj = Usuario(result[i][0],result[i][1],
                                  result[i][2],result[i][3],
                                  result[i][4],result[i][5],
                                  result[i][6])
                    lista.append(obj)
        except:
            lista=[]
        return lista





# Codigo de prueba
#crud = CrudUser()
#datos = ("arteaga13","3333","VALESKA","ARTEAGA","brithany@hotmail.com",
#        "DESARROLLADORA","A")
#print(crud.insertUser("segundok",datos))
#datos =("ariel23",)
#obj = crud.getUser("segundok",datos)
#if obj!=None:
#    print(obj.usuario+" "+obj.nombre+" "+obj.apellido+" "+obj.correo)
#else:
#    print("Usuario no existe!")
""" 
datos = ("I","arteaga13")
print(crud.deleteUser("segundok",datos))

datos = ("arteaga13",)
print(crud.removeUser("segundok",datos))
datos = ("A",)
lista = crud.getAllUsers("segundok",datos)
for i in range(len(lista)):
    print(lista[i].usuario+" "+lista[i].nombre+" "+lista[i].apellido)

datos = ("erick23","55555","A")
obj = crud.getLoggin("segundok",datos)
if obj!=None:
    print(obj.usuario+" "+obj.password+" "+obj.apellido)
else:
    print("Credenciales invalidas!")

datos = ("12345","CAMILA NICOLE","BRIONES PAREDES","paredes@hotmail.com",
         "ABOGADA","arteaga13")
print(crud.updateUser("segundok",datos))
"""



