################
# Vanesa Díaz - @diazvaned
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


import tp4ej1 as soporte



def suma_lenta(numero, otro_numero):
    while (otro_numero != 0):      
        if otro_numero < 0:
            otro_numero = otro_numero + 1
            numero = numero - 1
        if otro_numero > 0:
            otro_numero = otro_numero -1
            numero = numero + 1        
    return numero

def prueba():
    numero = soporte.ingreso_entero("Ingrese un numero: ")
    otro_numero = soporte.ingreso_entero("Ingrese otro numero: ")
    resultado = suma_lenta(numero,otro_numero)
    print(resultado)    

if __name__ == "__main__":
    prueba()