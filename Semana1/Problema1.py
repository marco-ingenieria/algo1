'''
SECCIÓN DECLARATIVA
Descripción: Calcular el equivalente de una temperatura en Celsius, en Fahrenheit y en Kelvin

'''

#1. Prólogo
print("-- Conversor de temperaturas --")

#2. Resolución
#2.1. Ingreso de datos en escala Celsius
gradoC_s = input("Ingrese grados en centígrados: ")
gradoC = float(gradoC_s)

#2.2 Conversión de temperatura a Fahrenheit y Kelvin
gradoF = (gradoC * (9/5)) + 32
gradoK = gradoC + 273.15

#3. Epílogo
print(f"La temperatura en Fahrenheit sería {gradoF: .2f}")
print(f"La temperatura en Kelvin sería {gradoK: .2f}")