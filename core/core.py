from dominio.entidades import *
from archivos.archivos import *
from procesos.menu import *
class Core:

    def __init__(self):
        self.ruta = "C:/Users/sopor/PycharmProjects/SegundoC_2/segundoK.csv"
        self.arch = ArchivoK()
        self.lista=self.arch.getAllStudents(self.ruta)
        self.obi = Procedimiento()
        self.men = MenuK()

    def start(self):
        tupla = ("Registro","Consulta","Actualizar",
                 "Eliminar","Listar","Salir")
        op = self.men.getMenu(tupla)
        if op==1:
            self.__registro()
            self.start()
        if op==2:
            self.__consulta()
            self.start()
        if op==3:
            self.__actualizar()
            self.start()
        if op==4:
            self.__eliminar()
            self.start()
        if op == 5:
            self.__listar()
            self.start()
        if op==6:
            print("Gracias por su visita...")

    def __registro(self):
        print("\t\tRegistro de estudiantes")
        cedula = input("Cedula:")
        self.lista=self.arch.getAllStudents(self.ruta)
        obj= self.obi.getValidar(cedula,self.lista)
        if obj==None:
            nombre = input("Nombre:")
            codigo = self.obi.inputInt("Codigo matricula:")
            ob1 = Estudiante(cedula,nombre,codigo)
            reg= ob1.getCedula()+";"+ob1.nombre+";"+str(ob1.getCodigo_Mat())+";\n"
            self.arch.create(self.ruta,reg,"a")
        else:
            print("Cedula ya existe!!")
        input("<Enter> para continuar...")

    def __consulta(self):
        print("Consulta de estudiantes")
        cedula = input("Cedula:")
        self.lista= self.arch.getAllStudents(self.ruta)
        obj = self.obi.getValidar(cedula,self.lista)
        if obj==None:
            print("Cedula no existe!")
        else:
            print(obj.getFields())
        input("<Enter> para continuar...")

    def __actualizar(self):
        print("\t\tActualizacion de datos.")
        cedula = input("Cedula:")
        self.lista= self.arch.getAllStudents(self.ruta)
        pos = self.obi.getPosition(cedula,self.lista)
        if pos>-1:
            print(self.lista[pos].getFields())
            nombre = input("Nombre:")
            cod = self.obi.inputInt("Codigo de matricula:")
            self.lista[pos].nombre=nombre
            self.lista[pos].setCodigo_Mat(cod)
            regs = ""
            for i in range(len(self.lista)):
                regs= regs+self.lista[i].getCedula()+";"+self.lista[i].nombre\
                      +";"+str(self.lista[i].getCodigo_Mat())+";\n"
            #print(regs)
            self.arch.create(self.ruta,regs,"w")
            print("Datos actualizados!")
        else:
            print("Estudiante no existe")
        input("<Enter> para continuar...")

    def __eliminar(self):
        print("\t\tEliminacion de datos")
        cedula = input("Cedula:")
        pos = self.obi.getPosition(cedula,self.lista)
        if pos>-1:
            print(self.lista[pos].getFields())
            input("<Enter> para eliminar Datos...")
            self.lista.pop(pos)
            regs = ""
            for i in range(len(self.lista)):
                regs = regs+self.lista[i].getCedula()+";"+self.lista[i].nombre+\
                       ";"+str(self.lista[i].getCodigo_Mat())+";\n"
            #print(regs)
            self.arch.create(self.ruta,regs,"w")
            print("Datos eliminados")
        else:
            print("Estudiante no existe..")

        input("<Enter> para continuar...")




    def __listar(self):
        print("\t\tListado de estudiantes.")
        self.lista= self.arch.getAllStudents(self.ruta)
        for i in range(len(self.lista)):
            print(self.lista[i].getData())
        input("<Enter> para continuar...")