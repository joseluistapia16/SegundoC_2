'''
def getmenu1(lista):
    for i in range(len(lista)):
        print(str(i + 1) + "." + lista[i])
    op = 0
    while op > len(lista) or op <= 0:
        op = int(input("Escoja el menu 1..." ))
    return op


lista = ["Desayuno", "Almuerzo", "Merienda", "Cena"]
getmenu1(lista)
'''

user1_answer = input("roca, papel o tijera:")
user2_answer = input("droca, papel o tijera?")

def compare(u1,u2):
    if u1==u2:
        print("Este es un empate")
    elif u1=="roca":
        if u2=="tijera":
            print("Gana Roca")
        else:
            print("Gana papel")
    elif u1=="tijera":
        if u2=="papel":
            print("Gana tijera")
        else:
            print("Gana Roca")
    elif u1=="papel":
        if u2=="roca":
            print("Gana papel")
        else:
            print("Gana Tijera")
    else:
        return(print("Inputs invalidos, trata nuevamente"))

print(compare(user1_answer, user2_answer))

'''