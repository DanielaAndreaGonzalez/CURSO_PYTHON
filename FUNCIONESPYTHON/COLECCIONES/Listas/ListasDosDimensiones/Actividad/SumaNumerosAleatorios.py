''' Usando la función para generar números aleatorios, vista en un capítulo anterior, 
genere una lista de dos dimensiones de tamaño m x n (máximo de 5 x 5) y llénela 
con valores entre 1 y 99, encuentre la suma de los elementos en cada fila'''


from random import randint

def leer_elementos(filas,columnas):
    dimensional = []
    for i in range(filas):
        dimensional.append([])
        for j in range(columnas):
            numero = randint(1,99)
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

def sumar_filas(dimensional):
    for i in range(len(dimensional)):
        print(f'Fila: {i}',dimensional[i])
        filas=0
        for j in range(len(dimensional[i])):
            #print(f'Fila: {j}',dimensional[j])
            filas = filas + dimensional[i][j]
        print(f'Suma: {filas}')
def main():
    filas = leer_int('Ingrese filas: ',1,5)
    columnas = leer_int('Ingrese columnas: ',1,5)

    dimensional = leer_elementos(filas,columnas)
    imprimir('Matriz: ',dimensional)
    sumar_filas(dimensional)
main()

