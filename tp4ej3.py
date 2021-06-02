################
# Vanesa Díaz - @diazvaned
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


import tp4ej1 as soporte


def convertir_a_fahrenheit(centigrados):
    fahrenheit = (centigrados *1.8) + 32
    return fahrenheit
def convertir_a_centigrados(fahrenheit):
    centigrados = (fahrenheit-32)/1.8
    return centigrados

if __name__ == "__main__":
    centigrados = soporte.ingreso_entero("Ingrese la temperatura en grados centigrados: ")
    print (f"Conversión a fahrenheit: {convertir_a_fahrenheit(centigrados)}")
    fahrenheit = soporte.ingreso_entero("Ingrese la temperatura en fahrenheit: ")
    print( f"Conversión a centigrados: {convertir_a_centigrados(fahrenheit)}")