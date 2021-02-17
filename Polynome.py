import math
class Polynome:
    "Construit un polynome de degré 2 de forme: a*(x^2)+b*x+c"
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def calcul(self,x):
        return (self.a*pow(x,2)+self.b*x+self.c)
    def affichePolynome(self,x):
        print(self.a,x,"^2 +",self.b,x,"+",self.c)
    