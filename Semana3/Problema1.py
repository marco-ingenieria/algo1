'''
SECCIÓN DECLARATIVA

Descripción: El programa toma dos enteros del usuario y los multiplica mediante sumas sucesivas

Casos de prueba: -

Recursos:
    -num1, num2: factores
    -acumulador: acumula el progreso de la multiplicación hasta llegar a su resultado final
'''

# 1. Prólogo
print("Ingresar ambos enteros:")
num1_s = input()
num1 = int(num1_s)

num2_s = input()
num2 = int(num2_s)

# 2. Resolución
acumulador = 0

if abs(num1) > abs(num2):
    for i in range(abs(num2)):
        acumulador += num1
    if num2 < 0:
        acumulador *= -1
else:
    for i in range(abs(num1)):
            acumulador += num2
    if num1 < 0:
        acumulador *= -1

# 3. Epílogo
print(f"El resultado es {acumulador}")
