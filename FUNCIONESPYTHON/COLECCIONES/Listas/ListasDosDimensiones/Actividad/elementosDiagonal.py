#Lista dos dimensiones donde almaacene los elementos 



def leer_elementos(mensaje,filas,columnas):
    dimensional = []
    for i in range(filas):
        dimensional.append([])
        for j in range(columnas):
            numero = leer_int(f'{mensaje} [{i}][{j}]: ',1,1000)
            dimensional[i].append(numero)
    return dimensional

def leer_int(mensaje,minimo,maximo):
    siga=True
    while siga:
        numero = int(input(mensaje))
        if numero >=minimo and numero <= maximo:
            siga=False
        else:
            print(f'\n¡Error!El dato debe estar entre {minimo} y {maximo}\n')
    return numero

def imprimir(mensaje,dimensional):
    print(f'\n{mensaje}')
    for i in range(len(dimensional)):
        for j in range(len(dimensional[0])):
            print(f'{dimensional[i][j]:7d}',end = " ")
        print()

def sumar_diagonal(mensaje,dimensional):
    sumar=0
    for i in range(len(dimensional)):
        for j in range(len(dimensional[0])):
            if i ==j:
                sumar=sumar+dimensional[j][i]
                print('Diagonales: ',dimensional[j][i],end =" ")
    
    print(f'\n{mensaje} {sumar}')

def main():
    siga=True
    while siga:
        filas = leer_int('Ingrese filas: ',1,5)
        columnas = leer_int('Ingrese columnas: ',1,5)
        if filas ==columnas:
            dimensional = leer_elementos('Elementos: ',filas,columnas)
            print(dimensional)
            sumar_diagonal('La suma de la diagonal es: ',dimensional)    
            siga=False
        else:
            print('¡Error! Deben ser iguales')

    

main()

