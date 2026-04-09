'''
SECCIÓN DECLARATIVA

Descripción: El programa determina si un número dado es "feliz".
             Un número es feliz si se puede llegar a 1 sumando los cuadrados de sus dígitos sucesivamente.
             Si el número es infeliz, eventualmente entra en un ciclo particular de ocho números que contiene el 4.

Casos de prueba: -

Recursos:
    -num: número base ingresado por el usuario
    -cadena: secuencia de números representada como un string
    -suma, dígito: acumuladores auxiliares
'''

# 1. Prólogo
print("Ingresar el número entero:")
num_s = input()
num = int(num_s)

# 2. Resolución
cadena = ""
while num != 1 and num != 4:
    suma = 0
    while num > 0:
        digito = num % 10
        suma += digito ** 2
        num //= 10
    print(suma, end = " -> ")
    num = suma

# 3. Epílogo
print("Fin")
if num == 1:
    print("Número feliz :]")
if num == 4:
    print("Número infeliz :[")


