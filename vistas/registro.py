from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
class Registro:

    def __init__(self):
        self.lista=["Desarrollador","Contador","Docente","Medico","Otro"]
        self.__getWindow()
        self.__getLabels()
        self.__getInputs()
        self.__getButtons()
        #self.ven1.mainloop()

    def __getWindow(self):
        self.ven1 = Toplevel()
        self.ven1.title("Segundo K")
        self.ven1.geometry("700x490")
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
        btn1 = Button(self.ven1, relief="flat", text="Aceptar",
                      bg="orange", fg="black", font=("Arial", 12),
                      command=self.__save,
                      cursor="hand1").place(x=200, y=410, width=110,height=40)

        btn2 = Button(self.ven1, relief="flat", text="Cancelar",
                  bg="orange", fg="black", font=("Arial", 12),
                  command=self.ven1.destroy,
                  cursor="hand1").place(x=400, y=410, width=110, height=40)
    def __save(self):
        messagebox.showinfo("Registro",self.user.get(),
                            parent=self.ven1)

# Codigo de prueba
#obr = Registro()

