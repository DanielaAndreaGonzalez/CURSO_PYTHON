'''Dada una cantidad en pesos colombianos, obtenga e informe la equivalencia en 
dólares y en euros, de acuerdo con la cotización del día.'''


def leerFloat(mensaje):
    cantidad = float(input(mensaje))
    return cantidad

def convertirPesosColombianos(cantidadPesos):
    dolares = (cantidadPesos * 1) / 3762
    mensaje = f'USD ${dolares}'
    return mensaje

def convertirAeuros(cantidadPesos):
    euros = cantidadPesos * 0.00022
    mensaje = f'\neuro {euros}'
    return mensaje

def main():
    cantidad = leerFloat('Ingrese la cantidad a convertir: ')
    calcularDolar = convertirPesosColombianos(cantidad)
    calcularEuros = convertirAeuros(cantidad)
    print(calcularDolar,calcularEuros)

main()
