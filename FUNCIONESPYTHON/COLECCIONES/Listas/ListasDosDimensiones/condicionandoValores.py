#Determina el elemento de mayor valor de una matriz


def leer_elementos(mensaje,filas,columnas):
    dimensional = []
    for i in range(filas):
        dimensional.append([])
        for j in range(columnas):
            numero = leer_int(f'{mensaje}[{i}][{j}]: ',-1000,1000)
            dimensional[i].append(numero)
    return dimensional


def encontrar_mayor(dimensional):
    mayor = dimensional[0][0]
    for i in range(len(dimensional)):
        for j in range(len(dimensional[0])):
            if mayor < dimensional[i][j]:
                mayor = dimensional[i][j]
    return mayor

def imprimir_elementos(mensaje,dimensional):
    print(f'\n{mensaje}')
    for i in range(len(dimensional)):
        for j in range(len(dimensional[0])):
            print(f'{dimensional[i][j]:4d}',end= " ")
        print()

def leer_int(mensaje,minimo,maximo):
    siga = True
    while siga:
        numero = int(input(mensaje))
        if numero >= minimo and numero <= maximo:
            siga = False
        else:
            print(f'\n¡Error!El dato debe estar entre {minimo} y {maximo}')
    return numero

def main():
    filas = leer_int('Cantidad de filas: ',1,5)
    columnas = leer_int('Cantidad de columnas: ',1,5)

    print('\nElementos de la matriz\n')
    dimensional = leer_elementos('Elementos ',filas,columnas)
    mayor = encontrar_mayor(dimensional)
    print(f'\nEl mayor elemento de la matriz es: {mayor}')
    imprimir_elementos('Los datos de la matriz son:\n',dimensional)


main()

