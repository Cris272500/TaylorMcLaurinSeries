import math

class LogaritmoN():
    def PotenciaLN(self):
        p = []

        for i in range(1, 18):
            p.append(pow(-1, i - 1))
        return p

    def Numeros(self):
        N = []
        for i in range(1, 18):
            N.append(i)
        return N

    def FLogaritmoNatural(self, x):
        a1 = []
        a2 = []
        suma = 0
        a1 = self.PotenciaLN()
        a2 = self.Numeros()

        for i in range(17):
            indPot = a1[i]
            indice = a2[i]
            suma += (indPot * pow(x,indice)) / indice
        return suma

