import sympy as sp

# Definir la variable simbólica
x = sp.Symbol('x')

# Definir la función
f = sp.ln(x)

print(f)

# Calcular la derivada
df = sp.diff(f, x, 1)

# Imprimir la derivada
print(df)
