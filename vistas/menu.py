from tkinter import *
from dominio.entidades import *
from vistas.createStudent import *
class MenuK:

    def __init__(self, obj = None):
        self.obU=None
        self.rutaI = "C:/Users/sopor/OneDrive/Imágenes/python-poo.png"
        titulo = ""
        if obj != None:
            self.obU= obj
            titulo = "Usuario:"+obj.nombre+" "+obj.apellido+"."
        self.__getWindow(titulo)
        self.__getMenu()
        self.__getImage(self.rutaI,0,0,25)


    def __getWindow(self, titulo):
        self.ven = Tk()
        self.ven.title(titulo)
        self.ven.geometry("1000x570")
        self.ven.config(bg="purple")
        self.ven.resizable(0, 0)

    def __getMenu(self):
        self.menu = Menu(self.ven)
        self.ven.config(menu = self.menu)
        #cascada
        iten1 = Menu(self.menu)
        self.menu.add_cascade(label= "Archivo", menu= iten1)
        iten1.add_command(label="Registro",command=self.__opc1)
        iten1.add_command(label= "Gestion de estudiantes")
        iten1.add_separator()
        iten1.add_command(label="Salir", command=self.__salir)
        iten2 = Menu(self.menu)
        self.menu.add_cascade(label="Ayuda", menu=iten2)
        iten2.add_command(label="About")

    def __getImage(self,ruta, x,y,tam):
        img = PhotoImage(file=ruta)
        img = img.zoom(tam)
        img = img.subsample(32)
        panel = Label(self.ven,image=img).place(x=x,y=y)
        self.ven.mainloop()

    def __opc1(self):
        NewStudent(self.obU)

    def __salir(self):
        self.ven.destroy()



#codigo de prueba

#obj = MenuK()

