'''
SECCIÓN DECLARATIVA
Descripción: Calcular el índice de masa corporal basado en el peso y la estatura de una persona

'''

#1. Prólogo
print("-- Medidor de masa corporal --")

#2. Resolución
#2.1. Ingreso de datos de la persona
peso_s = input("Ingrese el peso en kg: ")
peso = float(peso_s)
estatura_s = input("Ingrese la estatura en m: ")
estatura = float(estatura_s)

#2.2 Cálculo del Índice de Masa Corporal
imc = peso / (estatura ** 2)

#3. Epílogo
print(f"El índice de masa corporal sería {imc: .2f}")