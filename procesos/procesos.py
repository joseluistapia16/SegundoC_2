def getSuma(x,y):
    return (x+y)

def getSubtotal(precio,cantidad):
    return (precio*cantidad)

def getIva(subtotal):
    return (subtotal*0.12)

def getTotal(subtotal,iva):
    return (subtotal+iva)

def getResults(subtotal,iva,total):
    msg = "Subtotal:"+str(round(subtotal,2))+\
          "\nIva:"+str(round(iva,2))+\
          "\nTotal a pagar:"+str(round(total,2))
    return msg

def getPromedio(n1,n2,n3):
    return (n1+n2+n3)/3

def getEstado(promedio):
    if promedio<0 or promedio>10:
        return "Valor invalido!!"
    else:
        if promedio>=0 and promedio<7:
            return "Reprobado!"
        if promedio>=7 and promedio<=10:
            return "Aprobado"

def getEtapa(edad):
    if edad<0:
        return "Valor invalido!!"
    else:
        if edad>=0 and edad<11:
            return "Infante!"
        if edad>10 and edad<18:
            return "Adolescente!"
        if edad>17 and edad<26:
            return "Joven!"
        if edad>25 and edad<65:
            return "Adulto!"
        if edad>64:
            return "Adulto mayor!"

def validateNumero(valor,lista):
    res = False
    for i in range(len(lista)):
        if valor==lista[i]:
            res = True
            break
    return res

def inputInt(cadena):
    num= -1
    while num<0:
        try:
           num = int(input(cadena))
        except:
            num=-1
    return num



