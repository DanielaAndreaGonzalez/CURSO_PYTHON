'''Calcule la media armónica de un conjunto de números. La media armónica H de 
una serie de números es el recíproco de la media aritmética de los recíprocos de
os números de la serie. Sean los números X1, X2, …, XN. La media armónica H se 
obtiene de la relación:
'''
def leer_numeros(mensaje,minimo):
    siga = True
    while siga:
        numero = int(input(mensaje))
        if numero > minimo:
            siga = False
        else:
            print('\n¡Error! Debe ser un número mayor a 0 ')
    return numero

def imprimir_items(numero):
    print(f'Números')
    for i in range(len(numero)):
        print(numero[i])

def calcular_media_armonica():
    numeros = []

    cantidad = leer_numeros('Ingrese número: ',0)
    cont=0
    H=0
    acu=0
    for i in range(cantidad):
        numero = int(input(f'Elementos [{i}]: '))
        numeros.append(numero)
        cont+=1
           
        acu =( acu+ (1/numeros[i]))
        H = round((cont/acu),3)

    print(f'La media armónica H = {H}')

    imprimir_items(numeros)

calcular_media_armonica()