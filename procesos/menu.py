from dominio.entidades import *
class MenuK:

    def __init__(self):
        self.obi = Procedimiento()

    def getMenu(self,tupla):
        for i in range(len(tupla)):
            print(str(i+1)+".- "+tupla[i])
        op=0
        while op<1 or op>len(tupla):
            op=self.obi.inputInt("ingrese una opcion[1.."+str(len(tupla))+"]:")
        return op