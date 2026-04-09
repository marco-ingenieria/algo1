'''
Sección declarativa
'''
from random import sample, seed 

#Funciones
def busqueda_lineal(datos, clave, contar = False):
    '''
    '''
    contador = 0
    n = len(datos)

    i = 0
    while i < n and datos[i] != clave:
        if contar:
            contador += 1
        i += 1

    if i < n:
        return i, contador if contar else i
    else:
        return -1, contador if contar else -1     

def busqueda_binaria(datos, clave, contar = False):
    contador = 0
    izq = 0
    der = len(datos) - 1

    while izq <= der:
        if contar:
            contador += 1
        medio = (izq + der) // 2

        if datos[medio] == clave:
            return medio, contador if contar else medio
        elif clave < datos[medio]:
            der = medio - 1
        else:
            izq = medio + 1

    return -1, contador if contar else -1



#1. Prólogo


#2. Resolución
seed(42)
n = 1000
lista = sample(range(1, 10 * n), n)
lista.sort()

lista_claves = sample(lista, 5)
lista_claves += [lista[0], lista[-1], -1, -2, -3, -4, -5]

print(lista_claves)
for i in range(len(lista_claves)):
    binaria_valor, binaria_contador  = busqueda_binaria(lista, lista_claves[i], True)
    lineal_valor, lineal_contador = busqueda_lineal(lista, lista_claves[i], True)
    print(f"Busqueda binaria: Se encontró {lista_claves[i]} en la posición {binaria_valor} en {binaria_contador} búsquedas")
    print(f"Busqueda lineal: Se encontró {lista_claves[i]} en la posición {lineal_valor} en {lineal_contador} búsquedas")

    print(" - - - - - - - - - - - - - -")
#3. Epílogo
