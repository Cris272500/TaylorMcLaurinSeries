import math

class Exponencial():
    # Método que calcula la potencia 
    def PotenciaE(self):
        p = []
        for i in range(18):
            p.append(i)
        return p
    
    # Método que calcula el factorial de un número
    def FactorialE(self, numero):
        f = 1
        for i in range(1, numero + 1):
            f *= i
        return f
    
    # Método que calcula la sumatoria de la función exponencial
    def FExponencial(self, x):

        l_numeros = self.PotenciaE()
        suma = 0

        for i in range(18):
            suma += pow(x, l_numeros[i]) / self.FactorialE(l_numeros[i])
        return suma


