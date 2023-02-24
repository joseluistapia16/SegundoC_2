from tkinter import *
from tkinter import ttk
from vistas.processGui import *
from dominio.entidades import *
from vistas.createStudent import *
from procesos.procesos import *
class GestionDatos:

    def __init__(self,obj = None):
        self.clk =0
        self.cad = Cadenas()
        self.obU = obj
        self.n_fila=[-1,-1]
        self.cv = GuiProcess()
        self.datos = []
        #Generar datos
        self.datos= self.fillList()
        #*********
        self.getWindow()
        self.getLabels()
        self.getInputs()
        self.getButtons()
        self.__showTable(self.datos)
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
        self.validate1 = self.venT.register(self.validateId)
        self.cedula = Entry(self.venT, validate="key",
                             font=("Arial", 12), fg="black",
                             bg="white",
                            validatecommand=(self.validate1,"%d","%S","%s"))
        self.cedula.place(x=450, y=77)

    def getButtons(self):
        btn1 = Button(self.venT,relief="flat",text="Buscar",
                      bg="green",fg="black",font=("Arial",12),
                      command=self.getFilter,
                      cursor="hand1").place(x=680,y=80,width=90,height=20)
        btn2 = Button(self.venT, relief="flat", text="Salir",
                      bg="green", fg="black", font=("Arial", 12),
                      command=self.venT.destroy,
                      cursor="hand1").place(x=580, y=350, width=90)

        btn3 = Button(self.venT, relief="flat",text="Registro",
                      bg="green",font=("Arial",11),
                     command=self.reg1,
                      cursor="hand1").place(x=460,y=350,width=90)

    def __showTable(self,lista1=None):
        self.tabla = ttk.Treeview(self.venT,columns=(1,2,3,4,5),
                                  show="headings",height=8)
        self.tabla.bind("<1>",self.onClick)
        vsb= ttk.Scrollbar(self.venT,orient="vertical",
                           command=self.tabla.yview)
        vsb.place(x=1058,y=120,height=190)
        self.tabla.configure(yscrollcommand=vsb.set)
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("Treeview.Headings",bg="red")
        #Columna
        self.tabla.heading(1,text="ID")
        self.tabla.heading(2,text="Cedula")
        self.tabla.heading(3,text="Nombre")
        self.tabla.heading(4,text="Apellido")
        self.tabla.heading(5,text="Correo")
        self.tabla.column(1,anchor=CENTER)
        self.tabla.column(2,anchor=CENTER)
        self.tabla.column(3,anchor=CENTER)
        self.tabla.column(4,anchor=CENTER)
        self.tabla.column(5,anchor=CENTER)
        for x in range(len(lista1)):
            self.tabla.insert("","end"
                ,values=(str(x+1),
                lista1[x].cedula,
                lista1[x].nombres,lista1[x].apellidos,lista1[x].correo))
        self.tabla.place(x=55,y=120)


    def reg1(self):
        NewStudent(self.obU)

    def getFilter(self):
        self.datos = self.getData(self.cedula.get())
        if self.datos!=[]:
            self.__showTable(self.datos)
            self.cedula.delete(0,END)
        else:
            self.datos= self.fillList()
            self.__showTable(self.datos)


    def onClick(self,event):
        item = event.widget.identify("item",event.x,event.y)
        pos = self.cad.getNumber(item)
        if pos!=-1:
            self.clk+=1
            if self.clk==1:
                self.n_fila[0]=pos
            if self.clk==2:
                self.n_fila[1]=pos
                self.clk=0
            if self.clk==0 and self.n_fila[0]==self.n_fila[1]:
                print("Ventana 1")



    def validateId(self,accion,car,texto):
        if accion!='1':
            return True
        return car in "1234567890" and len(texto)<10

    def getData(self,id):
        lista2=[]
        for i in range(len(self.datos)):
            if id== self.datos[i].cedula:
                lista2.append(self.datos[i])
        return lista2

    def fillList(self):
        lista3 =[]
        for i in range(0,5):
            obj=Estudiantes("1234567"+str(i+1),"Jose Carlos"+str(i+1),
                                      "Linares Lopez","Correo",123)
            lista3.append(obj)
        return lista3


# Codigo de prueba
v1 = GestionDatos()