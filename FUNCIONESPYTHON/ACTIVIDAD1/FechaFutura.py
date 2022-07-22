'''Lea la fecha actual en el formato dd-mm- aaaa, luego lea un número entero 
positivo, el cual representará una cantidad de días futuros. Calcule e informe la 
fecha futura, partiendo de la fecha inicial y teniendo en cuenta la cantidad de 
días leídos. Ejemplo:
Fecha de hoy: día 1, mes 3, año 2019
Días futuros: 45
Fecha futura: 16-04-2019
Nota: se tomarán 360 días por año.'''


def leerInt(mensaje):
    cantidad = int(input(mensaje))
    return cantidad

def calcular_fecha(dias_actual,dias_futuro,mes,año):
    suma = dias_actual + dias_futuro
    if suma >30 and mes <12:
        dia = ( dias_actual+dias_futuro)- 30
        mes = mes + 1
        mensaje = f'{dia}-{mes}-{año}'
    elif mes<12 and suma<30:
        dia =( dias_actual+dias_futuro)
        mensaje = f'{dia}-{mes}-{año}'
    else:
        dia =(dias_actual + diasfuturo) - 30
        mes = 1
        año = año +1
        mensaje = f'{dia}-{mes}-{año}'
    return mensaje


def main():
    print('Ingrese los siguientes datos: \n')
    dia_actual = leerInt('Ingrese el día actual: ')
    mes_actual = leerInt('Ingrese el mes actual: ')
    año_actual = leerInt('Ingrese el año actual: ')
    dia_futuro = leerInt('Ingrese el día a futuro: ')
    
    calcular = calcular_fecha(dia_actual, dia_futuro, mes_actual,año_actual)
    print(calcular)
main()