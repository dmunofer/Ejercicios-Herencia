class A():
    def __init__(self,a):
        self.a =a 
class B():
    def __init__(self,b):
        self.b=b 
class C():
    def __init__(self,c):
        self.c =c 
class D(A,B,C):
    def __init__(self,a,b,c):
        self.a= A.__init__(self,a)
        self.b=B.__init__(self,b)
        self.c= C.__init__(self,c)
