from EliasGod_Inputs import punto_limit

class Entrada():
    def valorX(self, opc):
       while True:
           print("Ingrese el valor de x: ")
           x = punto_limit()
           # Evitando que introduzca una letra
           try:
                x = float(x)
                if(opc == 1 or opc == 2):
                    # Vendrian las validaciones en el caso si es seno o coseno
                    return x
                # Validaciones para el caso de la funcion exponencial
                elif(opc == 3):
                    if x >= 100 and x <= -100:
                        print("El valor digitado provoca un desbordamiento pruebe con otro")
                    else:
                        return x
                # Validaciones para el caso de la funcion ln
                elif(opc == 4):
                    if x <= 0:
                        print("El valor digitado es invalido, solo se aceptan positivos")
                    else:
                        return x
           except ValueError:
               print("Dato no valido, debe ser un numero")
