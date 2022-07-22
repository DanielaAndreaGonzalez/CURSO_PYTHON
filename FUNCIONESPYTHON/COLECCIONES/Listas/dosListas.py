#Lee los elementos de dos listas y los fusiona en una nueva

def leer_elementos(mensaje,cantidad):
    numeros = []
    for i in range(cantidad):
        numero = leer_int(f'{mensaje}[{i}]: ',1,100)
        numeros.append(numero)
    return numeros

def fusionar(numeros1,numeros2):
    tope = len(numeros1) + len(numeros2)
    unidos = []
    j = 0

    for i in range(tope):
        if i< len(numeros1):
            unidos.append(numeros1[i])
        else:
            unidos.append(numeros2[j])
            j += 1
    return unidos

def imprimir_elementos(mensaje,numeros):
    print(f'\n{mensaje}')
    for i in range(len(numeros)):
        print(numeros[i],end=" ")

def leer_int(mensaje,minimo,maximo):
    siga = True
    while siga:
        numero = int(input(mensaje))
        if numero >= minimo and numero <= maximo:
            siga = False
        else:
            print(f'\n¡Error! El dato debe estar entre {minimo} y {maximo}\n')
        return numero

cantidad = leer_int('\nDigite la cantidad de elementis primera lista: ',1,50)
numeros1 = leer_elementos('Lista 1 ',cantidad)

cantidad = leer_int('\nDigite la cantidad de elementos segunda lista: ',1,50)
numeros2 = leer_elementos('Lista 2 ',cantidad)

unidos = fusionar(numeros1,numeros2)
imprimir_elementos('La lista fusionada es: ',unidos)