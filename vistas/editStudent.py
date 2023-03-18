from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import *
from vistas.processGui import *
from dominio.entidades import *
from dao.crudEstudiante import *

class EditStudent:

    def __init__(self,obj=None):
        self.crud = CrudStudent()
        self.cv= GuiProcess()
        self.lista = ["DESARROLLO DE SOFTWARE", "ANALISIS DE DATOS",
                      "MARKETTING", "DISEÑO GRAFICO"]
        self.__getWindow()
        self.__getFrame()
        self.__getLabels()
        self.__getInputs()
        self.__getButtons()
        print(obj.carrera)
        self.fillData(obj)
        self.ven2.mainloop()

    def __getWindow(self,titulo=None):
        self.ven2 = Toplevel()
        self.ven2.title(titulo)
        self.cv.center(self.ven2,700,490)
        self.ven2.config(bg="purple")
        self.ven2.resizable(0,0)

    def __getLabels(self):
        posX = 120
        lb1 = Label(self.marco, bg="purple", fg="white",
                    text="Actualizacion de Estudiantes", font=("Arial", 18)).place(
            x=220, y=20)
        lb2 = Label(self.marco, bg="purple", fg="white",
                    text="Cedula", font=("Arial", 18)).place(
            x=posX, y=100)
        lb3 = Label(self.marco, bg="purple", fg="white",
                    text="Nombres", font=("Arial", 18)).place(
            x=posX, y=150)
        lb4 = Label(self.marco, bg="purple", fg="white",
                    text="Apellidos", font=("Arial", 18)).place(
            x=posX, y=200)
        lb5 = Label(self.marco, bg="purple", fg="white",
                    text="Codigo matricula", font=("Arial", 18)).place(
            x=posX, y=250)
        lb6 = Label(self.marco, bg="purple", fg="white",
                    text="Correo", font=("Arial", 18)).place(
            x=posX, y=300)
        lb7 = Label(self.marco, bg="purple", fg="white",
                    text="Carrera", font=("Arial", 18)).place(
            x=posX, y=350)

    def __getInputs(self):
        posX= 350
        """ comentado
        self.validate1 = self.marco.register(self.validateId)
        self.cedula = Entry(self.marco,validate="key",
                            font=("Tahoma",16),bg="#D6EAF8",
                            validatecommand=(self.validate1,"%d","%S","%s"))
        """
        self.cedula = Entry(self.marco,
                            font=("Tahoma",16),bg="#D6EAF8")
        self.cedula.place(x=posX,y=100,width=200,height=25)
        self.nombres = Entry(self.marco,font=("Tahoma",16),bg="#D6EAF8")
        self.nombres.place(x=posX,y=150,width=200,height=25)
        self.apellidos= Entry(self.marco,font=("Tahoma",16),bg="#D6EAF8")
        self.apellidos.place(x=posX,y=200,width=200,height=25)
        self.codigo_mat = Entry(self.marco,font=("Tahoma",16),bg="#D6EAF8")
        self.codigo_mat.place(x=posX,y=250,width=200,height=25)
        self.correo = Entry(self.marco,font=("Tahoma",16),bg="#D6EAF8")
        self.correo.place(x=posX,y=300,width=200,height=25)
        self.carrera= Combobox(self.marco,state="readonly",values=self.lista)
        self.carrera.place(x=posX,y=350,width=200,height=30)

    def __getButtons(self):
        btn1 = Button(self.marco, relief="flat",
                      text="Eliminar", bg ="green",
                      font=("Arial",16),fg="white", cursor="hand1",
                      command=self.__eliminar
                      ).place(x=290,y=410,width=110,height=40)
        self.guardar= Button(self.marco,relief="flat",text="Guardar",
                             bg="green",font=("Arial",16),fg="white",
                             cursor="hand1",command=self.save)
        self.guardar.place(x=140,y=410,width=110,height=40)
        self.cancelar= Button(self.marco,relief="flat",text="Cancelar",
                             bg="green",font=("Arial",16),fg="white",
                             cursor="hand1",command=self.ven2.destroy)
        self.cancelar.place(x=430,y=410,width=110,height=40)

    def __getFrame(self):
        self.marco = Frame(self.ven2,bd=7, bg="purple")
        self.marco.pack(fill="both",expand=1)
        self.marco.config(cursor="pirate")
        self.marco.config(relief="groove")

    def __deleteFields(self):
        self.cedula.delete(0,END)
        self.nombres.delete(0,END)
        self.apellidos.delete(0,END)
        self.correo.delete(0,END)
        self.codigo_mat.delete(0,END)

    def __eliminar(self):
        datos = ("I",self.cedula.get())
        res = self.crud.deleteUser("segundok",datos)
        messagebox.showinfo("Eliminado",
                            res,parent=self.ven2)


    def save(self):
        pos = self.carrera.current()
        obj= Estudiantes(self.cedula.get(),self.nombres.get(),
                         self.apellidos.get(),self.correo.get(),
                         int(self.codigo_mat.get()),"A",
                         "JOSE33",self.lista[pos])
        print(obj.getData(), " editar")
        msg = self.__validar(obj)
        if len(msg)<1:
            tupla = (obj.nombres,obj.apellidos,
                     obj.correo,obj.carrera,obj.cedula)
            msg = self.crud.updateStudent("segundok",tupla)
            messagebox.showinfo("Actualizar",
                            msg, parent=self.ven2)
        else:
            messagebox.showerror("Error de datos",
                                 msg,parent=self.ven2)



    def validateId(self,accion,car,texto):
        if accion!='1':
            return True
        return car in "1234567890" and len(texto)<10

    def fillData(self,obj):
        self.cedula.insert(0,obj.cedula)
        self.cedula['state']='disabled'
        self.nombres.insert(0,obj.nombres)
        self.apellidos.insert(0,obj.apellidos)
        self.correo.insert(0, obj.correo)
        self.codigo_mat.insert(0,str(obj.cod_mat))
        self.codigo_mat['state']="disabled"
        name = self.getName(self.lista,obj.carrera)
        print(name, "prueba")
        self.carrera.set(name)


    def getName(self,carreras,name):
        msg = None
        print(carreras," - ",name)
        for i in range(len(carreras)):
            if name==carreras[i]:
                msg= carreras[i]
                break
        return msg

    def __validar(self, obj):
        res = ""
        if len(obj.cedula) < 10:
            res = res + "Cedula Invalida!"
        if len(obj.nombres) < 2:
            res = res + "Nombres Invalido!"
        if len(obj.apellidos) < 2:
            res = res + "Apellidos Invalidos!"
        if len(obj.correo) < 7:
            res = res + "Correo Invalido!"
        if len(str(obj.cod_mat)) < 2:
            res = res + "Codigo Invalido!"
        return res


#Codigo de prueba
#pr = NewStudent()
