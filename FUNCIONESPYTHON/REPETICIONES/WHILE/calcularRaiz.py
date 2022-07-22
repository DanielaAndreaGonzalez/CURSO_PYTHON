#Raíz cuadrada con validación

from math import sqrt


def leerPositivo(mensaje):
    siga = True
    while siga:
        numero = float(input(mensaje))
        if numero >= 0:
            siga = False
        else:
            print(f'\n¡Error! El dato debe ser positivo\n')
    return numero

numero = leerPositivo('\nNúmero a calcular raíz: ')
raiz = sqrt(numero)
print(f'\nLa raíz de {numero} es: {raiz}')
