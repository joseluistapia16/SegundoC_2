from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from vistas.processGui import *
class Registro:

    def __init__(self):
        self.cv = GuiProcess()
        self.lista=["Desarrollador","Contador","Docente","Medico","Otro"]
        self.__getWindow()
        self.__getLabels()
        self.__getInputs()
        self.__getButtons()
        #self.ven1.mainloop()

    def __getWindow(self):
        self.ven1 = Toplevel()
        self.ven1.title("Segundo K")
        self.cv.center(self.ven1,700,490)
        self.ven1.config(bg="purple")
        self.ven1.resizable(0,0)

    def __getLabels(self):
        posX = 120
        lb1 = Label(self.ven1,bg="purple",fg="white",
                    text="Registro de usuarios",font=("Arial",18)).place(
            x=220,y=20)
        lb2 = Label(self.ven1,bg="purple",fg="white",
                    text="Usuario",font=("Arial",18)).place(
            x=posX,y=100)
        lb3 = Label(self.ven1,bg="purple",fg="white",
                    text="Password",font=("Arial",18)).place(
            x=posX,y=150)
        lb4 = Label(self.ven1,bg="purple",fg="white",
                    text="Nombres",font=("Arial",18)).place(
            x=posX,y=200)
        lb5 = Label(self.ven1,bg="purple",fg="white",
                    text="Apellidos",font=("Arial",18)).place(
            x=posX,y=250)
        lb6 = Label(self.ven1,bg="purple",fg="white",
                    text="Correo",font=("Arial",18)).place(
            x=posX,y=300)
        lb7 = Label(self.ven1,bg="purple",fg="white",
                    text="Profesion",font=("Arial",18)).place(
            x=posX,y=350)


    def __getInputs(self):
        posX= 350
        self.user = Entry(self.ven1,font=("Tahoma",16),bg="#D6EAF8")
        self.user.place(x=posX,y=100,width=200,height=25)
        self.password = Entry(self.ven1,font=("Tahoma",16),bg="#D6EAF8")
        self.password.place(x=posX,y=150,width=200,height=25)
        self.nombres = Entry(self.ven1,font=("Tahoma",16),bg="#D6EAF8")
        self.nombres.place(x=posX,y=200,width=200,height=25)
        self.apellidos = Entry(self.ven1,font=("Tahoma",16),bg="#D6EAF8")
        self.apellidos.place(x=posX,y=250,width=200,height=25)
        self.correo = Entry(self.ven1,font=("Tahoma",16),bg="#D6EAF8")
        self.correo.place(x=posX,y=300,width=200,height=25)
        self.profesion= Combobox(self.ven1,state="readonly",values=self.lista)
        self.profesion.place(x=posX,y=350,width=200,height=30)

    def __getButtons(self):
        btn1 = Button(self.ven1, relief="flat",
                      text="Nuevo", bg ="green",
                      font=("Arial",11),fg="white", cursor="hand1",
                      command=self.__vaciar
                      ).place(x=570,y=30,width=110,height=25)
        self.guardar= Button(self.ven1,relief="flat",text="Guardar",
                             bg="green",font=("Arial",16),fg="white",
                             cursor="hand1",command=self.__save)
        self.guardar.place(x=200,y=420,width=110,height=40)
        self.cancelar= Button(self.ven1,relief="flat",text="Cancelar",
                             bg="green",font=("Arial",16),fg="white",
                             cursor="hand1",command=self.ven1.destroy)
        self.cancelar.place(x=360,y=420,width=110,height=40)

    def __save(self):
        messagebox.showinfo("Registro",self.user.get(),
                            parent=self.ven1)

    def __vaciar(self):
        self.user.delete(0,END)
        self.password.delete(0,END)
        self.nombres.delete(0,END)
        self.apellidos.delete(0,END)
        self.correo.delete(0,END)

# Codigo de prueba
#obr = Registro()

