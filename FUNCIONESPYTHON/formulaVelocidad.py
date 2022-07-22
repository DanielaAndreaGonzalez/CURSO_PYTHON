#Calcular la fórmula de la velocidad


def leerFloat(mensaje):
    cantidad = float(input(mensaje))
    return cantidad

def calcularVelocidad(distancia,tiempo):
    v = distancia/tiempo
    return v

def main():
    x = leerFloat('Ingrese la distancia: ')
    t = leerFloat('Ingrese el tiempo: ')
    calcular=calcularVelocidad(x, t)
    print(calcular)

main()