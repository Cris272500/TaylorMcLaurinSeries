#Clases de la serie de MacLaurin
from Serie_Maclaurin.ClaseSeno import Seno
from Serie_Maclaurin.ClaseCoseno import Coseno
from Serie_Maclaurin.ClaseExponencial import Exponencial
from Serie_Maclaurin.ClaseLogaritmoNatural import LogaritmoN

# Clases de la serie de Taylor
from Serie_Taylor.ClaseSenoT import SenoTaylor
from Serie_Taylor.ClaseCosenoT import CosenoTaylor
from Serie_Taylor.ClaseExponencialT import ExponencialTaylor
from Serie_Taylor.ClaseLogaritmoT import LogaritmoNTayor

# Clases de Entradas
from ClaseEntradaTaylor import Entrada_Taylor
from ClaseEntrada import Entrada

class Main(Entrada, Entrada_Taylor):
    def __init__(self):
        self.funcionS = Seno()
        self.funcionC = Coseno()
        self.funcionE = Exponencial()
        self.funcionL = LogaritmoN()

        # Funciones para la serie de Taylor
        self.funcionCTaylor = SenoTaylor()
        self.funcionCosenoTaylor = CosenoTaylor()
        self.funcionExponencialTaylor = ExponencialTaylor()
        self.funcionLogaritmoTaylor = LogaritmoNTayor()

    def MenuOpc(self):
        while True:
            print("----BIENVENIDO-----\n"
                  "Escoja que la serie\n"
                  "1. Serie de Taylor\n"
                  "2. Serie de Maclaurin\n"
                  "3. Salir")
            opc = input("--> ")
            try:
                opc = int(opc)
                # 1er caso
                if opc == 1:
                    # Se ejecuta la serie de Taylor y cambiamos de menu
                    print("EJERCICIOS DE SERIE DE TAYLOR")
                    self.TaylorMenu()
                    break
                elif opc == 2:
                    print("EJERCICIOS DE SERIE DE MACLAURIN")
                    self.MaclarinMenu()
                    break    # Se ejecuta la serie de Maclarin y cambiamos de menu
                elif opc == 3:
                    print("Saliendo...")
                    break    # El programa termina su ejecucion
                else:
                    print("Opcion invalida")
            except ValueError:
                print("Ingrese un numero entero")

    # Menu de ejercicios para serie de Taylor
    def TaylorMenu(self):
        while True:
            print("Escoja el ejercicio que desea resolver por Taylor: \n"
                  "1. f(x) = sen(x)\n"
                  "2. f(x) = cos(x)\n"
                  "3. f(x) = eˣ\n"
                  "4. f(x) = ln(1 + x)\n"
                  "5. Salir")
            opc = input("--> ")
            # Seno
            try:
                opc = int(opc)
                # Seno
                if opc == 1:
                    print("FUNCION SENO")
                    x, a = self.ValorX_A(opc)
                    self.ejecutar_programa(self.funcionCTaylor.FSenoTaylor(x , a))
                elif opc == 2:
                    print("FUNCION COSENO")
                    x, a = self.ValorX_A(opc)
                    self.ejecutar_programa(self.funcionCosenoTaylor.FCosenoTaylor(x, a))
                elif opc == 3:
                    print("FUNCION EXPONENCIAL")
                    x, a = self.ValorX_A(opc)
                    self.ejecutar_programa(self.funcionExponencialTaylor.F_ExponencialTaylor(x, a))
                elif opc == 4:
                    print("FUNCION LOGARITMICA")
                    x, a = self.ValorX_A(opc)
                    self.ejecutar_programa(self.funcionLogaritmoTaylor.FLogaritmoTaylor(x, a))
                elif opc == 5:
                    self.MenuOpc()
                    break
            except ValueError:
                print("Ingrese un numero entero")
            # Coseno
            # Exponencial
            # Logaritmica

    # Menu de ejercicios para serie de Maclaurin
    def MaclarinMenu(self):
        while True:
            print("Escoja el ejercicio que desea resolver por Maclaurin: \n"
                  "1. f(x) = sen(x)\n"
                  "2. f(x) = cos(x)\n"
                  "3. f(x) = eˣ\n"
                  "4. f(x) = ln(1 + x)\n"
                  "5. Salir")
            opc = input("--> ")
            try:
                opc = int(opc)
                # Seno
                if opc == 1:
                    print("FUNCION SENO")
                    self.ejecutar_programa(self.funcionS.Fseno(self.valorX(opc)))
                elif opc == 2:
                    print("FUNCION COSENO")
                    self.ejecutar_programa(self.funcionC.FCoseno(self.valorX(opc)))
                elif opc == 3:
                    print("FUNCION EXPONENCIAL")
                    self.ejecutar_programa(self.funcionE.FExponencial(self.valorX(opc)))
                elif opc == 4:
                    print("FUNCION LOGARITMICA")
                    self.ejecutar_programa(self.funcionL.FLogaritmoNatural(self.valorX(opc)))
                elif opc == 5:
                    self.MenuOpc()
                    break
            except ValueError:
                print("Ingrese un numero entero")

    def ejecutar_programa(self, function):
        resultado = function
        print("el resultado es:", resultado)

main = Main()
main.MenuOpc()
#main.ejecutar_programa()    # Llamando la funcion que ejecuta el programa