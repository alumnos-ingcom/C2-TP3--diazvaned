################
# Vanesa Díaz - @diazvaned
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    intentos = cantidad_reintentos
    while cantidad_reintentos > 0:
        try:
            return ingreso_entero(mensaje)
        except IngresoIncorrecto as err:
            print (f"No era un numero quedan {cantidad_reintentos}")
            cantidad_reintentos = cantidad_reintentos - 1
    raise IngresoIncorrecto (f"Luego de {intentos}") 
    
def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=10):
    while True:
        numero = ingreso_entero(mensaje + str(valor_minimo) +" y "+ str(valor_maximo))
        if (numero >= valor_minimo and numero <= valor_maximo):
            break
        

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass 


def ingreso_entero(mensaje):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número entero.
    """
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
    return entero



if __name__ == "__main__":
    ingreso_entero_restringido("Ingrese un numero")
    