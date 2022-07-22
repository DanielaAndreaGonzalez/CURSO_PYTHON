#Calcula la sumatoria de los elementos de una lista

cantidad = int(input('Digite la cantidad de elementos: '))

numeros = [0] * cantidad

for i in range(cantidad):
    numeros[i] = int(input(f'Elementos: [{i}]: '))
    print(numeros)
