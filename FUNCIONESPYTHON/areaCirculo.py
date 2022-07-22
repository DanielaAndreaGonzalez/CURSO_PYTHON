#Programa que calcular el área de un circulo importando
#un módulo y alguna de sus funciones

from math import pi

def leerFloat(mensaje):
    cantidad = float(input(mensaje))
    return cantidad

def calcularArea(radio):
    area = pi * (radio **2)
    mensaje =f'El área del circulo es de {area}'
    return mensaje

def main():
    r = leerFloat('Ingrese el radio: ')
    calcular = calcularArea(r)
    print(calcular,'m2')

main()