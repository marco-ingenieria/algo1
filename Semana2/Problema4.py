'''
SECCIÓN DECLARATIVA

'''

#1. Prólogo
print("--  --")

#2. Resolución
#2.1. Entrada del usuario
num_s = input("Ingresar número\n")
num = int(num_s)

#2.2. Unidades
num_u = num % 10
unidades = ""
if num_u == 1:
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

#2.3 Decenas
num_d = num % 100
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

#2.4 Centenas
num_c = num % 1000
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

#2.5. Millares
#2.5.1. Unidades de millares
num_mu = (num % 10000) // 1000
unidades_de_millares = ""
singular = False
if num_mu == 1:
    if num % 10000 != num:
        unidades_de_millares = "un"
    else:
        singular = True
elif num_mu == 2:
    unidades_de_millares = "dos"
elif num_mu == 3:
    unidades_de_millares = "tres"
elif num_mu == 4:
    unidades_de_millares = "cuatro"
elif num_mu == 5:
    unidades_de_millares = "cinco"
elif num_mu == 6:
    unidades_de_millares = "seis"
elif num_mu == 7:
    unidades_de_millares = "siete"
elif num_mu == 8:
    unidades_de_millares = "ocho"
elif num_mu == 9:
    unidades_de_millares = "nueve"

#2.5.2. Decenas de millares
num_md = (num % 100000) // 1000
decenas_de_millares = ""
if num_mu == num_md:
    decenas_de_millares = unidades_de_millares
elif num_md == 10:
    decenas_de_millares = "diez"
elif num_md == 11:
    decenas_de_millares = "once"
elif num_md == 12:
    decenas_de_millares = "doce"
elif num_md == 13:
    decenas_de_millares = "trece"
elif num_md == 14:
    decenas_de_millares = "catorce"
elif num_md == 15:
    decenas_de_millares = "quince"
elif num_md < 20:
    decenas_de_millares = f"dieci{unidades_de_millares}"
elif num_md == 20:
    decenas_de_millares = "veinte"
elif num_md < 30:
    decenas_de_millares = f"veinti{unidades_de_millares}"
elif num_md < 40:
    decenas_de_millares = "treinta"
elif num_md < 50:
    decenas_de_millares = "cuarenta"
elif num_md < 60:
    decenas_de_millares = "cincuenta"
elif num_md < 70:
    decenas_de_millares = "sesenta"
elif num_md < 80:
    decenas_de_millares = "setenta"
elif num_md < 90:
    decenas_de_millares = "ochenta"
elif num_md < 100:
    decenas_de_millares = "noventa"

if num_mu > 0 and num_md > 30:
    decenas_de_millares += f" y {unidades_de_millares}"

#2.5.3. Centenas de millares
num_mc = (num % 1000000) // 1000
centenas_de_millares = ""
if num_md == num_mc:
    centenas_de_millares = decenas_de_millares
elif num_mc == 100:
    centenas_de_millares = "cien"
elif num_mc < 200:
    centenas_de_millares = f"ciento {decenas_de_millares}"
elif num_mc < 300:
    centenas_de_millares = f"doscientos {decenas_de_millares}"
elif num_mc < 400:
    centenas_de_millares = f"trescientos {decenas_de_millares}"
elif num_mc < 500:
    centenas_de_millares = f"cuatrocientos {decenas_de_millares}"
elif num_mc < 600:
    centenas_de_millares = f"quinientos {decenas_de_millares}"
elif num_mc < 700:
    centenas_de_millares = f"seiscientos {decenas_de_millares}"
elif num_mc < 800:
    centenas_de_millares = f"setecientos {decenas_de_millares}"
elif num_mc < 900:
    centenas_de_millares = f"ochocientos {decenas_de_millares}"
elif num_mc < 1000:
    centenas_de_millares = f"novecientos {decenas_de_millares}"

if centenas_de_millares or singular:
    centenas_de_millares += " mil "
centenas_de_millares += centenas

#2.6. Millones
#2.6.1. Unidades de millones
num_mmu = (num % 10000000) // 1000000
unidades_de_millones = ""
plural = True
if num_mmu == 1:
    unidades_de_millones = "un"
    if num % 10000000 == num:
        plural = False
elif num_mmu == 2:
    unidades_de_millones = "dos"
elif num_mmu == 3:
    unidades_de_millones = "tres"
elif num_mmu == 4:
    unidades_de_millones = "cuatro"
elif num_mmu == 5:
    unidades_de_millones = "cinco"
elif num_mmu == 6:
    unidades_de_millones = "seis"
elif num_mmu == 7:
    unidades_de_millones = "siete"
elif num_mmu == 8:
    unidades_de_millones = "ocho"
elif num_mmu == 9:
    unidades_de_millones = "nueve"

#2.6.2. Decenas de millones
num_mmd = (num % 100000000) // 1000000
decenas_de_millones = ""
if num_mmu == num_mmd:
    decenas_de_millones = unidades_de_millones
elif num_mmd == 10:
    decenas_de_millones = "diez"
elif num_mmd == 11:
    decenas_de_millones = "once"
elif num_mmd == 12:
    decenas_de_millones = "doce"
elif num_mmd == 13:
    decenas_de_millones = "trece"
elif num_mmd == 14:
    decenas_de_millones = "catorce"
elif num_mmd == 15:
    decenas_de_millones = "quince"
elif num_mmd < 20:
    decenas_de_millones = f"dieci{unidades_de_millones}"
elif num_mmd == 20:
    decenas_de_millones = "veinte"
elif num_mmd < 30:
    decenas_de_millones = f"veinti{unidades_de_millones}"
elif num_mmd < 40:
    decenas_de_millones = "treinta"
elif num_mmd < 50:
    decenas_de_millones = "cuarenta"
elif num_mmd < 60:
    decenas_de_millones = "cincuenta"
elif num_mmd < 70:
    decenas_de_millones = "sesenta"
elif num_mmd < 80:
    decenas_de_millones = "setenta"
elif num_mmd < 90:
    decenas_de_millones = "ochenta"
elif num_mmd < 100:
    decenas_de_millones = "noventa"

if num_mmu > 0 and num_mmd > 30:
    decenas_de_millones += f" y {unidades_de_millones}"

#2.6.3. Centenas de millones
num_mmc = (num % 1000000000) // 1000000
centenas_de_millones = ""
if num_mmd == num_mmc:
    centenas_de_millones = decenas_de_millones
elif num_mmc == 100:
    centenas_de_millones = "cien"
elif num_mmc < 200:
    centenas_de_millones = f"ciento {decenas_de_millones}"
elif num_mmc < 300:
    centenas_de_millones = f"doscientos {decenas_de_millones}"
elif num_mmc < 400:
    centenas_de_millones = f"trescientos {decenas_de_millones}"
elif num_mmc < 500:
    centenas_de_millones = f"cuatrocientos {decenas_de_millones}"
elif num_mmc < 600:
    centenas_de_millones = f"quinientos {decenas_de_millones}"
elif num_mmc < 700:
    centenas_de_millones = f"seiscientos {decenas_de_millones}"
elif num_mmc < 800:
    centenas_de_millones = f"setecientos {decenas_de_millones}"
elif num_mmc < 900:
    centenas_de_millones = f"ochocientos {decenas_de_millones}"
elif num_mmc < 1000:
    centenas_de_millones = f"novecientos {decenas_de_millones}"

if centenas_de_millones:
    if plural:
        centenas_de_millones += " millones "
    else:
        centenas_de_millones += " millón "

centenas_de_millones += centenas_de_millares
#3. Epílogo
print(centenas_de_millones)
