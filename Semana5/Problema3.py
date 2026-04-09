import random

def busqueda_lineal(datos, clave, contar = False):
    '''
    '''
    contador = 0
    n = len(datos)

    i = 0
    while i < n and datos[i] != clave:
        if contar:
            contador += 1
        i += 1

    if i < n:
        return i, contador if contar else i
    else:
        return -1, contador if contar else -1   

def busqueda_lineal_mtf(datos, clave,contar = False):
    '''Búsqueda lineal con heurística Move-to-Front.
       Si encuentra la clave, la mueve a la posición 0.'''
    contador = 0
    n = len(datos)
    i = 0
    while i < n and datos[i] != clave:
        if contar:
            contador += 1
        i += 1

    if i < n:
        # Encontrado: mover al frente
        elemento = datos.pop(i)   # extraer de posición i
        datos.insert(0, elemento) # insertar al inicio
        return 0,contador if contar else 0               # ahora está en posición 0
    else:
        return -1,contador if contar else -1

def busqueda_lineal_transpose(datos, clave):
    '''Búsqueda lineal con heurística de Transposición.
    Si encuentra la clave, la intercambia con el anterior.'''
    n = len(datos)
    i = 0
    while i < n and datos[i] != clave:
        if contar:
                contador += 1
        i += 1

    if i < n:
        if i > 0:  # no intercambiar si ya está en posición 0
            # Intercambio con el anterior (swap)
            datos[i], datos[i - 1] = datos[i - 1], datos[i]
            return i - 1, contador if contar else i-1  # nueva posición
        else:
            return 0, contador if contar else 0      # ya estaba al inicio
    else:
        return -1, contador if contar else -1


datos = list(range(200))

clave_frecuentes = random.choices(datos, k=5)

lista = random.choices(clave_frecuentes,k = 700)

lista += random.choices(range(200), k=300)
random.shuffle(lista)