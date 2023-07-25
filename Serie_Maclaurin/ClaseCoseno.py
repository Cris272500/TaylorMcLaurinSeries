import math

class Coseno:
    def potCos(self):
        p = []
        for i in range(18):
            p.append(pow(-1, i))
        return p

    def par(self):
        a = []
        for i in range(18):
            a.append(2 * i)
        return a
    
    def factCos(self, pares):
        f = 1
        for i in range(2, pares + 1):
            f *= i
        return f
    
    def FCoseno(self, x):
        a1 = []
        a2 = []
        suma = 0

        a1 = self.potCos()
        a2 = self.par()

        valor = math.radians(x)

        for i in range(18):
            indice = a2[i]
            suma = suma + (a1[i] * pow(valor, a2[i]) / self.factCos(indice))
        return suma




