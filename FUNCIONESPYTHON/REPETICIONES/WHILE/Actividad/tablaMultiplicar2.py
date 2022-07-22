
def leerInt(mensaje):
    cantidad = int(input(mensaje))
    return cantidad


def calcularTabla(numero,tope):
    i =0
    while i<tope:
        resultado = i *numero
        print(f'{i} * {numero} = ',resultado)
        i +=1

def main():
    numero = leerInt('Ingrese número: ')
    tope = leerInt('Hasta que número desea ver: ')
    calcular = calcularTabla(numero,tope)
    print(calcular)



main()
