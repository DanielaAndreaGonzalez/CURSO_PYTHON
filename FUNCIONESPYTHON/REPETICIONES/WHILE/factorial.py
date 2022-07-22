#Calcula el factorial de un número

def leerInt(mensaje):
    cantidad = int(input(mensaje))
    return cantidad


def calcular_factorial(tope):
    if tope >= 0:
        factorial = 1
        numeros = 1
        while numeros <= tope:
            factorial = factorial * numeros
            numeros = numeros + 1
    else:
        factorial = '¡Error!,la entrada es un número negativo'

    return factorial

def main():
    numero = leerInt('Número a calcular el factorial: ')
    factorial = calcular_factorial(numero)
    print(f'Factorial = {factorial}')

main()