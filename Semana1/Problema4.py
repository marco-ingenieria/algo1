'''
SECCIÓN DECLARATIVA
Descripción: Calcular el n-ésimo valor de la secuencia Fibonacci usando la fórmula de Binet

'''

#1. Prólogo
print("-- --")

#2. Resolución
#2.1. Definición del número de oro y su conjugado
numOro = (1 + (5 ** (1/2))) / 2
conjugadoNumOro = (1 - (5 ** (1/2))) / 2

#2.2 Ingreso del número por el usuario
numUsuario_s = input("Ingrese un número entero no negativo: ")
numUsuario = int(numUsuario_s)

#2.2 Cálculo de la secuencia fibonacci según la fórmula de Binet
resultado = ((numOro ** numUsuario) - (conjugadoNumOro ** numUsuario)) / (5 ** (1/2))
resultadoEntero = round(resultado)

#3. Epílogo
print(f"El {numUsuario}-ésimo número de la secuencia Fibonacci es: {resultadoEntero}")
