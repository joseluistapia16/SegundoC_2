import mysql.connector as mc
class Conexion:

    def conecta(self,nombre):
        cone = None
        credenciales = {
            'host' : 'localhost',
            'port' : '3306',
            'user' : 'root',
            'password': '1234',
            'database': nombre
        }
        try:
           cone= mc.connect(**credenciales)
        except(mc.errors.ProgrammingError,mc.InternalError) as ex:
            print(str(ex))
        return cone

# Codigo de prueba
#cx = Conexion()
#print(cx.conecta("segundok"))