'''
SECCIÓN DECLARATIVA

'''

#1. Prólogo
print("--  --")

#2. Resolución
#2.1. Se toman ambas fechas como entrada y se determina cuál es la mayor y cuál es la menor
fecha_1_string = input("Ingresar fecha 1\n")
fecha_1 = int(fecha_1_string)

fecha_2_string = input("Ingresar fecha 2\n")
fecha_2 = int(fecha_2_string)

if fecha_1 > fecha_2:
    fecha_y_mayor = fecha_1 // 10000
    fecha_m_mayor = (fecha_1 // 100) % 100
    fecha_d_mayor = fecha_1 % 100
    fecha_y_menor= fecha_2 // 10000
    fecha_m_menor = (fecha_2 // 100) % 100
    fecha_d_menor = fecha_2 % 100
else:
    fecha_y_mayor = fecha_2 // 10000
    fecha_m_mayor = (fecha_2 // 100) % 100
    fecha_d_mayor = fecha_2 % 100
    fecha_y_menor = fecha_1 // 10000
    fecha_m_menor = (fecha_1 // 100) % 100
    fecha_d_menor = fecha_1 % 100

#2.2. Se calcula la diferencia en cada componente de la fecha
dif_d = fecha_d_mayor - fecha_d_menor
dif_m = fecha_m_mayor - fecha_m_menor
dif_y = fecha_y_mayor - fecha_y_menor

#2.3. Se compensan las diferencias que hayan salido negativas y se corrige el año bisiesto
if dif_d < 0:
    mes_anterior = ((fecha_m_mayor + 10) % 12) + 1
    if mes_anterior in [1, 3, 5, 7, 8, 10, 12]:
        prestamo = 31
    elif mes_anterior == 2:
        if (fecha_y_mayor % 4 == 0 and not fecha_y_mayor % 100 == 0) or fecha_y_mayor % 400 == 0:
            prestamo = 29
        else:
            prestamo = 28
    else:
        prestamo = 30
    dif_d += prestamo
    dif_m -= 1

if dif_m < 0:
    dif_m += 12
    dif_y -= 1

#3. Epílogo
print(f"La diferencia es de {dif_y} años, {dif_m} meses y {dif_d} días")
