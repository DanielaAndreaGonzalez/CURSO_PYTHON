#Programa que a partir del simbolo quíico o número atómico da el nombre del elemento


def leerFloat(mensaje):
    cantidad = float(input(mensaje))
    return cantidad

def leerString(mensaje):
    cadena = input(mensaje)
    return cadena

def leerInt(mensaje):
    cantidad = int(input(mensaje))
    return cantidad

def determinar_elemento(opcion,simbolo,num_atomico):
    if opcion == 0:
         if simbolo == 'FI':
            mensaje = 'Flerovio'
         elif simbolo == 'Mc':
            mensaje = 'Moscovio'
         elif simbolo == 'Lv' :
            mensaje = 'Livermorio'
         elif simbolo == 'Ts' :
            mensaje = 'Teneso'
         elif simbolo == 'Og' :
            mensaje = 'Oganesón'
         else:
            mensaje = ' No se encuentra'
    elif opcion == 1:
        if num_atomico == 114:
            mensaje = 'Flerovio'
        elif num_atomico == 115:
            mensaje = 'Moscovio'
        elif  num_atomico == 116:
            mensaje = 'Livermorio'
        elif num_atomico == 117:
            mensaje = 'Teneso'
        elif num_atomico == 118:
            mensaje = 'Oganesón'
        else:
            mensaje = ' No se encuentra'
    else:
        mensaje = 'No se ecncuentra'
    return mensaje

def main():
    print('Digite los siguientes datos: ')
    opcion = leerInt('\n Símbolo Químico[0] \n Número atómico[1]\n>>>')
    if opcion == 0:
       num_atomico = 2000
       simbolo = leerString('Ingrese el símbolo químico: ').capitalize()
       nombre = determinar_elemento(opcion,simbolo, num_atomico)
       print('\n',nombre)
    else:
        simbolo = 'NN'
        num_atomico = leerInt('Ingrese el número atómico: ')
        nombre = determinar_elemento(opcion,simbolo, num_atomico)
        print('\n',nombre)
main()