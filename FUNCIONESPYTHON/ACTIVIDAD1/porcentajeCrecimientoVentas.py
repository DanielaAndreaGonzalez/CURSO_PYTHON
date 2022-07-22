#Para calcular el porcentaje de crecimiento de ventas en un negocio de un 
#periodo dado a otro, se aplica la siguiente fórmula:
#DATOS:
#pc=porcentaje de crecimiento
#vf = ventjas finales
#vi=ventas iniciales

def leerFloat(mensaje):
    cantidad = float(input(mensaje))
    return cantidad


def calcular_ventas(vf,vi):
    pc = ((vf/vi) * 100) -100
    return pc

def main():
    vf= leerFloat('Ingrese ventas finales: ')
    vi = leerFloat('Ingrese ventas iniciales: ')
    calcular = calcular_ventas(vf, vi) 
    print(calcular,'%')

main()