'''
SECCIÓN DECLARATIVA
Descripción: Representar una fecha y hora (año, mes, día, horas, minutos) en formato fraccionario
La parte entera representa la fecha y la fraccionaria, la hora y minutos

'''

#1. Prólogo
print("--Pasaje de fecha y hora a un valor fraccionario--")

#2. Resolución
#2.1. Ingreso de datos de la fecha
print("Ingrese los datos de la fecha y la hora")
dia_s = input("dia: ")
dia = int(dia_s)
mes_s = input("mes: ")
mes = int(mes_s)
año_s = input("año: ")
año = int(año_s)
hora_s = input("hora: ")
hora = int(hora_s)
minuto_s = input("minuto: ")
minuto = int(minuto_s)

#2.2 Cálculo de la fecha en formato fraccionario
entera = año * 10000 + mes * 100 + dia
fraccion = hora /24 + minuto/(60*24)
fecha_completa = entera + fraccion

#3. Epílogo
print(f"La fecha como un numero seria {fecha_completa: .6f}")
