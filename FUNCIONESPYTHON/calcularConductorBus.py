'''Una empresa de buses urbanos, desea un programa que permita 
calcular cuánto devenga en total un conductor en un día domingo. El turno dominical 
se paga con un incremento del 30% sobre el valor de turno normal, además por cada 
pasajero que movilice, al conductor se le otorga un bono de $200'''


def leerFloat(mensaje):
    cantidad = float(input(mensaje))
    return cantidad

def leerString(mensaje):
    cadena = input(mensaje)
    return cadena
    
def leerInt(mensaje):
    cantidad = int(input(mensaje))
    return cantidad

def calcular_devengado(pasajeros,valorTurno):
    BONO = 200
    bono_pasajeros = BONO * pasajeros
    devengado = valorTurno * 1.30 + bono_pasajeros
    return devengado

def main():
    print('Digite los siguientes datos: ')
    nombre = leerString('Nombre del conductor: ')
    valorTurno = leerFloat('Valor turno normal: ')
    pasajeros = leerInt('Cantidad pasajeros: ')
    devenga = calcular_devengado(pasajeros, valorTurno)
    print(f'\n{nombre}, usted devengará ${devenga}')

main()