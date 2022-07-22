#Lea un número de dos cifras y halle la suma entre los dos dígitos que lo 
#conforman. Por ejemplo, si el número leído es 59 el resultado será 14 (5 + 9).
#Nota: se supone que el número leído está en el rango 10 a 99.


def leerInt(mensaje):
    cantidad = int(input(mensaje))
    return cantidad

def calcularSuma(cantidad):
    if cantidad >=10 and cantidad <=99:
        x = cantidad%10
        y= (cantidad%100)//10    
        suma = x+y
        mensaje = f'{cantidad} = {y} + {x} la suma interna es {suma}'
    else:
        mensaje = 'No cumple condición'
    return mensaje

def main():
    numero = leerInt('Ingrese número de dos cifras: ')
    calcular = calcularSuma(numero)
    print(calcular)

main()