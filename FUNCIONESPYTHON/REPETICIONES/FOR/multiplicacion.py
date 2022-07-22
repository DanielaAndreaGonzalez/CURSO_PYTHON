#Solicita un número y le calcula su tabla de multiplicacion


def leerInt(mensaje):
    numero = int(input(mensaje))
    return numero


tabla = leerInt('Ingrese la tabla a calcular: ')

print(f'\nTable del {tabla}\n')

for fila in range(1,10):
    producto = tabla * fila
    print(f'{tabla} * {fila} = {producto}')






