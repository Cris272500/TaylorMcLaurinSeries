import math

class Seno:
    # Metodo que calcula la potencia
    def pot(self):
        p = []
        for i in range(18):
            p.append(pow(-1, i))
        return p

    # Metodo que retorna los numeros impares del 0 al 17
    def imp(self):
        a = []
        for i in range(18):
            a.append(2 * i + 1)
        return a

    # Metodo que calcula el factorial de los numeros impares
    def fact(self, impares):
        f = 1
        for i in range(2, impares + 1):
            f *= i
        return f

    # Metodo que llama los anteriores y hace la sumatoria
    def Fseno(self, x):
        a1 = []
        a2 = []
        suma = 0

        a1 = self.pot()
        a2 = self.imp()

        valor = math.radians(x)

        for i in range(18):
            indice = a2[i]
            suma = suma + (a1[i] * pow(valor, a2[i]) / self.fact(indice))
        return suma


