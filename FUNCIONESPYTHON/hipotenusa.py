#Calcular el valor de la hipotenusa de un triángulo rectángulo

from math import sqrt
from math import hypot

def leerFloat(mensaje):
    cantidad = float(input(mensaje))
    return cantidad

def calcularHipotenusa(a,b):
    #h = sqrt(a **2 + b **2)
    h = hypot(a,b)
    return h

def main():
    a = leerFloat('Ingrese el valor del primer cateto: ')
    b = leerFloat('Ingrese el valor del segundo cateto: ')
    calcular = calcularHipotenusa(a, b)
    print(f'\nEn valor de la hipotenusa es: {calcular}')

main()
