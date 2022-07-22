''' Basándose en la solución del ejercicio anterior, debe convertir los elementos 
positivos en negativos y los positivos en negativos, el cero queda igual.'''



def leer_elementos(mensaje,filas,columnas):
    dimensional = []
    for i in range(filas):
        dimensional.append([])
        for j in range(columnas):
            numero = leer_int(f'{mensaje} [{i}][{j}]: ',-1000,1000)
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

def listas(dimensional):
    positivos = []
    negativo = []
    
    for i in range(len(dimensional)):
        for j in range(len(dimensional[0])):
            if dimensional[i][j]>=0:
               positivos.append(dimensional[i][j] *-1)
             
            else:
                negativo.append(dimensional[i][j] * -1)
    print(f'\nPositivos en negativos: {positivos} \nNegativos en positivos: {negativo}')        


def main():
    filas=leer_int('Ingrese filas: ',1,5)
    columnas= leer_int('Ingrese columnas: ',1,5)
    dimensional=leer_elementos('Elementos: ',filas,columnas)
    imprimir('Matriz: ',dimensional)
    listas(dimensional)


main()