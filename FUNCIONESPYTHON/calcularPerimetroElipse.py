#Calcular el perimetro de una elipse

from math import pi
def leerFloat(mensaje):
    cantidad = float(input(mensaje))
    return cantidad

def calcularPerimetro(r,s):
    o = 2 * pi * (((r **2 + (s**2)) / 2)**(1/2)) 
    mensaje = f'Fórmula {o}'
    return mensaje

def main():
    r = leerFloat('Ingrese el valor del semieje mayor: ')
    s = leerFloat('Ingrese el valor del semieje menor: ')
    calcular = calcularPerimetro(r, s)
    print(calcular)

main()