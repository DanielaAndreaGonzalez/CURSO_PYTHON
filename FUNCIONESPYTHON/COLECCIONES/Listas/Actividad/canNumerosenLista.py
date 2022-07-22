'''. Lea una cantidad de números no mayor a 100, con valores entre -1500 y 1500, 
determine cuántas veces se encuentra cada número dentro de la lista. '''

def leer_numeros(mensaje,minimo,maximo):
    siga = True
    while siga:
        numero = int(input(mensaje))
        if numero >= minimo and numero <=maximo:
            siga = False
        else:
            print(f'\n¡Error! Debe estar entre {minimo} y {maximo}')
    return numero

def imprimir_numeros(mensaje,numeros):
    print(f'\n{mensaje}')
    for i in range(len(numeros)):
        print(numeros[i], end= " ")


def valores(mensaje,minimo,maximo):
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

    for i in range(cantidad):
    
        valor = valores(f'Elementos [{i}]: ',-1500,1500)
        numeros.append(valor)
        for i,valor in enumerate(numeros):
            veces = numeros.count(valor)
            print(f'El valor {numeros[i]} se encuentra: ',veces)
        

    imprimir_numeros('Números: ',numeros)


main()






