'''
SECCIÓN DECLARATIVA

Descripción: Programa que toma un numero entero hasta la magnitud de los miles de millones y lo expresa en palabras (como cardinal)

Casos de prueba:

Recursos:
    +
'''

def unidades_a_texto(num_u, es_grupo):
    '''
    Pasa el dígito de las unidades a texto
    Recibe un entero del 0 al 9
    Si es un grupo de miles o millones se cambia "uno" a "un"
    Retorna el string representando las unidades
    '''
    unidades = ""
    if num_u == 1:
        if es_grupo:
            unidades = "ún"
        else:
            unidades = "uno"
    elif num_u == 2:
        unidades = "dos"
    elif num_u == 3:
        unidades = "tres"
    elif num_u == 4:
        unidades = "cuatro"
    elif num_u == 5:
        unidades = "cinco"
    elif num_u == 6:
        unidades = "seis"
    elif num_u == 7:
        unidades = "siete"
    elif num_u == 8:
        unidades = "ocho"
    elif num_u == 9:
        unidades = "nueve"

    return unidades

def decenas_a_texto(num_d, es_grupo):
    '''
    Pasa las decenas a texto
    Recibe un entero del 0 al 99
    Retorna el string representando las decenas
    '''
    num_u = num_d % 10
    unidades = unidades_a_texto(num_u, es_grupo)
    decenas = ""
    if num_u == num_d:
        decenas = unidades
    elif num_d == 10:
        decenas = "diez"
    elif num_d == 11:
        decenas = "once"
    elif num_d == 12:
        decenas = "doce"
    elif num_d == 13:
        decenas = "trece"
    elif num_d == 14:
        decenas = "catorce"
    elif num_d == 15:
        decenas = "quince"
    elif num_d < 20:
        decenas = f"dieci{unidades}"
    elif num_d == 20:
        decenas = "veinte"
    elif num_d < 30:
        decenas = f"veinti{unidades}"
    elif num_d < 40:
        decenas = "treinta"
    elif num_d < 50:
        decenas = "cuarenta"
    elif num_d < 60:
        decenas = "cincuenta"
    elif num_d < 70:
        decenas = "sesenta"
    elif num_d < 80:
        decenas = "setenta"
    elif num_d < 90:
        decenas = "ochenta"
    elif num_d < 100:
        decenas = "noventa"

    if num_u > 0 and num_d > 30:
        decenas += f" y {unidades}"

    return decenas

def grupo_a_texto(num_c, es_grupo):
    '''
    Pasa un grupo de tres dígitos (unidades, miles, millones) a texto
    Recibe un entero del 0 al 999 (cantidad de unidades, de miles y de millones)
    Retorna el string representando el grupo
    '''
    num_d = num_c % 100
    decenas = decenas_a_texto(num_d, es_grupo)
    centenas = ""
    if num_d == num_c:
        centenas = decenas
    elif num_c == 100:
        centenas = "cien"
    elif num_c < 200:
        centenas = f"ciento {decenas}"
    elif num_c < 300:
        centenas = f"doscientos {decenas}"
    elif num_c < 400:
        centenas = f"trescientos {decenas}"
    elif num_c < 500:
        centenas = f"cuatrocientos {decenas}"
    elif num_c < 600:
        centenas = f"quinientos {decenas}"
    elif num_c < 700:
        centenas = f"seiscientos {decenas}"
    elif num_c < 800:
        centenas = f"setecientos {decenas}"
    elif num_c < 900:
        centenas = f"ochocientos {decenas}"
    elif num_c < 1000:
        centenas = f"novecientos {decenas}"

    return centenas

def numero_a_texto(num):
    '''
    Pasa un número a texto separándolo en tres grupos para cada uno de los cuales se le aplicará "grupo_a_texto()"
    Recibe el número a transformar
    Maneja las excepciones para el mil y el millón singular
    Retorna el string del número como texto
    '''
    num_c = num % 1000
    num_mc = (num % 1000000) // 1000
    num_mmc = (num % 1000000000) // 1000000
    numero_texto = ""

    if num_mmc:
        if num_mmc == 1:
            numero_texto += f"{grupo_a_texto(num_mmc, True)} millón "
        else:
            numero_texto += f"{grupo_a_texto(num_mmc, True)} millones "
    if num_mc:
        if num_mc == 1:
            numero_texto += "mil "
        else:
            numero_texto += f"{grupo_a_texto(num_mc, True)} mil "
    numero_texto += grupo_a_texto(num_c, False)

    return numero_texto

#1. Prólogo
num_s = input("Ingresar número\n")
num = int(num_s)

#2. Resolución
cardinal = numero_a_texto(num)

#3. Epílogo
print(cardinal)
