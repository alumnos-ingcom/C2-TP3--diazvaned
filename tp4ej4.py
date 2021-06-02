################
# Vanesa Díaz - @diazvaned
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as soporte



def compara(numero, otro_numero):
    resultado = 0
    if (numero > otro_numero):
        resultado = 1
    if (numero < otro_numero):
        resultado = -1
    if (numero == otro_numero):
        resultado = 0
    return resultado


if __name__ == "__main__":
    numero = soporte.ingreso_entero("Ingrese un numero")
    otro_numero = soporte.ingreso_entero("Ingrese otro numero")
    print (compara(numero, otro_numero))