#Lee un número entero y lo convierte en su equivalente binario

def convertir_binario(numero):
    resultados = []

    while numero >=1:
        residuo = numero %2
        resultados.append(residuo)
        numero = numero // 2

    invertido = []
    j = len(resultados)
    for i in range(len(resultados)):
        j -=1
        invertido.append(resultados[j])
    #resultados.reverse()
    #inver = resultados
    return invertido

def imprimir_elementos(mensaje,numeros):
    print(f'\n{mensaje}')
    for i in range(len(numeros)):
        print(numeros[i], end = " ")

def leer_int(mensaje,minimo,maximo):
    siga = True
    while siga:
        numero = int(input(mensaje))
        if numero >= minimo and numero <= maximo:
            siga=False
        else:
            print(f'¡Error! El dato debe estar entre {minimo} y {maximo}\n')
    return numero

numero = leer_int('\nDigite el número a convertir: ',1,10000)
num_binario= convertir_binario(numero)
imprimir_elementos('El número binario es: ',num_binario)




