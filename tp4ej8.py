################
# Vanesa Díaz - @diazvaned
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as soporte

def ordenar_menor_a_mayor(uno, dos, tres):
    n = 0
    aux = 0
    lista =[uno,dos,tres]
    for i in range (len(lista)):
        for n in range (len(lista)):
            if (lista[i] < lista[n]):
                aux = lista[i]
                lista[i] = lista[n]
                lista[n] = aux
        n = n+1
    tupla =lista[0], lista[1], lista[2]
    return tupla
    
def ordenar_mayor_a_menor(uno, dos, tres):
    n = 0
    aux = 0
    lista =[uno,dos,tres]
    for i in range (len(lista)):
        for n in range (len(lista)):
            if (lista[i] > lista[n]):
                aux = lista[n]
                lista[n] = lista[i]
                lista[i] = aux
        n = n+1
    tupla =lista[0], lista[1], lista[2]
    return tupla

def prueba ():
    uno = soporte.ingreso_entero("Ingrese un numero entero: ")
    dos = soporte.ingreso_entero("Ingrese un numero entero: ")
    tres = soporte.ingreso_entero("Ingrese un numero entero: ")
    
    min = ordenar_menor_a_mayor(uno, dos, tres)
    print (f"Menor a mayor: {min}")
    max = ordenar_mayor_a_menor(uno, dos, tres)
    print (f"Mayor a menor: {max}")

if __name__ == "__main__":
    prueba()