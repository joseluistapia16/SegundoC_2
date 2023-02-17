class Procedimiento:
    def inputInt(self,cadena):
        num = -1
        while num < 0:
            try:
                num = int(input(cadena))
            except:
                num = -1
        return num
    def inputFloat(self,cadena):
        num = -1
        while num < 0:
            try:
                num = float(input(cadena))
            except:
                num = -1
        return num

    def imprimir(self,cadena):
        print("Impresion "+cadena)

    def saludo(self,valor):
        print("Hola "+valor+".")
        self.__privado()

    def __privado(self):
        print("Uso de metodo privado")

    def getValidar(self,id,lista):
        obj = None
        for i in range(len(lista)):
            if id==lista[i].getCedula():
               obj = lista[i]
               break
        return obj

    def getPosition(self,id,lista):
        pos = -1
        for i in range(len(lista)):
            if id == lista[i].getCedula():
               pos=i
               break
        return pos

class Persona:

    def __init__(self,p1,p2):
        self.__cedula=p1
        self.nombre = p2

    def setCedula(self,id):
        self.__cedula=id

    def getCedula(self):
        return self.__cedula

    def getData(self):
        return self.__cedula+" "+self.nombre

    def getFields(self):
        return "Cedula:"+self.__cedula + "\nNombre:" + self.nombre

class Docente(Persona):

    def __init__(self,p1,p2,p3):
        Persona.__init__(self,p1,p2)
        self.gestoria=p3

    def getData(self):
        return self.getCedula()+" "+self.nombre+" "+self.gestoria

class Estudiante(Persona,Procedimiento):

    def __init__(self,p1,p2,p3):
        Persona.__init__(self,p1,p2)
        self.__cod_mat = p3

    def setCodigo_Mat(self,codigo):
        self.__cod_mat=codigo

    def getCodigo_Mat(self):
        return self.__cod_mat

    def getData(self):
        return self.getCedula()+" "+self.nombre+\
               " "+str(self.__cod_mat)

    def getFields(self):
        return "Cedula:" + self.getCedula()+ "\nNombre:" + self.nombre+ \
               "\nCodigo Matricula:" + str(self.__cod_mat)

class Carrera:

    def __init__(self,nombre,codigo,n_docentes):
        self.nombre = nombre
        self.__cod_carrera=codigo
        self.n_docentes = n_docentes

    def setCodigo_Carrera(self,codigo):
        self.__cod_carrera=codigo

    def getCodigo_Carrera(self):
        return self.__cod_carrera

class Materia:

    def __init__(self,nombre,cod_mat,n_unidades):
        self.nombre= nombre
        self.__codigo_materia = cod_mat
        self.n_unidades= n_unidades

    def setCodigo_Materia(self,codigo):
        self.__codigo_materia=codigo

    def getCodigo_Materia(self):
        return self.__codigo_materia


class Usuario:

    def __init__(self, *param):
        self.usuario = param[0]
        self.password = param[1]
        self.nombre = param[2]
        self.apellido = param[3]
        self.correo = param[4]
        self.profesion = param[5]
        self.estado = param[6]

class Estudiantes:

    def __init__(self,*args):
        self.cedula = args[0]
        self.nombres = args[1]
        self.apellidos = args[2]
        self.correo = args[3]
        self.cod_mat = args[4]
