#Calcula el valor devengado por un conductor
#Trabaja con validaciones


def calcular_devengado(pasajeros,valor_turno):
    BONO = 200
    bono_pasajeros = BONO * pasajeros
    devengado = valor_turno * 1.30 + bono_pasajeros
    return devengado


def leerFloat(mensaje,minimo,maximo):
    siga=True
    while siga:
        numero = float(input(mensaje))
        if numero >= minimo and numero <=maximo:
            siga = False
        else:
            print(f'¡Error! El dato debe estar entre {minimo} y {maximo}')
    return numero

def leerInt(mensaje,minimo,maximo):
    siga=True
    while siga:
        numero = int(input(mensaje))
        if numero >= minimo <= maximo:
            siga = False
        else:
            print(f'¡Error! El dato debe estar entre {minimo} y {maximo}')
    return numero

def leerCadena(mensaje,minimo):
    siga=True
    while siga:
        cadena = input(mensaje)
        if len(cadena) >= minimo:
            siga = False
        else:
            print(f'¡Error! Debe digitar mínimo {minimo} caracteres')
    return cadena


print('Digite los siguientes datos:\n')
nombre=leerCadena('Nombre del conductor', 3)
valor_turno = leerFloat('Valor turno normal:', 25000, 150000)
pasajeros = leerInt('Cantidad de pasajeros: ', 0, 5000)

devenga = calcular_devengado(pasajeros, valor_turno)

print(f'\n{nombre}, usted devengará ${devenga}')
