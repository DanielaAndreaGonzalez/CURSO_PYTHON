#Dado un número mayor o igual a 1,determinar si es primo o no


def leerInt(mensaje):
    numero = int(input(mensaje))
    return numero


def es_primo(numero):
    divisiones = 0

    for i in range(1,numero +1):
        if numero %i ==0:
            divisiones +=1
    
    if divisiones == 2:
        es_num_primo = True
    else:
        es_num_primo = False
    return es_num_primo

def main():
    numero = leerInt('Digite un número mayor a cero: ')

    if numero <= 0:
        print('Debe ser número positivo ')
    else:
        if es_primo(numero):
            print(f'{numero} es número primo')
        else:
            print(f'{numero} no es un número primo')

main()