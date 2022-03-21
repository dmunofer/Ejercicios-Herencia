orientaciones = ["NORTE","SUR", "ESTE","OESTE"]

class Pared():
    def __init__(self,orientacion):
        if orientacion == orientaciones[0]:
            self.orientacion = "NORTE"
        elif orientacion == orientaciones[1]:
            self.orientacion = "SUR"
        elif orientacion == orientaciones[2]:
            self.orientacion= "ESTE"
        elif orientacion == orientaciones[3]:
            self.orientacion = "OESTE"
pared_norte = Pared("NORTE")
pared_oeste = Pared("OESTE")
pared_sur = Pared("SUR")
pared_este = Pared("ESTE")

class Ventana(Pared,float):
    def __init__(self,num):
        self.ventana= (Pared(),num)
ventana_norte = Ventana(pared_norte, 0.5)
ventana_oeste = Ventana(pared_oeste, 1)
ventana_sur = Ventana(pared_sur, 2)
ventana_este = Ventana(pared_este, 1)

class Casa(Pared(),Ventana()):
    def __init__(self,pared,ventana):
        self.pared = pared
        self.ventana = ventana
    def __str__(self):
        return str(self.pared)+str(self.ventana)
    def superficie_acristalada(self):
        suma=0
        for e in self.ventana:
            suma=suma+e
        return suma


