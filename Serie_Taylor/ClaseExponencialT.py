import math

class ExponencialTaylor():

    # Funcion para cargar las potencias e^a*n
    def PotenciasExponencialTaylor(self, a):
        p = []
        for n in range(18):
            p.append(math.exp(a))
        return p
    
    # Lista numeros para sacarle factorial y Elevarlos
    def Numeros(self):
        numeros = []
        for n in range(18):
            numeros.append(n)
        return numeros
    
    # Calculando el factorial de la lista de numeros
    def Factorial(self, Nums):
        f = 1
        for n in range(2, Nums + 1):
            f *= n
        return f
    
    # Llamando a las otras funciones
    def F_ExponencialTaylor(self, x, a):
        potencias = []
        numeros = []
        suma = 0

        potencias = self.PotenciasExponencialTaylor(a)
        numeros = self.Numeros()

        for n in range(18):
            suma += (potencias[n] * pow(x - a, numeros[n])) / (self.Factorial(numeros[n]))
        return suma


