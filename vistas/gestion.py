from tkinter import *
from tkinter import ttk
from vistas.processGui import *
class GestionDatos:

    def __init__(self,obj = None):
        self.n_fila=[-1,-1]
        self.cv = GuiProcess()
        self.getWindow()
        self.getLabels()
        self.getInputs()
        self.getButtons()
        self.__showTable()
        self.venT.mainloop()


    def getWindow(self,titulo=None):
        self.venT = Toplevel()
        self.venT.title(titulo)
        self.cv.center(self.venT,1100,400)
        self.venT.config(bg="purple")

    def getLabels(self):
        lb1 = Label(self.venT, fg="white", bg="purple",
                    font=("Arial", 12),
                    text="Gestion de estudiantes").place(
            x=480, y=30)
        lb2 = Label(self.venT, fg="white", bg="purple",
                    font=("Arial", 12),
                    text="Cedula").place(
            x=380, y=77)


    def getInputs(self):
        self.cedula = Entry(self.venT,
                             font=("Arial", 12), fg="black",
                             bg="white")
        self.cedula.place(x=450, y=77)

    def getButtons(self):
        btn1 = Button(self.venT,relief="flat",text="Buscar",
                      bg="green",fg="black",font=("Arial",12),
                      #command=self.__logueo,
                      cursor="hand1").place(x=680,y=80,width=90,height=20)
        btn2 = Button(self.venT, relief="flat", text="Salir",
                      bg="green", fg="black", font=("Arial", 12),
                      command=self.venT.destroy,
                      cursor="hand1").place(x=580, y=350, width=90)

        btn3 = Button(self.venT, relief="flat",text="Registro",
                      bg="green",font=("Arial",11),
                     # command=self.__registro,
                      cursor="hand1").place(x=460,y=350,width=90)

    def __showTable(self,lista1=None):
        self.tabla = ttk.Treeview(self.venT,columns=(1,2,3,4,5),
                                  show="headings",height=8)
        self.tabla.bind("<1>",self.onClick)
        vsb= ttk.Scrollbar(self.venT,orient="vertical",
                           command=self.tabla.yview)
        vsb.place(x=1058,y=120,height=190)

    def onClick(self):
        pass


# Codigo de prueba
v1 = GestionDatos()