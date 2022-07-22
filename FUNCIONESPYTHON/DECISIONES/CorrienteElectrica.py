#Este programa calcula las variables de la ley de ohm
#Datos:
# V = I * R
#V : voltaje
#I : corriente
#R:resistencia
'''Fórmulas
v = i * r
i = v/r
r=v/i
'''
#Funciones

def leerFloat(mensaje):
    cantidad = float(input(mensaje))
    return cantidad

#Calcula el voltaje
def v(i,r):
    v = i * r
    return v

#Calcula la corriente
def i(v,r):
    i = v/r
    return i

#calcula la resistencia
def r(v,i):
    r = v/i
    return r

def main():
    print('¿Qué valor desea calcular?')
    print('\n[V]oltaje\n[R]esistencia\n[C]orriente\n')
    opcion = input().upper()

    if opcion== 'V':
        corriente = leerFloat('Digite el valor de la corriente: ')
        resistencia = leerFloat('Digite el valor de la resistencia: ')
        print(f'El voltaje es: {v(corriente, resistencia)}')

    elif opcion == 'R':
        resistencia = leerFloat('Digite el valor de la resistencia: ')
        voltaje = leerFloat('Digite el valor del voltaje: ')
        print(f'La corriente es: {i(voltaje, resistencia)}')

    elif opcion == 'C':
        voltaje= leerFloat('Digite el valor del voltaje: ')
        corriente = leerFloat('Digite el valor de la corriente: ')
        print(f'La resistencia es: {r(voltaje, corriente)}')

    else:
        print('\n ¡Error! Opción no disponible')

main()