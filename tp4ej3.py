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
def prueba():
    centigrados = soporte.ingreso_entero("Ingrese la temperatura en grados centigrados: ")
    centigrados = convertir_a_fahrenheit(centigrados)
    print (f"Conversión a fahrenheit: {centigrados}")
    fahrenheit = soporte.ingreso_entero("Ingrese la temperatura en grados fahrenheit: ")
    fahrenheit = convertir_a_centigrados(fahrenheit)
    print (f"Conversión a centigrados: {fahrenheit}")
    
if __name__ == "__main__":
    prueba()