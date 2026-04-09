'''
SECCIÓN DECLARATIVA

Descripción: El programa calcula una aproximación de pi usando una cantidad de términos de la serie de Leibniz/serie de Nilakantha dada por el usuario

Casos de prueba: -

Recursos:
    -k: pasos de la serie, ingresados por el usuario
    -i, j: contadores
    -signo: valor auxiliar para alternar los términos
    -suma_leibniz: acumulador de la serie de Leibniz
    -suma_nilakantha: acumulador de la serie de Nilakantha
    -error_leibniz: error respecto del pi de referencia de la serie de Leibniz
    -error_nilakantha: error respecto del pi de referencia de la serie de Nilakantha
'''
import math

# 1. Prólogo
k_s = input("Ingresar la cantidad de términos:\n")
k = int(k_s)

# 2. Resolución
# 2.1 Leibniz
suma_leibniz = 0
signo = 1
for i in range(k):
    suma_leibniz += signo / (1 + (2 * i))
    signo *= -1

suma_leibniz *= 4
error_leibniz = abs(suma_leibniz - math.pi)

# 2.2 Nilakantha
suma_nilakantha = 3
signo = 4

for j in range(1, k+1):
    suma_nilakantha += signo / ((2 * j) * ((2 * j) + 1) * ((2 * j) + 2)) 
    signo *= -1

error_nilakantha = abs(suma_nilakantha - math.pi)

# 3. Epílogo
print(f"La serie de Leibniz en {k} términos es {suma_leibniz}, con un error de {error_leibniz}")
print(f"La serie de Nilakantha en {k} términos es {suma_nilakantha}, con un error de {error_nilakantha}")
