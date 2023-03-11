from tkinter import *
from tkinter import messagebox
from vistas.menu import *
from dominio.entidades import *
from vistas.registro import *
from vistas.processGui import *
from dao.crudUsuario import *
class LoginK:

    def __init__(self):
        self.crud = CrudUser()
        self.wc=GuiProcess()
        self.__getWindow()
        self.__getLabels()
        self.__getInputs()
        self.__getButtons()
        self.ven.mainloop()


    def __getWindow(self):
        self.ven= Tk()
        self.ven.title("Segundo K")
        self.wc.center(self.ven,400,300)
        #self.ven.geometry("400x300")
        self.ven.config(bg="purple")
        self.ven.resizable(0,0)


    def __getLabels(self):
        lb1 = Label(self.ven, fg="white", bg="purple",
                    font=("Tahoma", 20),
                    text="Usuario").place(
            x=150, y=50
        )

        lb2 = Label(self.ven, fg="white", bg="purple",
                    font=("Arial", 20), text="Password").place(
            x=140, y=130
        )

    def __getInputs(self):
        self.usuario = Entry(self.ven,
            font=("Arial",20),fg="red",
                bg="white")
        self.usuario.place(x=120,y=100,
                          width=160, height=30)
        self.clave=Entry(self.ven,font=("Arial",20),fg="red",
                         bg="white",show="*")
        self.clave.place(x=120, y=180, width=160, height=30)


    def __getButtons(self):
        btn1 = Button(self.ven,relief="flat",text="Aceptar",
                      bg="orange",fg="black",font=("Arial",12),
                      command=self.__logueo,
                      cursor="hand1").place(x=110,y=235,width=90)
        btn2 = Button(self.ven, relief="flat", text="Cancelar",
                      bg="orange", fg="black", font=("Arial", 12),
                      command=self.ven.destroy,
                      cursor="hand1").place(x=210, y=235, width=90)

        btn3 = Button(self.ven, relief="flat",text="Registrar",
                      bg="green",font=("Arial",11),
                      command=self.__registro,
                      cursor="hand1").place(x=300,y=20,width=90,height=20)

    def __logueo(self):
        usu = self.usuario.get()
        pas1 = self.clave.get()
        datos=(usu,pas1,"A")
        obj = self.crud.getLoggin("segundok",datos)
        if obj!=None:
           self.ven.destroy()
           obk1 = MenuK(obj)
        else:
            messagebox.showinfo("Advertencia","Credenciales invalidas!",
                                parent=self.ven)

    def __registro(self):
        obr= Registro()






prb = LoginK()
