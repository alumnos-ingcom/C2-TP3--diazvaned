################
# Vanesa Díaz - @diazvaned
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


import tp4ej1 as soporte


def minimo(lista):
    n = 0
    aux = 1
    for i in range (len(lista)):
        if (lista[i] < lista[n]):
            aux = lista[i]
            n = n+1
    return aux
    
def maximo(lista):
    n = 0
    aux = 1
    for i in range (len(lista)):
        if (lista[i] > lista[n]):
            aux = lista[i]
            n = n+1
    return aux

def prueba ():
    lista =[]
    for i in range (5):
        elemento = soporte.ingreso_entero("Ingrese un numero entero")
        lista.append(elemento)
    min = minimo(lista)
    print (f"Minimo: {min}")
    max = maximo(lista)
    print (f"Maximo: {max}")

if __name__ == "__main__":
    prueba()