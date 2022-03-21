class Punto2D():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return "A = X : "+(str(self.x))+", Y: "+(str(self.y))
    def traslacion(self,p,q):
        self.x=self.x+p
        self.y=self.y+q
        return self

class Punto3D():
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __str__(self):
        return "A = X : "+(str(self.x))+", Y: "+(str(self.y))+", Z: "+(str(self.z))
    def traslacion(self,p,q,j):
        trasladado_list =[]
        trasladado_list.append(self.x+p)
        trasladado_list.append(self.y+q)
        trasladado_list.append(self.z+j)
        return Punto3D(trasladado_list[0],trasladado_list[1],trasladado_list[2])












