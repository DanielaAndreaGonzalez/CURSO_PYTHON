#Calcula la sumatoria de los elementos de una lista

cantidad = int(input('Digite la cantidad de elementos: '))

numeros = []

for i in range(cantidad):
    numero = int(input(f'Elementos [{i}]: '))
    numeros.append(numero)

sumatoria = 0
for i in range(cantidad):
    sumatoria = sumatoria + numeros[i]

print('\nLos datos de la lista son: \n')
for i in range(cantidad):
    print(numeros[i],end=" ")

print(f'\n\nLa sumatoria de los elementos es: {sumatoria}')