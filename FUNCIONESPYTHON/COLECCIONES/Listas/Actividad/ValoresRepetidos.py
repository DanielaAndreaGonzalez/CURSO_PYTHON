#Escriba una función que determine el valor de los dos ítems que más veces se 
#encuentran dentro de una lista.


def leerInt(mensaje):
    cantidad = int(input(mensaje))
    return cantidad


def mayores(numeros):
    repetido = []
    unicos = []
    for i in numeros:
        if i not in unicos:
            unicos.append(i)
        else:
            if i not in repetido:
                repetido.append(i)
    print(unicos)
    print('Items que más se repiten en una lista son: ',repetido)
    

def main():
    cantidad = leerInt('Ingrese números: ')
    numeros = []

    for i in range(cantidad):
        numero = int(input(f'Números: [{i}]: '))
        numeros.append(numero)
    
    mayores(numeros)
    print(numeros)
        

main()
        





