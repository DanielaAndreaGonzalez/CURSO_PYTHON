#Lectura, proceso y salida de una lista


def leer_elementos(mensaje,cantidad):
    numeros = []
    for i in range(cantidad):
        numero = leer_int(f'{mensaje}[{i}]:',1,100)
        numeros.append(numero)
    return numeros

def sumar(numeros):
    sumatoria = 0
    for i in range(len(numeros)):
        sumatoria = sumatoria + numeros[i]
    return sumatoria

def imprimir_elementos(mensaje,numeros):
    print(f'\n{mensaje}')
    for i in range(len(numeros)):
        print(numeros[i],end =" ")

def leer_int(mensaje,minimo,maximo):
    siga = True
    while siga:
        numero = int(input(mensaje))
        if numero >= minimo and numero <= maximo:
            siga=False
        else:
            print(f'\n¡Error! El dato debe estar entre {minimo} y {maximo}\n')
    return numero

cantidad = leer_int('\nDigite la cantidad de elementos: ',1,50)
numeros = leer_elementos('Elemento ',cantidad)

sumatoria = sumar(numeros)

print(f'\nLa sumatoria de los elementos es: {sumatoria}')
imprimir_elementos('Los datos de la lista son: ',numeros)
