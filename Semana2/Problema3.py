'''
SECCIÓN DECLARATIVA

'''

#1. Prólogo
print("--  --")

#2. Resolución
#2.1. Entrada del usuario
num_s = input("Ingresar un número del 1 al 3999\n")
num = int(num_s)

#2.2. Unidades
num_u = num % 10
unidades = ""
if num_u != 0:
    unidades += ((num_u < 5) * ((num_u % 4) + (num_u // 4))) * "I"
    unidades += ((num_u + 1) // 5) % 2 * "V"
    unidades += ((num_u > 5) * ((num_u - 5) % 4) + ((num_u - 5) // 4)) * "I"
    unidades += (num_u // 9) * "X"

#2.3 Decenas
num_d = (num % 100) // 10
decenas = ""
if num_d != 0:
    decenas += ((num_d < 5) * ((num_d % 4) + (num_d // 4))) * "X"
    decenas += ((num_d + 1) // 5) % 2 * "L"
    decenas += ((num_d > 5) * ((num_d - 5) % 4) + ((num_d - 5) // 4)) * "X"
    decenas += (num_d // 9) * "C"

#2.4 Centenas
num_c = (num % 1000) // 100
centenas = ""
if num_c != 0:
    centenas += ((num_c < 5) * ((num_c % 4) + (num_c // 4))) * "C"
    centenas += ((num_c + 1) // 5) % 2 * "D"
    centenas += ((num_c > 5) * ((num_c - 5) % 4) + ((num_c - 5) // 4)) * "C"
    centenas += (num_c // 9) * "M"

#2.5. Millares
num_m = num // 1000
millares = num_m * "M"

#3. Epílogo
print(f"{millares}{centenas}{decenas}{unidades}")
