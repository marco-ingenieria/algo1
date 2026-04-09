'''
SECCIÓN DECLARATIVA

Descripción: El programa toma dos enteros del usuario y los divide mediante restas sucesivas

Casos de prueba: -

Recursos:
    -p, q: dividendo y divisor
    -cociente: lleva la cuenta de las restas, o sea, el progreso de la división hasta llegar a su resultado final
    -resto: el resto tras la última resta posible
'''

# 1. Prólogo
print("Ingresar ambos enteros:")
p_s = input()
p = int(p_s)

q_s = input()
q = int(q_s)

if q == 0:
    print("Error: división por cero")
else:

# 2. Resolución
    cociente = 0
    resto = abs(p)

    while resto >= abs(q):
        resto -= abs(q)
        cociente += 1

    if p < 0:
        resto *= -1
        if q >= 0:
            cociente *= -1
    else:
        if q < 0:
            cociente *= -1

# 3. Epílogo
    print(f"El resultado es {cociente} y el resto es {resto}")
