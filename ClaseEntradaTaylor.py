from EliasGod_Inputs import punto_limit

class Entrada_Taylor():
   def ValorX_A(self, opc):
    while True:
        print("Ingrese el valor de x: ")
        x = punto_limit()

        # Validar que el valor de 'x' sea numérico
        try:
            x = float(x)
        except ValueError:
            print("Error: el tipo de dato no coincide")
            continue
        a = 0
        while a == 0:
            print("Ingrese el valor de a: ")
            a = punto_limit()

            # Validar que el valor de 'a' sea numérico
            if not a.isnumeric():
                print("Error: el tipo de dato no coincide")
                a = 0
                continue

            # Convertir 'a' a un número flotante
            a = float(a)
                    
            # Mostramos un mensaje de error si 'a' es cero
            if a == 0:
                print("Error, -a- debe ser distinto de cero, por la definicion")
        # El caso si escoge seno o coseno
        if opc == 1 or opc == 2:
            return x, a
        # El caso si escoge exponencial
        elif opc == 3:
            if x >= 100 or x <= -100:
                print("El valor digitado provoca un desbordamiento, pruebe con otro")
            else:
                return x, a
        # El caso si escoge logaritmo natural
        elif opc == 4:
            if x <= 0:
                print("El valor digitado es inválido, solo se aceptan valores positivos")
            if a <= 0:
                print("Debe ser positivo")
            else:
                return x, a


       
