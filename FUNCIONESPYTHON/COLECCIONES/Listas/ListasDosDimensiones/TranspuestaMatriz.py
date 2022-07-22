#Calcula la transpuesta d euna matriz

def leer_elementos(mensaje,filas,columnas):
    dimensional = []
    for i in range(filas):
        dimensional.append([])
        for j in range(columnas):
            numero = leer_int(f'{mensaje}[{i}][{j}]: ',-1000,1000)
            dimensional[i].append(numero)
    return dimensional


def calcular_transpuesta(dimensional):
    transpuesta = []
    for i in range(len(dimensional[0])):
        transpuesta.append([])
        for j in range(len(dimensional)):
            transpuesta[i].append(dimensional[j][i])
    return transpuesta

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
            siga=False
        else:
            print(f'\n¡Error!El dato debe estar entre {minimo} y {maximo} \n')
    return numero

def main():
    filas=leer_int('Cantidad de filas: ',1,5)
    columnas = leer_int('Cantidad de columnas: ',1,5)
    
    print('\nElementos de la matriz\n')
    dimensional = leer_elementos('Elementos: ',filas,columnas)

    transpuesta = calcular_transpuesta(dimensional)

    imprimir_elementos('Matriz original:\n',dimensional)
    imprimir_elementos('Matriz transpuesta:\n',transpuesta)


main()