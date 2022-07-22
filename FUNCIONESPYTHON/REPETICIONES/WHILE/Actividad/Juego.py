#Programa de juego 

from random import randint


def leerInt(mensaje):
    numero = int(input(mensaje))
    return numero


def jugar():

    
    cont = 1
    numero = randint(1,15)
    while (cont<=5):
        

        leer = leerInt(f'Tiene {6-cont} oportunidades \nAdivine el número: ')

        if leer == numero:
            mensaje = f'Felicidades adivinó {numero} == {leer} lo hizo en {cont} oportunidades'   
            cont =5
        else:
            if cont == 5:
                mensaje = f'Lo siento será en una próxima oportunidad ,correcto: {numero}'
            else:
                if leer > numero :
                    mensaje = f'Número digitado es mayor'
                elif leer < numero:
                    mensaje = f'Número digitado es menor'
        print(mensaje)
        cont +=1
    print(f'Número correcto {numero}')
    
    
        
jugar()


