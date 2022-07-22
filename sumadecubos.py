''' Halle e informe la suma de los cubos de los números desde 1 hasta un valor n, 
para ello use la siguiente fórmula:
'''

def leerInt(mensaje):
    cantidad = int(input(mensaje))
    return cantidad

def calcularSuma(cantidad):
    suma = ((cantidad * (cantidad + 1)) /2) **2
    return suma

def main():
    cantidad = leerInt('Ingrese cantidad: ')
    suma = calcularSuma(cantidad)
    print(suma)

main()


