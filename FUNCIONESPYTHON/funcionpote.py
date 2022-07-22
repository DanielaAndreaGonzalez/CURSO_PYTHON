#Programa que calcula la elevación de un numero
#con la funion pote
from math import pow
def leerInt(mensaje):
    numero = int(input(mensaje))
    return numero


def calcularPotencia(base,potencia):
    resultado = pow(base, potencia)
    mensaje = f'{base} ^ {potencia} ={resultado}'
    return resultado

def main():
    base = leerInt('Ingrese la base: ')
    potencia = leerInt('Ingrese la potencia a elevar: ')
    calcular = calcularPotencia(base,potencia)
    print(calcular)

main()