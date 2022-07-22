dimensional =[]
filas = int(input('Ingrese núm '))
columnas=int(input('Ingrese núm '))

for i in range(filas):
    dimensional.append([])
    for j in range(columnas):
        numero = int(input(f'Elemento [{i}][{j}]: '))
        dimensional[i].append(numero)
   
print('\nLos datos de la matriz son:\n')
for i in range(filas):
    for j in range(columnas):
        print(f'{dimensional[i][j]:7d}', end =" ")
    print()



