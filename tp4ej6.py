################
# Vanesa Díaz - @diazvaned
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


import tp4ej1 as soporte


def minimo(lista):
    aux = 0
    for i in range (len(lista)):
        if (lista[i] < aux):
            aux = lista[i]
    return aux
    
def maximo(lista):
    aux = 0
    for i in range (len(lista)):
        if (lista[i] > aux):
            aux = lista[i]
    return aux

def prueba ():
    lista =[]
    for i in range (5):
        elemento = soporte.ingreso_entero("Ingrese un numero entero")
        lista.append(elemento)
    min = minimo(lista)
    print (f" Minimo: {min}")
    max = maximo(lista)
    print (f" Maximo: {max}")

if __name__ == "__main__":
    prueba()