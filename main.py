
from core.core import *
from vistas.login import *
if __name__ == '__main__':
    lg = LoginK("Segundo K")
"""
if __name__ == '__main__':
    inicio = Core()
    inicio.start()

 """












"""
from procesos.procesos import *
from procesos.menu import *
class Producto:

    def __init__(self,nom,mar,cod):
        self.nombre = nom
        self.marca = mar
        self.__codigo = cod

    def setCodigo(self,codigo):
        self.__codigo= codigo

    def getCodigo(self):
        return self.__codigo

    def getData(self):
        return self.nombre+" "+self.marca+" "+self.__codigo


def funcion1():
    n1 = int(input("Numero 1:"))
    n2 = int(input("Numero 2:"))
    r = getSuma(n1,n2)
    print("El total es:"+str(r))
def funcion2():
    cadena= "Hola"
    msg = " Segundo K"
    A = " POO"
    aux = cadena+msg+A+str(90.90)
    print(aux)

def funcion3():
    num1 = int(input("Numero 1:"))
    num2=  int(input("Numero 2:"))
    res = getSuma(num1,num2)
    print("Resultado:",res)

def funcion4():
    cliente = input("Cliente:")
    producto = input("Producto:")
    precio = float(input("Precio:"))
    cantidad = int(input("Cantidad:"))
    subtotal = getSubtotal(precio,cantidad)
    iva = getIva(subtotal)
    total = getTotal(subtotal,iva)
    msg = getResults(subtotal,iva,total)
    print(msg)

def funcion5():
    estudiante= input("Estudiante:")
    materia = input("Materia:")
    n1 = float(input("Nota 1:"))
    n2 = float(input("Nota 2:"))
    ex = float(input("Examen:"))
    promedio = getPromedio(n1,n2,ex)
    msg = "El promedio es:"+str(round(promedio,2))
    print(msg)
    estado = getEstado(promedio)
    print(estado)


def funcion6():
    edad = int(input("Edad:"))
    aux = getEtapa(edad)
    print(aux)

def funcion7():
    c = 0
    ci=0
    ac=0
    while c<15:
        c=c+1
        if c % 2!=0:
          print(c)
          ci= ci +1
          ac=ac+c
    print("Total de numeros impares es:"+str(ci))
    print("Total acumulado:"+str(ac))

    ci = 0
    ac=0
    for c in range(1,16):
        if c%2!=0:
            print(c)
            ci=ci+1
            ac=ac + c
    print("Cantidad de numeros impares:"+str(ci))
    print("Total acumulado:"+str(ac))

def funcion8():
    tupla1 = ("JOSE","LUIS","KELLY",True,100,300)
    print(tupla1)
    print(tupla1[5])
    for i  in range(len(tupla1)):
        print(tupla1[i])

    lista=[9,0,11]
    lista.append("Segundo K")
    lista.append("POO")
    lista.append(True)
    lista[4]="BASE DE DATOS"
    print(lista)
    print("Tamaño inicial "+str(len(lista)))
    lista.pop(2)
    print(lista)
    print("Tamaño final "+str(len(lista)))
    lista.clear()
    print("Tamaño final "+str(len(lista)))

    dic1 = {
           100 : "POO",
           "clave 2": 300,
           True : (5,6,8),
        (1,1,2):False
    }
    dic1[33]="Diccionario"
    del dic1["clave 2"]
    dic1[True]=777
    print(dic1)

def funcion9():
    tupla = ("Registro","Consulta","Actualizar",
             "Eliminar","Listar","Salir",
             )
    op=getMenu(tupla)
    if op==1:
        print("PYTHON")
    if op==2:
        print("JAVA")

def funcion10():
    i = 0
    lista=[]
    while i <5:
        num = int(input("Numero "+str(i+1)+":"))
        res = validateNumero(num,lista)
        if res !=True:
           lista.append(num)
        else:
            i = i -1
        i=i+1

    for x in range(len(lista)):
        print(lista[x])


#num = inputInt("ingrese un numero:")

obj = Producto("Cola","Coca Cola","C001")
print(obj.getData())


#funcion10()
"""
