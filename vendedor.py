#Un vendedor de oro requiere calcular y conocer el total de ventas en un día. Para 
#ello, él posee la cantidad de gramos vendidos y el precio por gramo.


def leerFloat(mensaje):
    cantidad = float(input(mensaje))
    return cantidad

def calcularVentasTotal(cantidadGramos,precioGramo):
    total = cantidadGramos * precioGramo
    return total

def main():
    cantidad = leerFloat('Ingrese la cantidad de gramos vendidos: ')
    precio = leerFloat('Ingrese el precio: ')
    total = calcularVentasTotal(cantidad, precio)
    print(f'El total de ventas en el día es de {total}')

main()