'''
N1= int(input("numero 1:"))
N2= int(input('numero 2:'))
R= (N1-N2)
msg=('Resta:'+str(R))
print(msg)
'''
import random

'''
X1=float(input('ingresa No 1:'))
X2=float(input('ingresa No 2:'))
M= (X1*X2)
msg=('Multiplicacion:'+str(M))
print(msg)
'''
'''
N1=float(input('Dato 1:'))
N2=float(input('Dato 2:'))
D=(N1/N2)
msg=('Division:'+str(D))
print(msg)
'''
'''
N= input('Nombre Estudiante:')
M= input('Materia:')
N1= float(input('Nota 1:'))
N2= float(input('Nota 2:'))
N3= float(input('Nota 3:'))
P= ((N1+N2+N3)/3)
msg= ('Promedio:'+ str(P))
print(msg)

if P>=7 and P<=10:
    print('Aprobado')
if P<7:
    print('Reprobado')
if P<0 or P>10:
    print('Valores invalidos')
'''
'''
Cliente=input('Nombre Cliente:')
P=input('Producto:')
C=float(input('Cantidad:'))
PR=float(input('Precio:'))
S=(C*PR)
IVA=(S*0.12)
Total=(S+IVA)
msg=('Subtotal:'+ str(round(S,2)))
ms2=('IVA:'+str(round(IVA,2)))
ms3=('Total:'+str(round(Total,2)))
print(msg)
print(ms2)
print(ms3)

if S>100:
    Dst=float(S*0.02)
    print('Subtotal con descuento:'+ str(round(S-Dst,2)))
    TotalD = float(S-Dst + ((S-Dst)*0.12))
    print('Total con Descuento:'+ str(TotalD))

'''
'''
edad = int(input("ingrese su edad:"))
if edad>=0 and edad<11:
    print("Infante")
if edad>=11 and edad<=17:
    print("Adolescente")
if edad>=18 and edad<=25:
    print("Jovenes")
if edad>=26 and edad<=64:
    print("Adulto")
if edad>64:
    print("Adulto mayor")
if edad<0:
    print("Valor invalido")
'''
'''
K=float(input('Kilometros recorridos:'))
G=float(input('Litros de combustible gastados:'))
R=(K/G)
print('El consumo de kilometros es de'+' '+str(R))
K=float(input('Ingreso de Kilometros:'))
M=K*1000
print(M)
'''
'''
A=int(input('Juegos ganados por A:'))
B=int(input('Juegos ganados por B:'))
if(A==6 and B==(A-2)):
    print('Gano A')
if(A==(B-2) and B==6):
    print('Gano B')
if(A==5 and B==7):
    print('Gano B')
if(A==7 and B==5):
    print('Gano A')
if(A==6 and B==7):
    print('Gano B')
if(A==7 and B==6):
    print('Gano A')
if(A==5 and B>5 and B<7) or (B == 5 and A > 5 and A < 7):
    print('Aun no termina')
else:
    print('invalido')
'''
"""
c=0
ci=0
ac = 0
while c<10:
    c=c+1
    if c%2!=0:
      print(c)
      ci=ci+1
      ac = ac + c

print("Numero impares "+str(ci))
print("Valor acumulado "+str(ac))

cp =0
acp=0
for c in range(1,11):
    if c%2==0:
      print(c)
      cp= cp+1
      acp= acp+c
print("Numero de pares:"+str(cp))
print("Valor acumulado "+str(acp))
"""
'''
tupla1 = (45,False,"Jose",405,True,"Biggi")
for i in range(len(tupla1)):
    print(tupla1[i])
'''
'''
for c in range(1,11):
    print(c//2)
'''
'''
counter = 10
while counter >2:
    counter /= 2
    print(counter)
'''
'''

def sumsqrt(valor1, valor2):
    valor1*=valor1
    valor2*=valor2
    sum=valor1+valor2
    print(str(sum))

sumsqrt(3,4)
'''
'''
def myfuntion():
   print('Hello from my funtion')

myfuntion()


def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Mayra", "Refsnes")
'''
'''
tuple1 = (10,20,30,40,50)
tuple1 = tuple1[0:len(tuple1)]
print(tuple1)
'''
'''
tuple1=('orange', [10,20,30], (5,15,25))
print(tuple1[1][1])
tuple1=tuple1[1]
tuple1=tuple1[1]
print(tuple1)
'''
'''
tuple1=(50, )
print(tuple1)
'''
'''
tuple1=(10,20,30,40)
a,b,c,d = tuple1
print(a)
print(b)
print(c)
print(d)
'''
'''
tuple1=(11,22)
tuple2=(99,98)
tuple1, tuple2=tuple2, tuple1
print(tuple1)
print(tuple2)
'''
'''
tuple1=(11,22,33,44,55,66)
tuple2=(tuple1[3], tuple1[4])
print(tuple2)
'''
'''
tuple1=(11,22,33,44,55,66)
tuple2=tuple1[3:-1]
print(tuple2)
'''
'''
tuple1=(11, [22, 33], 44, 55)
tuple1[1][0]=222
print(tuple1)
'''
'''
tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(tuple1)
'''
'''
a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)
'''
'''

a = ("h", "b", "a", "c", "f", "d", "e", "g")
x = sorted(a, reverse=True)
print(x)
'''
'''
tuple1=(50,10,60,70,50)
print(tuple1.count(50))
'''
'''
def check(t):
    return all(i == t[0] for i in t)

tuple1 = (45, 45, 45, 45)
print(check(tuple1))
'''
'''
tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
tuple1 = (sorted((tuple1), key=lambda x: x[1]))
print(tuple1)
'''
'''
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(t(2))
'''
'''
'''
'''
a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a, reverse= True)
print(x)
'''
'''

'''
'''
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(1))
'''
'''
tuple1=(50,10,60,70,50)
print(tuple1.count(50))
'''
'''
def check(t):
    return all(i==t[0] for i in t)
'''
'''
tupla=(45,45,45,45,45)
print(len(tupla))
'''

'''''
list=[]

for i in range(5):
    y=input('Ingrese nombre:')
    list.append(y)
print(list)
'''
'''
list=(1,2,5,7)

def find(i):
    return all(i==list[0] for i in list)
print(find(7))
'''
'''
lista =[]
for i in range(0,5):
    nombre = input("ingrese su nombre "+str(i+1)+":")
    lista.append(nombre)

for i in range(len(lista)):
   print(lista[i])


nombre = input("Nombre a buscar:")
res ="No existe"
for i in range(len(lista)):
    if nombre == lista[i]:
        res="existe"
        break
print(res)

'''
'''
list=["casa","carro","perro","gato"]
if "loro" in list:
    print("Si esta")
else:
    print("No esta")

'''
'''
nombre=input("Nombre:")
edad=input("Edad:")
year=int(2023-int(edad)+int(100))
print(nombre + " tu tendras 100 en este ano : "+str(year))
'''

'''

numero=int(input("Ingrese un numero:"))
d=(numero%2)
print(d)
texto=("how does an even number react differently when divided by 2")
if d!=0:
    texto=("how does an odd number react differently when divided by 2")
print(texto)
t=(numero%4)
if t==0:
    print("El numero es multiplo de 4")

'''
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num=int(input('Ingrese un numero:'))
list=[]
for i in range(len(a)):
   r=a[i]
   if r<num:
     list.append(r)
     print(list)
'''
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for element in a:
    print(element)
'''
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([x for x in a if x<5])

'''
'''
numbers = [7,3,13,6,8,5,1,2,4,15,9,10,12,14,11]
Newlist=[]
Newlist2=[]
i=int(input("Ingrese un numero:"))

for x in numbers:
    if x<5:
        Newlist.append(x)
        Newlist.sort()
        print(Newlist)

for n in numbers:
    if n<i:
        Newlist2.append(n)
        Newlist2.sort()
        print(Newlist2)
'''
'''
i = int(input("Ingrese un numero:"))

for x in range (1,i+1):
    if i%x==0:
       print(x)

'''
'''
i = int(input("Ingrese un numero:"))
list=[]
for x in range(1,i+1):
    if i%x==0:
        list.append(x)
        print(list)
'''
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list=[]
list1=[]

for i in (a):
    if i in b:
        list.append(i)
        list.sort()


for n in b:
    if n in a:
      list1.append(n)
      list1.sort()

list3=set(list+list1)
print(list3)
'''
'''
#from Menu.menu import *

lista = ["Desayuno", "Almuerzo", "Merienda", "Cena"]
getmenu1(lista)
'''
'''
i=str(input("Ingrese la palabra:"))
r=i[::-1]
print(r)
if r==i:
    print("Palabra palindrome")
else:
    print("Palabra no palindrome")
'''
'''
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b=[]

for i in a:
    if i%2==0:
        b.append(i)
        print(b)
      
b=[i for i in a if i%2==0]
print(b)
'''
'''
a=input("Player 1:")
b=input("Player 2:")
if a=="roca" and b=="tijera":
    print("Gana Player 1")
if a == "papel" and b == "tijera":
    print("Gana Player 2")
if a == "papel" and b == "roca":
    print("Gana Player 1")
else
    print
'''
'''u1=str(input("ingrese dato 1:"))
u2=str(input("ingrese dato 2:"))

def compare (u1, u2):
    if u1 == u2:
        return ("Empate")
    elif u1 == "roca":
        if u2 == "tijera":
            return("gana roca")
        else:
            if u2 == "papel":
               return("gana papel")
            else:
                return ("invalido input")

    elif u1 == "tijera":
        if u2 == "papel":
            return("gana tijera")
        else:
            if u2=="roca":
                return("gana roca")
            else:
                return ("invalido input")

    elif u1 =="papel":
        if u2=="roca":
            return("gana roca")
        else:
            if u2 =="tijera":
                return("gana tijera")
            else:
                return ("invalido input")
    else:
        return("invalido input")
print(compare(u1,u2))

'''
'''
a=input("Ingrese un numero:")
for i in range(0,9):
    i+=1
    if a==i:
       return("acertaste")

'''
'''
lista=(1,2,3,4,5,6,7,8,9)
a=int(input("Ingrese numero:"))
#for i in lista:
    if a==i:
       print("acertaste")
    else:
        if a>9 and a<10:
           print("estas cerca")
        else:
           print("estas lejos")
    print(a)
'''
'''
b=0
a=random.randint(1,9)
c=0
while b !=a and b != "exit":
    b=input("ingrese un numero del 1 al 9:")
    if b=="exit":
        break

    b=int(b)
    c +=1
    if b<a:
        print("too low")
    elif b>a:
       print("too high")
    else:
        print("acertaste")
        print("solo realizastes",c, "intentos")
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
lista1 = []
lista2 = []
lista3=[]
lista4=[]
'''
for i in a:
  if i in b:
      lista1.append(i)
      lista1.sort()
      print(lista1)
for y in b:
  if y in a:
      lista2.append(y)
      lista2.sort()
      print(lista2)
lista3=set(lista1 + lista2)
print(lista3)
'''
'''
import random
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
result = [i for i in set(a) if i in b]

print(a)
print(b)
print(result)

'''
'''
x = [1, 2, 3]
y = [5, 10, 15]
customlist = [a*b for a in x for b in y if a*b%2 != 0]
print(customlist)

'''
'''


numero= input("ingrese un numero" "\n"+ ">>>")
numero= int(numero)
a=[x for x in range (2, numero) if numero%x==0]

def es_primo(n):
    if numero>1:
        if len(a)==0:
            print("es primo")
        else:
            print("no es primo")
    else:
        print("no es primo")
es_primo(numero)
'''
'''

lista1=random.sample(range(1,20),12)
lista1=sorted(lista1)
lista2=[lista1[0],lista1[len(lista1)-1]]
print(lista1)
print(lista2)
'''

n=input("Ingrese la cantidad de numero fibonaci a generar:")
n=int(n)
lista=[]
f=1

def fibonaci(n):
    for n in range(0,n):
        while f<n:
            lista=[1,1]
            lista.append(lista[1]+lista[1-1])
        print(lista)




