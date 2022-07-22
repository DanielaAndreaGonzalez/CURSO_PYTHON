'''Lea una cantidad de números no mayor a 100, con valores positivos no mayores 
a 2000 y determine cuántos de ellos son pares y cuántos impares'''


def leer_numeros(mensaje,minimo,maximo):
    siga=True
    while siga:
        numero = int(input(mensaje))
        if numero >= minimo and numero <= maximo:
            siga = False
        else:
            print(f'\n¡Error! Debe estar entre {minimo} y {maximo}')
    return numero


def imprimir_items(mensaje,numeros):
    print(mensaje)
    for i in range(len(numeros)):
        print(numeros[i],end = " ")


def par_impar(mensaje,minimo,maximo):
    siga = True
    while siga:
        numero = int(input(mensaje))
        if numero >= minimo and numero <=maximo:
            siga = False
        else:
            print(f'\n¡Error! Debe estar entre {minimo} y {maximo}')
    return numero


def main():

    numeros = []    
    cantidad = leer_numeros('Ingrese el número: ',1,100)

    cont=0
    contImpar=0
    for i in range(cantidad):
    
        valor = par_impar(f'Elementos [{i}]: ',1,2000)
        numeros.append(valor)
        if numeros[i] %2==0:
             cont+=1
        else:
            contImpar+=1
    
    print('Pares',cont,'Impares: ',contImpar)
    imprimir_items('Números: ',numeros)

main()