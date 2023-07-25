import math
from sympy import symbols, diff, cos, pi, nsimplify, expand

class CosenoTaylor():
    def PotCosenoTaylor(self):
        p = []
        for n in range(18):
            p.append(n)
        return p
    # Factorial
    def Factorial(self, nums):
        f = 1
        for n in range(2, nums+1):
            f *= n
        return f
    
    def DerivadasOrden(self):
        # Define la variable simbólica
        x = symbols('x')
        # Define la función seno
        f = cos(x)

        fDerivadas = []
        for i in range(18):
            derivada = f.diff(x, i)
            fDerivadas.append(derivada)
        return fDerivadas
    
    # Metodo que evalua cada derivada con el valor de a
    def DerivadasEvaluadas(self, a):
        # Define la variable simbólica
        x = symbols('x')

        evaluados = []
        derivadas = self.DerivadasOrden()
        for derivada in derivadas:
            resultado = derivada.subs(x, a)
            evaluados.append(float(resultado))
        return evaluados

     # Metodo que calcula el resultado de la serie de Taylor
    def FCosenoTaylor(self, x, a):
        # Convirtiendo a radianes
        a_radian = math.radians(a)
        x_radian = math.radians(x)
        suma = 0

        # Arreglo que tendrá los evaluados
        evaluados = self.DerivadasEvaluadas(a_radian)
        potencias = self.PotCosenoTaylor()

        for i in range(18):
            termino = (evaluados[i] * (x_radian - a_radian) ** potencias[i]) / self.Factorial(potencias[i])
            suma += termino
        return suma


