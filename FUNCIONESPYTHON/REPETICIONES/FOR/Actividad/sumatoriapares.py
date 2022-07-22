#Sumatoria de números pares desde 1 hasta n


def leerInt(mensaje):
    cantidad = int(input(mensaje))
    return cantidad


n = leerInt('Ingrese número: ')
acu = 0
for i in range(1,n):
    if i%2==0:
        acu = acu + i
        
print(f'Suma números pares: {acu}')
    

