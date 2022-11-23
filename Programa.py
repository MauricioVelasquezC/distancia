from Punto import Punto



class Programa():

    def __init__(self):
        messi=Punto()
        elbicho=Punto()
        messi.x=10
        messi.y=12
        elbicho.x=16
        elbicho.y=18
        self.distancia=messi.Calcular_distancia(elbicho)

dist=Programa()

print (dist.distancia)

        