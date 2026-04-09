'''
SECCIÓN DECLARATIVA
BUG - NO AJUSTA BIEN PARA ENERO Y FEBRERO
'''

#1. Prólogo
print("-- --")

#2. Resolución
#2.1. 
fecha_string = input("Ingresar fecha\n")
fecha = int(fecha_string)
fecha_y = fecha // 10000
fecha_m = (fecha // 100) % 100
fecha_d = fecha % 100

#2.2. 
if fecha_m <= 2:
    fecha_m += 12
    fecha_y -= 1

fecha_K = fecha_y % 100
fecha_J = fecha_y // 100

#2.3.
h = (fecha_d + (13 * (fecha_m + 1) // 5) + fecha_K + (fecha_K // 4) + (fecha_J // 4) - (2 * fecha_J)) % 7
if h == 0:
    nombre_dia = "Sábado"
elif h == 1:
    nombre_dia = "Domingo"
elif h == 2:
    nombre_dia = "Lunes"
elif h == 3:
    nombre_dia = "Martes"
elif h == 4:
    nombre_dia = "Miércoles"
elif h == 5:
    nombre_dia = "Jueves"
elif h == 6:
    nombre_dia = "Viernes"
#3. Epílogo
print(f"El {fecha_d}/{fecha_m}/{fecha_y} es {nombre_dia}")
