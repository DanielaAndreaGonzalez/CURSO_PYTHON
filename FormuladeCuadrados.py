'''Escriba un programa en Python que, permita hallar y conocer la suma de 
los cuadrados de los números desde 1 hasta un valor n, utilizando la siguiente 
fórmula:
'''


def leerInt(mensaje):
    numero = int(input(mensaje))
    return numero

def calcularSuma(numero):
    suma = numero * (numero + 1)*(2*numero+1)//6
    return suma


def main():
    numero = leerInt('Ingrese número ')
    sumar= calcularSuma(numero)
    print(sumar)

main()
