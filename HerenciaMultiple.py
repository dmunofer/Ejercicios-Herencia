class A():
    def __init__(self,a):
        self.a =a 
class B():
    def __init__(self,b):
        self.b=b 
class C():
    def __init__(self,c):
        self.c =c 
class D():
    def __init__(self,a,b,c):
        a= A.__init__(self,a)
        b=B.__init__(self,b)
        c= C.__init__(self,c)
