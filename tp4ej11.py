################
# Vanesa Díaz - @diazvaned
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def es_palindromo(texto):
    inicio = 0
    fin = len(texto) -1
    contador = 0
    control = 0
    while ((texto[inicio] != texto[fin]) and (control != len(texto)-1)):
        if (texto[inicio] == texto[fin]):
            contador = contador +1
        inicio = inicio +1
        fin = fin -1
        control = control +1
    if (contador == control):
        return True
    else:
        return False

def prueba():
    palabra = input ("Ingrese una palabra: ")
    palindromo = es_palindromo(palabra)
    print(palindromo)

if __name__ == "__main__":
    prueba()