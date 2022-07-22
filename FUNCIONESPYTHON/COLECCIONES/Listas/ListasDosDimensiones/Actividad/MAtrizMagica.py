'''Se tiene una lista de dos dimensiones, donde se almacenan los elementos de una 
matriz. Determine si es una matriz mágica. Una matriz mágica es aquella en que 
la suma de cada una de sus filas, columnas y diagonales tienen el mismo valor. 
Tenga presente que, las matrices mágicas tienen que ser cuadradas.'''



def leer_elementos(mensaje,filas,columnas):
    dimensional = []
    for i in range(filas):
        dimensional.append([])
        for j in range(columnas):
            numero = leer_int(f'{mensaje}[{i}][{j}]: ',-1000,1000)
            dimensional[i].append(numero)
    return dimensional


def leer_int(mensaje,minimo,maximo):
    siga=True
    while siga:
        numero = int(input(mensaje))
        if numero >= minimo and numero <= maximo:
            siga=False
        else:
            print(f'\n¡Error!El dato debe estar entre {minimo} y {maximo} \n')
    return numero

def imprimir(mensaje,dimensional):
    print(f'\n{mensaje}')
    for i in range(len(dimensional)):
        for j in range(len(dimensional[0])):
            print(f'{dimensional[i][j]:7d}',end = " ")
        print()

def matriz_magica(dimensional):
    diagonal=0
    for i in range(len(dimensional)):
        sumarFilas=0
        sumarColumnas=0
       # print(f'Fila: {i}',dimensional[i])
        for j in range(len(dimensional[0])):
            sumarFilas = sumarFilas + dimensional[i][j]
            #print(f'Columna {j}',dimensional[j][i],'\n')
            sumarColumnas = sumarColumnas + dimensional[j][i]
            if i ==j:
                diagonal=diagonal+dimensional[j][i]
        print (f'Suma Fila: {[i]} {sumarFilas} - Suma Columna:{[j]}{sumarColumnas}')
            
    print(f'\nSuma Diagonal: {diagonal}')

   
    if sumarColumnas == sumarFilas and sumarColumnas == diagonal:
        print('Es matriz mágica')
    else:
        print('No es matriz mágica')
            
      


def main():
    siga=True
    while siga:
        filas=leer_int('Ingrese filas: ',1,9)
        columnas=leer_int('Ingrese columnas: ',1,9)
        if filas == columnas:
            dimensional = leer_elementos('Elementos',filas,columnas)
            imprimir(f'\nMatriz de {filas} x {columnas}',dimensional)
            matriz_magica(dimensional)
            siga=False
        else:
            print('¡Error! Deben ser números iguales ')
main()