################
# Vanesa Díaz - @diazvaned
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import tp4ej1 as numeroentero
import tp4ej9 as numeroprimo


def factores_primos(numero):
    divisor = numero
    resto = 0
    factoresprimos = []
    while (divisor > 1):
        resto = numero % divisor
        esprimo = numeroprimo.es_primo(divisor)
        if (resto == 0 and (esprimo ==True)):
            factoresprimos.append(divisor)
        divisor = divisor -1
    return factoresprimos

def prueba():
    numero = numeroentero.ingreso_entero("Ingrese un numero entero: ")
    factoresprimos = factores_primos(numero)
    print("Lista de factores primos: ",factoresprimos)

if __name__ == "__main__":
    prueba()