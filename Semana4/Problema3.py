'''
SECCIÓN DECLARATIVA
Descripción: Calcula el producto entre dos enteros mediante el algoritmo de la campesina rusa

Casos de prueba:
    +

Recursos:
    +
'''
#Funciones
def campesina_rusa(x, y):
    '''
    Calcula un producto entre dos enteros positivos usando el algoritmo de la campesina rusa
    Recibe ambos números como parámetros
    Retorna el resultado como entero
    '''
    resultado = 0
    while y > 0:
        if y & 1 == 1:
            resultado += x
        x = x << 1
        y = y >> 1

    return resultado

def multiplicar(x, y):
    '''
    Llama a "campesina_rusa()" para el valor absoluto de los factores recibidos y determina el signo del resultado
    Recibe ambos números como parámetros
    Retorna el resultado como entero
    '''
    resultado = campesina_rusa(abs(x), abs(y))
    if (x < 0 and y > 0) or (y < 0 and x > 0):
        resultado *= -1

    return resultado

#Sección Algorítmica
#1. Prólogo
num1_s = input("Ingresar un entero:\n")
num1 = int(num1_s)

num2_s = input("Ingresar otro entero:\n")
num2 = int(num2_s)

#2. Resolución
resultado = multiplicar(num1, num2)

#3. Epílogo
print(f"{num1} * {num2} = {resultado}")
