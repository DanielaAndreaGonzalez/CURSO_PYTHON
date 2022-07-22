'''Basándose en la solución del ejercicio anterior, encuentre la sumatoria y el 
promedio de los impares, la sumatoria de los pares y determine cuál de las dos 
sumatorias es mayor.
'''

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

def mayor(prom1,prom2):
    if prom1>prom2:
        mensaje = f'\nPromedio pares es mayor: {prom1}'
    else:
        mensaje = f'\nPromedio Impares es mayor {prom2}'
    return mensaje

def imprimir_mensajes(sum_par,sum_impar,promPar,promImpar):
    print('Suma par',sum_par,'\nSuma impar',sum_impar)
    print('Promedio pares',promPar,'\nPromedio Impares',promImpar)
  

def main():

    numeros = []    
    cantidad = leer_numeros('Ingrese el número: ',1,100)

    cont=0
    contImpar=0
    sumPar=0
    sumImpar=0
    promPar=0
    promImpar=0
    for i in range(cantidad):
    
        valor = par_impar(f'Elementos [{i}]: ',1,2000)
        numeros.append(valor)
        if numeros[i] %2==0:
             cont+=1
             sumPar += numeros[i]
        else:
            contImpar+=1
            sumImpar += numeros[i]
    promPar = sumPar / cont
    promImpar = sumImpar /contImpar

    imprimir_mensajes(sumPar,sumImpar,promPar,promImpar)
    print(mayor(promPar,promImpar))
    imprimir_items('Números: ',numeros)

main()

