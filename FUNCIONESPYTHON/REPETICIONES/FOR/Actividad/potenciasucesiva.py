#Potencia de un número mediante potencia sucesiva


def leerInt(mensaje):
    numero = int(input(mensaje))
    return numero
 
def calcular_potencia(exponente,base):
    acu=1
    for i in range(exponente):
        acu *= base
    return acu

    



def main():
    m = leerInt('Ingrese la base: ')
    n = leerInt('Ingrese la potencia: ')
    potencia = calcular_potencia(n,m)
    print(potencia)


main()
    
