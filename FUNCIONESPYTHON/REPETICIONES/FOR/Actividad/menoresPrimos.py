#Programa que calcula los número menores a los primos



def leerInt(mensaje):
    cantidad = int(input(mensaje))
    return cantidad


def es_primo(numero):
    divisiones = 0

    if numero >0:
        for i in range(2,numero):
            divisiones = 2
            primo = True
            while primo and divisiones < i:
                if i % divisiones == 0:
                    primo = False
                else:
                    divisiones +=1
            if primo:
              print(i,'Es primo')
    else:
         print('El número ingresado no es correcto.Inténtelo nuevamente.')
                
        
def main():
    numero = leerInt('Ingrese num: ')

    es_primo(numero)

main()

