#Lee los elementos de dos listas y los multiplica elemento a elemento

def leer_elementos(mensaje,cantidad):
    numeros = []

    for i in range(cantidad):
        numero = leer_int(f'{mensaje} [{i}]: ',1,100)
        numeros.append(numero)
    
    return numeros

def multiplicar(numeros1,numeros2):
    producto = []

    for i in range(len(numeros1)):
        producto.append(numeros1[i] * numeros2[i])
    return producto

    
def imprimir_elementos(mensaje,numeros):
    print(f'\n{mensaje}')
    for i in range(len(numeros)):
        print(numeros[i],end = " ")

def leer_int(mensaje,minimo,maximo):
    siga = True
    while siga:
        numero = int(input(mensaje))
        if numero >= minimo and numero <= maximo:
            siga = False
        else:
            print(f'\n¡Error! El dato debe estar entre {minimo} y {maximo}')
    return numero

cantidad = leer_int('\nDigite la cantidad de elementos de las listas: ',1,50)
print('\nElementos de la primera lista\n')
numeros1 = leer_elementos('Lista 1: ',cantidad)

print('\nElementos de la segunda lista\n')
numeros2 = leer_elementos('Lista 2',cantidad)

imprimir_elementos('Elementos lista 1: ',numeros1)
imprimir_elementos('Elementos lista 2: ',numeros2)

producto = multiplicar(numeros1,numeros2)
imprimir_elementos('La lista resultado es: ',producto)






