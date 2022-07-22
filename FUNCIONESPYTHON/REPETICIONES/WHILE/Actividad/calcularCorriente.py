#Programa que calcula la corriente con la fórmula
#general v =i*r
#V:voltaje
#i:corriente
#r:resistencia

def leerInt(mensaje):
    cantidad = int(input(mensaje))
    return cantidad

def leerString(mensaje):
    cadena = input(mensaje)
    return cadena


def leerBooleano(mensaje):
    respuesta = input(mensaje).upper()

    if respuesta == 'S':
        respuesta = True
    else:
        respuesta = False
    return respuesta



def calcular(mensaje):
    if mensaje == 'V':
       i = leerInt('Ingrese el valor de la corriente: ')
       r = leerInt('Ingrese el valor de la resistencia: ')
       voltaje =i * r
       mensaje = f'{i} * {r} = {voltaje}' 
    elif mensaje == 'I':
        v = leerInt('Ingrese el valor del voltaje: ')
        r = leerInt('Ingrese el valor de la resistencia: ')
        corriente = v/r
        mensaje = f'{v} / {r} = {corriente}'
    elif mensaje == 'R':
        v = leerInt('Ingrese el valor del voltaje: ')
        i = leerInt('Ingrese el valor de la corriente: ')
        resistencia = v/i
        mensaje = f'{v} / {i} = {resistencia}'
    else:
        mensaje = 'Datos incorrectos'
    return mensaje




def main():
    
    respuesta = True

    while (respuesta):
        cadena = leerString('¿Qué desa calcular? [V]oltaje,[I]corriente,[R]esistencia ').upper()
        calculo = calcular(cadena)
        print(calculo)
        
        respuesta = leerBooleano('¿Desea seguir calculando [S][N] ')
    
    print('Gracias !!!')

    
    

main()
