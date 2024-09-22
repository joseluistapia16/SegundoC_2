from tkinter import *
from tkinter import ttk
from vistas.processGui import *
from dominio.entidades import *
from vistas.createStudent import *
from procesos.procesos import *
from vistas.editStudent import *
from dao.crudEstudiante import *


class GestionDatos:

    def __init__(self, obj=None):
        self.crud = CrudStudent()
        datos1 = ("A",)
        self.datos = self.crud.getAllStudents("segundok", datos1)
        self.clk = 0
        self.cad = Cadenas()
        self.obU = obj
        self.n_fila = [-1, -1]
        self.cv = GuiProcess()

        # Generar datos

        # *********
        self.getWindow()
        self.getLabels()
        self.getInputs()
        self.getButtons()
        self.__showTable(self.datos)
        self.venT.mainloop()

    def getWindow(self, titulo=None):
        self.venT = Toplevel()
        self.venT.title(titulo)
        self.cv.center(self.venT, 1100, 400)
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
        self.search_var = StringVar()  # Variable para la búsqueda en tiempo real
        self.search_var.trace("w", self.update_table)  # Actualiza la tabla en tiempo real cuando se escribe

        self.cedula = Entry(self.venT, textvariable=self.search_var,
                            #validate="key",
                            font=("Arial", 12), fg="black", bg="white",
                            #validatecommand=(self.validate1, "%d", "%S", "%s")
                            )
        self.cedula.place(x=450, y=77)

    def getButtons(self):
        btn2 = Button(self.venT, relief="flat", text="Salir",
                      bg="green", fg="black", font=("Arial", 12),
                      command=self.venT.destroy,
                      cursor="hand1").place(x=580, y=350, width=90)

        btn3 = Button(self.venT, relief="flat", text="Registro",
                      bg="green", font=("Arial", 11),
                      command=self.reg1,
                      cursor="hand1").place(x=460, y=350, width=90)

    def __showTable(self, lista1=None):
        self.tabla = ttk.Treeview(self.venT, columns=(1, 2, 3, 4, 5),
                                  show="headings", height=8)
        self.tabla.bind("<1>", self.onClick)
        vsb = ttk.Scrollbar(self.venT, orient="vertical",
                            command=self.tabla.yview)
        vsb.place(x=1058, y=120, height=190)
        self.tabla.configure(yscrollcommand=vsb.set)
        estilo = ttk.Style()
        estilo.theme_use("clam")
        estilo.configure("Treeview.Headings", bg="red")
        # Columna
        self.tabla.heading(1, text="ID")
        self.tabla.heading(2, text="Cedula")
        self.tabla.heading(3, text="Nombre")
        self.tabla.heading(4, text="Apellido")
        self.tabla.heading(5, text="Correo")
        self.tabla.column(1, anchor=CENTER)
        self.tabla.column(2, anchor=CENTER)
        self.tabla.column(3, anchor=CENTER)
        self.tabla.column(4, anchor=CENTER)
        self.tabla.column(5, anchor=CENTER)

        # Inicialmente muestra todos los datos
        self.update_table()

        self.tabla.place(x=55, y=120)

    def reg1(self):
        NewStudent(self.obU)

    def update_table(self, *args):
        """Actualiza la tabla filtrando los resultados según la búsqueda."""
        search_term = self.search_var.get().lower()  # Obtiene el término de búsqueda

        # Limpiar la tabla actual
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        # Filtra los datos según el término de búsqueda
        filtered_data = [student for student in self.datos if
                         search_term in student.cedula.lower() or
                         search_term in student.nombres.lower() or
                         search_term in student.apellidos.lower() or
                         search_term in student.correo.lower()]

        # Insertar los datos filtrados en la tabla
        for idx, student in enumerate(filtered_data):
            self.tabla.insert("", "end", values=(
                str(idx + 1),
                student.cedula,
                student.nombres,
                student.apellidos,
                student.correo
            ))

    def onClick(self, event):
        # Identifica el item seleccionado
        item = self.tabla.identify_row(event.y)
        if item:
            # Recupera los valores de la fila seleccionada
            valores = self.tabla.item(item, "values")
            print("Valores seleccionados: ", valores)

            # Busca la posición de los datos originales basados en el valor de la cédula (o algún otro identificador único)
            for idx, student in enumerate(self.datos):
                if student.cedula == valores[1]:  # Suponiendo que el valor de cédula está en la columna 2
                    pos = idx
                    break
            else:
                pos = -1

            print("Posición en los datos originales: ", pos)

            # Verifica si se encontró una posición válida
            if pos != -1:
                self.clk += 1
                if self.clk == 1:
                    self.n_fila[0] = pos
                if self.clk == 2:
                    self.n_fila[1] = pos
                    self.clk = 0
                if self.clk == 0 and self.n_fila[0] == self.n_fila[1]:
                    # Muestra la información del estudiante seleccionado
                    estudiante = self.datos[pos]

                    # Llama a la función para editar el estudiante
                    EditStudent(estudiante)
        else:
            print("No se seleccionó ningún item.")

    def validateId(self, accion, car, texto):
        if accion != '1':
            return True
        return car in "1234567890" and len(texto) < 10

if __name__ == '__main__':
    GestionDatos()