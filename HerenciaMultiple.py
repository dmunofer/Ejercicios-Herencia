class A():
    def __init__(self,a):
        self.a =a 
    def __str__(self):
        return str(self.a)
class B():
    def __init__(self,b):
        self.b=b 
    def __str__(self):
        return str(self.b)
class C():
    def __init__(self,c):
        self.c =c 
    def __str__(self):
        return str(self.c)
class D(A,B,C):
    def __init__(self,a,b,c):
        self.a= A(a)
        self.b=B(b)
        self.c= C(c)
    def __str__(self):
        return (str(self.a))+(str(self.b))+(str(self.c))
