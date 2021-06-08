################
# Vanesa Díaz - @diazvaned
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as soporte


def signo(numero):
    resultado = 0
    if (numero > 0):
        resultado = 1
    elif (numero < 0):
        resultado = -1
    else:
        resultado = 0
    return resultado

def prueba():
    numero = soporte.ingreso_entero("Ingrese un numero")
    resultado = signo(numero)
    print (resultado)

if __name__ == "__main__":
    prueba()