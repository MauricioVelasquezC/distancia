import math

class Punto:
    def __init__(self):
        self.x=0 
        self.y=0 
        
    def Calcular_distancia (self, otroPunto):

        resultado=math.sqrt(math.pow(self.x-otroPunto.x,2)+math.pow(self.y-otroPunto.y,2))
        return resultado

