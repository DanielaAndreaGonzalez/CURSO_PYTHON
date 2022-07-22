#Determina cuál vehículo obtienen mejores ganancias

def leer_elementos(mensaje,vehiculos,filas,columnas):
    dimensional = []
    for i in range(filas):
        print(f'\n{mensaje[i]}\n')
        dimensional.append([])
        for j in range(columnas):
            numero = leer_float(f'{vehiculos[j]:7s}: ',0,999999)
            dimensional[i].append(numero)
    return dimensional

def calcular_producido(dimensional):
    producido = [0] * len(dimensional[0])
    for i in range(len(dimensional)):
        for j in range(len(dimensional[0])):
            producido[j] += dimensional[i][j]
    return producido

def imprimir_elementos(mensaje,dimensional):
    for i in range(len(dimensional)):
        print(f'{mensaje[i]:10s}',end =" ")
        for j in range(len(dimensional[0])):
            print(f'{dimensional[i][j]:11.1f}',end = " ")
        print()

def imprimir_totales(dimensional):
    totales = calcular_producido(dimensional)
    print(f'\nTotales $: ',end = " ")

    for i in range(0,len(dimensional[0])):
        print(f'{totales [i]:11.1f}',end = " ")
    return totales

def encontrar_mayor(totales):
    mayor = max(totales)
    indice = totales.index(mayor)
    return indice

def leer_float(mensaje,minimo,maximo):
    siga=True
    while siga:
        numero = float(input(mensaje))
        if numero >= minimo and numero <= maximo:
            siga = False
        else:
            print(f'¡Error!El dato debe estar entre {minimo} y {maximo}\n')
    return numero

def main():
    vehiculos = ('Taxi', 'Bus', 'Uber')
    dias = ('Lunes', 'Martes' ,'Miércoles','Jueves','Viernes')
    

    columnas = len(vehiculos)
    filas = len(dias)

    print('\nDigite el producido diario por cada vehículo ')
    dimensional = leer_elementos(dias,vehiculos,filas,columnas)

    print(f'\nVehículo--> Taxi         Bus        Uber\n')
    imprimir_elementos(dias,dimensional)
    
    total = imprimir_totales(dimensional)

    indice = encontrar_mayor(total)

    print(F'\n\nEl{vehiculos[indice]}es el de mayor producido')

    
    

main()