################
# Vanesa Díaz - @diazvaned
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


import tp4ej1 as soporte



def suma_lenta(numero, otro_numero):
    resultado = (f"{numero}")
    while (otro_numero != 0):      
        if otro_numero < 0:
            otro_numero = otro_numero + 1
            numero = numero - 1
            resultado = resultado + " + (- 1)"
        if otro_numero > 0:
            otro_numero = otro_numero -1
            numero = numero + 1
            resultado = resultado + " + 1"
        
    return resultado + (f" = {numero}")


if __name__ == "__main__":
    numero = soporte.ingreso_entero("Ingrese un numero: ")
    otro_numero = soporte.ingreso_entero("Ingrese otro numero: ")
    print(suma_lenta(numero,otro_numero))