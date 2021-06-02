################
# Vanesa Díaz - @diazvaned
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as soporte


def signo(numero):
    resultado = ""
    if (numero > 0):
        resultado = "El número es positivo"
    if (numero < 0):
        resultado = "El número es negativo"
    if (numero ==0):
        resultado = "El numero es cero"
    return resultado


if __name__ == "__main__":
    numero = soporte.ingreso_entero("Ingrese un numero")
    print (signo(numero))