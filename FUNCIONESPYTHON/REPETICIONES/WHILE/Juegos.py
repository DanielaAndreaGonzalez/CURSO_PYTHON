#Programa para simular juego de niños 


from random import randint
#from math import ceil


def leerFloat(mensaje):
    while True:
        numero = input(mensaje)
        try:
            numero = float(numero)
            return numero
        except ValueError:
            print('La entrada es incorrecta, escribe un número ')
    

def leerBooleano(mensaje):
    siga=True
    while siga:
        respuesta = input(mensaje).upper()
        if respuesta == "S" or respuesta == "N":
            siga = False
        else:
            print(f'¡Error! Debe digitar S o N')
    return respuesta

    

def operaciones():
    operacion1 = randint(1,4)
    
    if operacion1 == 1:
        operar = '*'
    elif operacion1 == 2:
        operar = '+'
    elif operacion1 == 3:
        operar = '-'
    elif operacion1 == 4:
        operar = '/'
    return operar 


def jugar():
    buenas = malas = 0
    pausa = "S"
    
    while pausa =="S":
           
        numero1 = randint(1, 9)
        numero2 = randint(1, 9)

        calcular = operaciones()
        if calcular == '+':
            res = numero1 + numero2
        elif calcular == '-':
            res = numero1 - numero2
        elif calcular == '*':
            res = numero1 * numero2
        elif calcular == '/':
            res= round((numero1 / numero2),2)
            
       # print(res)

        resultado = leerFloat(f'\n{numero1} {calcular} {numero2} =')
        
        if resultado == res:
            buenas += 1
            print('Muy bien...¡Felicitaciones!')
        else:
            malas +=1
            print(f'Error... La respuesta correcta es: {res}')

        pausa = leerBooleano('\nOtra operación [S][N]?: ')
        
    print(f'\nRespuestas acertadas: {buenas}')
    print(f'Respuestas erradas: {malas}')

    

    

jugar()