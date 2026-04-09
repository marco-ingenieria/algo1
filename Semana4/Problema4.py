'''
SECCIÓN DECLARATIVA

Descripción: Programa que encuentra una cantidad dada de números perfectos usando los primos de Mersenne

Casos de prueba:
    +

Recursos:
    +
'''

#Funciones
def es_primo(num):
    '''
    Determina si el número ingresado es primo, evaluando que sus divisores no sean más que el 1
    Recibe el número a confirmar o rechazar como primo
    Devuelve True si es primo y False si no lo es
    '''
    return suma(num) > 1 

def mersenne(p):
    '''
    Calcula el número de Mersenne para un exponente dado
    Recibe el exponente
    Retorna el número de Mersenne
    '''
    return (2 ** p) - 1

def perfecto_desde_mersenne(p):
    '''
    Calcula el número perfecto asociado a un número primo mediante su número de Mersenne
    Recibe el número primo a evaluar.
    Devuelve el número perfecto asociado
    '''
    mersenne = mersenne(p)
    return mersenne * (2 ** (p-1))

def suma_divisores_propios(num):
    '''
    Busca la suma de todos los divisores propios de un número dado
    Recibe el número a evaluar
    Devuelve la suma
    '''
    suma = 0
    raiz = math.floor(num ** 0.5)

    for i in range(1, raiz + 1):
        if num != i and num % i == 0:
            suma += i
            if (num / i) > raiz and (num / i) != num:
                suma += (num / i)

    return suma

#Sección algorítmica
#1. Prólogo

#2. Resoulción
if es_primo(p) and es_primo(mersenne):


#3. Epílogo
