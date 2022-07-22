''' Lea dos números y halle la división del primero entre el segundo. En caso de 
que el segundo sea un 0, imprima un mensaje que diga que la división entre 
0 es indeterminada.'''



def leerInt(mensaje):
    cantidad = int(input(mensaje))
    return cantidad

def calcularDivision(cantidad):
    x = cantidad%10
    y= (cantidad%100)//10 
    if cantidad >10 and cantidad <=99:
        if x ==0:
           mensaje = f'División entre 0: División indeterminada'
        else:
            division = y/x 
            mensaje = f'{cantidad} = {y} / {x} la división interna es {division}'
    else:
        mensaje = 'Ingrese número de dos cifras'
    return mensaje

def main():
    numero = leerInt('Ingrese número de dos cifras: ')
    calcular = calcularDivision(numero)
    print(calcular)

main()