import msvcrt

def punto_limit():
    input_str = ""
    dot_used = False

    while True:
        char = msvcrt.getch().decode('utf-8')

        # Valida el Enter (El boton que funciona para confirmar entrada)
        if char == '\r':
            break
        
        # Valida la tecla Space
        if char == '\x08':
            if len(input_str) > 0:
                input_str = input_str[:-1]
                if input_str and input_str[-1] == '.':
                    dot_used = True
                else:
                    dot_used = False
                print('\b \b', end='', flush=True)
            continue
        
        # Agrega Caracteres al Input, si el '.' ya se utilizo, previene de ingresarlo nuevamente
        if char == '.':
            if not dot_used:
                dot_used = True
                input_str += char
                print(char, end='', flush=True)
        else:
            input_str += char
            print(char, end='', flush=True)
    
    print()
    return input_str

# Ejemplo del Uso
#Se lo pasas como funcion y string argumento

