from random import sample, seed 
import math

def busqueda_binaria_rec(datos, clave, izq, der, nivel):
    # Caso base: región vacía
    nivel += 1
    if izq > der:
        return -1, nivel
    

    medio = (izq + der) // 2

    # Caso base: encontrado
    if datos[medio] == clave:
        return medio, nivel
    # Caso recursivo: buscar en la mitad correspondiente
    elif clave < datos[medio]:
        return busqueda_binaria_rec(datos, clave, izq, medio - 1, nivel)
    else:
        return busqueda_binaria_rec(datos, clave, medio + 1, der, nivel) 


seed(42)
n = 10000
lista = sample(range(1, 10 * n), n)
lista.sort()

lista_claves = sample(lista, 5)
lista_claves += [lista[0], lista[-1], -1, -2, -3, -4, -5]

for i in range(len(lista_claves)):
    binaria_valor, binaria_contador  = busqueda_binaria_rec(lista, lista_claves[i], 0, len(lista) -1, 0)
    print(f"Busqueda binaria: Se encontró {lista_claves[i]} en la posición {binaria_valor} en {binaria_contador} búsquedas")