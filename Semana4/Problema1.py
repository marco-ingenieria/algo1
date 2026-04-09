'''
SECCIÓN DECLARATIVA

Descripción: Programa que toma un número decimal y lo expresa como número romano

Casos de prueba: -

Recursos:
    + num: número del 1 al 3999 ingresado por el usuario
    + num_u, num_d, num_c, num_m: los cuatro dígitos extraidos de num
    + unidades, decenas, centenas, millares: substrings de la cadena final, uno por cada dígito
'''

#Funciones
def convertir_digito(digito, char1, char5, char10):
    '''
    Convierte un dígito (sin importar cuál potencia de 10) a romano.
    Recibe el dígito a convertir y tres caracteres: uno para representar el multiplo por uno, otro para el cinco y otro para el diez
    Devuelve el string correspondiente para el dígito
    '''
    num_romano = ""
    if digito != 0:
        num_romano += ((digito < 5) * ((digito % 4) + (digito // 4))) * char1
        num_romano += ((digito + 1) // 5) % 2 * char5
        num_romano += ((digito > 5) * ((digito - 5) % 4) + ((digito - 5) // 4)) * char1
        num_romano += (digito // 9) * char10
    
    return num_romano

def convertir_decimal(num):
    '''
    Convierte el número completo a romano
    Recibe el número a traducir y devuelve el string completo
    '''
    #1. Obtención de los dígitos
    num_u = num % 10
    num_d = (num % 100) // 10
    num_c = (num % 1000) // 100
    num_m = num // 1000

    #2. Conversion de cada dígito a romano
    unidades = convertir_digito(num_u, "I", "V", "X")
    decenas = convertir_digito(num_d, "X", "L", "C")
    centenas = convertir_digito(num_c, "C", "D", "M")
    millares = convertir_digito(num_m, "M", "M", "M")

    return f"{millares}{centenas}{decenas}{unidades}"

def validar_entrada(num, lim_min, lim_max):
    '''
    Valida que la entrada esté dentro de un cierto rango
    Recibe el número a verificar, el valor mínimo (inclusivo) y el valor máximo (inclusivo)
    Retorna verdadero si el número está dentro de los límites y False en caso contrario
    '''
    return num >= lim_min and num <= lim_max

#Sección algorítmica
#1. Prólogo
num_s = input("Ingresar un número del 1 al 3999\n")
num = int(num_s)

if validar_entrada(num, 1, 3999):

#2. Resolución
    romano = convertir_decimal(num)

#3. Epílogo
print(romano)
