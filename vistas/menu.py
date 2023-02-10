from tkinter import *
from dominio.entidades import *
class MenuK:

    def __init__(self, obj = None):
        titulo = ""
        if obj != None:
            titulo = "Usuario:"+obj.nombre+" "+obj.apellido+"."

        self.__getWindow(titulo)
        self.__getMenu()
        self.ven.mainloop()

    def __getWindow(self, titulo):
        self.ven = Tk()
        self.ven.title(titulo)
        self.ven.geometry("700x490")
        self.ven.config(bg="purple")
        self.ven.resizable(0, 0)

    def __getMenu(self):
        self.menu = Menu(self.ven)
        self.ven.config(menu = self.menu)
        #cascada
        iten1 = Menu(self.menu)
        self.menu.add_cascade(label= "archivo", menu= iten1)
        iten1.add_command(label="Registro")
        iten1.add_command(label= "Gestion de estudiantes")
        iten1.add_separator()
        iten1.add_command(label="Salir", command=self.__salir)
        iten2 = Menu(self.menu)
        self.menu.add_cascade(label="Ayuda", menu=iten2)
        iten2.add_command(label="About")

    def __salir(self):
        self.ven.destroy()



#codigo de prueba

#obj = MenuK()

