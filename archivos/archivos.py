from dominio.entidades import *

class ArchivoK:

    def create(self,ruta,registro,modo):
        archivo = open(ruta,modo)
        archivo.write(registro)
        archivo.close()

    def getAllStudents(self,ruta):
        lista = []
        try:
            archivo = open(ruta,"r")
            for linea in archivo.readlines():
                tupla = linea.split(";")
                obj = Estudiante(tupla[0],tupla[1],int(tupla[2]))
                lista.append(obj)
        except:
            print(".... ")
        return lista


    def getHTML(self,ruta):
        texto = ""
        try:
            archivo = open(ruta,"r")
            for linea in archivo.readlines():
                texto= texto+linea
        except:
            print(".... ")
        return texto

ruta = "C:/Users/sopor/OneDrive/Escritorio/Proyectos/cursoJS/index.html"
arch = ArchivoK()
msg = arch.getHTML(ruta)
print(msg)