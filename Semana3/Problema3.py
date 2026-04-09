'''
SECCIÓN DECLARATIVA

Descripción: El programa calcula la sucesión de collatz y la sucesión de números malabaristas desde el número ingresado por el usuario hasta 1. 
             Muestra en cada caso la cantidad de pasos que ejecutó y el valor más alto al que llegó

Casos de prueba: -

Recursos:
    -n: valor inicial introducido por el usuario
    -valor_collatz: copia de n para la sucesión de collatz
    -valor_malabarista: copia de n para la sucesión de números malabaristas
    -max_collatz: valor máximo de la sucesión de collatz desde n
    -max_malabarista: valor máximo de la sucesión de números malabaristas desde n
    -pasos_collatz: cantidad de repeticiones de la sucesión de collatz desde n
    -pasos_malabarista: cantidad de repeticiones de la sucesión de números malabaristas desde n

'''

import math

# 1. Prólogo
n_s = input("Ingresar número entero:\n")
n = int(n_s)

# 2. Resolución
# 2.1 Sucesión de collatz
valor_collatz = n
max_collatz = n
pasos_collatz = 0

while valor_collatz != 1:
    if valor_collatz % 2 == 0:
        valor_collatz //= 2
    else:
        valor_collatz *= 3
        valor_collatz += 1
    
    pasos_collatz += 1
    if valor_collatz > max_collatz:
        max_collatz = valor_collatz

# 2.2 Sucesión de números malabaristas
valor_malabarista = n
max_malabarista = n
pasos_malabarista = 0

while valor_malabarista != 1:
    if valor_malabarista % 2 == 0:
        valor_malabarista **= 0.5
        valor_malabarista = math.floor(valor_malabarista)
    else:
        valor_malabarista **= 1.5
        valor_malabarista = math.floor(valor_malabarista)

    pasos_malabarista += 1
    if valor_malabarista > max_malabarista:
        max_malabarista = valor_malabarista

# 3. Epílogo
print(f"La serie de Collatz para {n} dura {pasos_collatz} pasos y su valor máximo fue {max_collatz}")
print(f"La serie de números malabaristas para {n} dura {pasos_malabarista} pasos y su valor máximo fue {max_malabarista}")
