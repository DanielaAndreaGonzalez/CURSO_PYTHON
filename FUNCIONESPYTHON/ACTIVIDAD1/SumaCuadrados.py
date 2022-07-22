#La siguiente fórmula permite hallar y conocer la suma de los cuadrados de los 
#números desde 1 hasta un valor n:


def leerInt(mensaje):
    cantidad = int(input(mensaje))
    return cantidad

def calcular_suma_cuadrados(n):
    suma =( n * (n+1) *(2*n+1))/6
    return suma

def main():
    n = leerInt('Ingrese número: ')
    calcular = calcular_suma_cuadrados(n)
    print(calcular)

main()