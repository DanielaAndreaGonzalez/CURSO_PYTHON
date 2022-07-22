#Determina el mayor elemento de una metriz

filas = int(input('Cantidad de filas: '))
columnas = int(input('Cantidad de columnas: '))

dimensional = []
for i in range(filas):
    dimensional.append([])
    for j in range(columnas):
        numero = int(input(f'Elemento [{i}][{j}]: '))
        dimensional[i].append(numero)

mayor = dimensional[0][0]

for i in range(filas):
    for j in range(columnas):
        if mayor < dimensional[i][j]:
            mayor = dimensional[i][j]

print(f'\nEl mayor elemento de la matriz es: {mayor}')
  
print('\nLos datos de la matriz son:\n')
for i in range(filas):
    for j in range(columnas):
        print(f'{dimensional[i][j]:7d}', end =" ")
    print()
