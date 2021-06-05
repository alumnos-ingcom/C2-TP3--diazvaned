################
# Vanesa Díaz - @diazvaned
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import tp4ej1 as soporte

def es_primo(numero):
    divisor = numero
    aux = 0
    contador = 0
    while (divisor >= 1 and contador < 3):
        aux = numero % divisor
        if (aux == 0):
            contador = contador + 1
        divisor = divisor -1 
    if contador > 2:
        return False
    else:
        return True 

def prueba():
    numero = soporte.ingreso_entero("Ingrese un numero entero")
    numero = es_primo(numero)
    print (numero)

if __name__ == "__main__":
    prueba()