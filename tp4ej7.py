################
# Vanesa Díaz - @diazvaned
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as soporte

def division_lenta(dividendo, divisor):
    #quita signos y los guarda
    signodivisor = 1
    signodividendo = 1
    cociente = 0
    if ((dividendo > 0 and divisor > 0) or (dividendo < 0 and divisor < 0)):
        signodivisor = 1
        signodividendo = 1
    elif (dividendo < 0 or divisor < 0):
        if dividendo <0:
            dividendo = dividendo * -1
            signodividendo = -1
        if divisor < 0:
            print ("divisor")
            divisor = divisor * -1
            signodivisor = -1
    #restas sucesivas
    while ((dividendo >= divisor) and (divisor != 0)):
        dividendo = dividendo -divisor
        cociente = cociente + 1
    #asigna nuevamente los signo    
    resto = dividendo * signodividendo
    cociente = cociente * signodivisor
    return (resto ,cociente)

def prueba():
    dividendo = soporte.ingreso_entero("Ingrese un numero: ")
    divisor = soporte.ingreso_entero("Ingrese otro numero: ")
    resultado = division_lenta(dividendo,divisor)
    print("Resto y cociente: " ,resultado)  

if __name__ == "__main__":
    prueba()