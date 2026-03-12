'''
SECCIÓN DECLARATIVA
Descripción: Calcular el n-ésimo valor de la secuencia Fibonacci usando la fórmula de Binet

'''

#1. Prólogo
print("-- --")
print("Ingrese los valores de a,b y c:")
a_s = input("a: ")
a = int(a_s)
b_s = input("b: ")
b = int(b_s)
c_s = input("c: ")
c = int(c_s)

#2. Resolución
#2.1. Definición del número de oro y su conjugado

dis = b ** 2 - 4*a*c

if(dis == 0):
    r = -b / (2*a)
    print("Es solo una raiz")
    print(f'raiz: {r}')
else:
    rDis = dis**(0.5)

    r1 = (-b + (rDis)) / (2*a)
    r2 = (-b - (rDis)) / (2*a)


    #2.2 Ingreso del número por el usuario

    #2.2 Cálculo de la secuencia fibonacci según la fórmula de Binet

    #3. Epílogo
    print(f"{round(r1.real)}{r1.imag} - {round(r2.real)}{r2.imag}")
