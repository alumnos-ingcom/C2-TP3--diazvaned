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
    elif (numero < otro_numero):
        resultado = -1
    else:
        resultado = 0
    return resultado

def prueba():
    numero = soporte.ingreso_entero("Ingrese un numero")
    otro_numero = soporte.ingreso_entero("Ingrese otro numero")
    comparacion = compara(numero, otro_numero)
    print (comparacion)
    
if __name__ == "__main__":
    prueba()