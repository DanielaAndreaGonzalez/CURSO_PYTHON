#Calcula la multiplicación entre dos matrices

def leer_elementos(mensaje,filas,columnas):
    dimensional = []
    for i in range(filas):
        dimensional.append([])
        for j in range(columnas):
            numero = leer_int(f'{mensaje} [{i}][{j}]: ',-1000,1000)
            dimensional[i].append(numero)
    return dimensional

def calcular_multiplicacion(dimensional_a,dimensional_b):
    multiplicacion = []
    for i in range(len(dimensional_a)):
        multiplicacion.append([])
        for j in range(len(dimensional_b[0])):
            sumatoria =0
            for k in range(len(dimensional_b)):
                sumatoria = sumatoria + dimensional_a[i][k] * dimensional_b[k][j]
            multiplicacion[i].append(sumatoria)
    return multiplicacion

def imprimir_elementos(mensaje,dimensional):
    print(f'\n{mensaje}')
    for i in range(len(dimensional)):
        for j in range(len(dimensional[0])):
            print(f'{dimensional[i][j]:7d}', end = " ")
        print()

def leer_int(mensaje,minimo,maximo):
    siga=True
    while siga:
        numero = int(input(mensaje))
        if numero >= minimo and numero <= maximo:
            siga = False
        else:
            print(f'\n¡Error!El dato debe estar entre {minimo} y {maximo}\n')
    return numero
def main():
    filas_a = leer_int('\nFilas matriz A: ',1,5)
    columnas_a = leer_int('\nColumnas matriz A: ',1,5)

    filas_b = leer_int('\nFilas matriz B: ',1,5)
    columnas_b = leer_int('\nColumnas matriz B: ',1,5)
    
    if columnas_a == filas_b:
        print(f'\nElementos matriz A\n')
        lista_a=leer_elementos('Matriz A',filas_a,columnas_a)

        print('\nElementos matriz B\n')
        lista_b=leer_elementos('Matriz B',filas_b,columnas_b)

        lista_c=calcular_multiplicacion(lista_a,lista_b)

        imprimir_elementos('Matriz A:\n',lista_a)
        imprimir_elementos('Matriz B:\n',lista_b)

        imprimir_elementos(f'Martiz resultante producto:\n',lista_c)
    else:
        print('\nNo se puede realizar la multiplicación')


main()