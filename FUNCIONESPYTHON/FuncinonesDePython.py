#Fuciones para datos de tipo str (cadena)

def leerString(mensaje):
    cadena = input(mensaje)
    return cadena

def utilizarFunciones(cadena):
    print(cadena.lower())
    print(cadena.capitalize())
    print(cadena.swapcase())
    print(cadena.title())
    print(cadena.center(50,'*'))
    print(cadena.upper())
    return cadena

def main():
    nombre= leerString('Digite un nombre: ')
    letra = leerString('Digite la letra a buscar: ')
    mirar = utilizarFunciones(nombre)
    print(f'La letra \"{letra}\" se encuentra {nombre.count(letra)} veces ')

main()