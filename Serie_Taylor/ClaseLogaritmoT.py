import math
import sympy as sp

class LogaritmoNTayor():
    def NumerosSerie(self):
        nums = []

        for n in range(18):
            nums.append(n)
        return nums
    
    def Factorial(self, nums):
        f = 1
        for n in range(2, nums+1):
            f *= n
        return f
    
    def DerivadasOrden(self):
        x = sp.Symbol('x')

        # Definiendo la funcion
        f = sp.ln(x)

        # Calculando las derivadas de 0 - 17
        fDerivadas = []
        for i in range(18):
            derivada = f.diff(x, i)
            fDerivadas.append(derivada)
        return fDerivadas
    
    def DerivadasEvaluadas(self, a):
        # Variable simbolica
        x = sp.Symbol('x')

        evaluados = []
        derivadas = self.DerivadasOrden()
        for derivada in derivadas:
            resultado = derivada.subs(x, a)
            evaluados.append(float(resultado))
        return evaluados
    
    # Llamando a las otras funciones, funcion principal de esta clase
    def FLogaritmoTaylor(self, x, a):
        suma = 0

        # Arreglo que tendra los evaluados y n
        evaluados = self.DerivadasEvaluadas(a)
        potencias = self.NumerosSerie()

        for i in range(18):
            suma += (evaluados[i] * (x - a) ** potencias[i]) / self.Factorial(potencias[i])
        return suma

#inst = LogaritmoNTayor()
#print(inst.FLogaritmoTaylor(10, 8))