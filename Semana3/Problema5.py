'''
SECCIÓN DECLARATIVA

Descripción: El programa evalúa si un dado número es perfecto, abundante o deficiente.
             La suma de los divisores propios de un número perfecto es el mismo número.
             La suma de los divisores propios de un número deficiente es menor que el número.
             La suma de los divisores propios de un número abundante es mayor que el número.

Casos de prueba: -

Recursos:
    -num: número ingresado por el usuario
    -raiz: raiz cuadrada del número ingresado por el usuario
    -suma: acumulador de los divisores
    -i: contador
    -tipo: string representando la categoría del número
'''
import math

# 1. Prólogo
num_s = input("Ingresar un número entero\n")
num = int(num_s)

# 2. Resolución
tipo = ""
suma = 0
raiz = math.floor(num ** 0.5)

for i in range(1, raiz + 1):
    if num != i and num % i == 0:
        suma += i
        if (num / i) > raiz and (num / i) != num:
            suma += (num / i)

if suma > num:
    tipo = "abundante"
elif suma < num:
    tipo = "deficiente"
else:
    tipo = "perfecto!"

# 3. Epílogo
print(f"La suma es {suma}")
print(f"El número es {tipo}")
