#Calcula la frecuencia cardiaca máxima de una persona

def leer_int(mensaje):
    numero = int(input(mensaje))
    return numero

def leer_booleano(mensaje):
    respuesta = input(mensaje).upper()

    if respuesta == 'S':
        respuesta = True
    else:
        respuesta = False

    return respuesta

def esActivo(edad,es_activo):
    es_mujer = leer_booleano('Es usted mujer [S] [N]?: ')
    if es_activo:
        if es_mujer:
            fcmax = 214 - (0.8*edad)
        else:
            fcmax = 209 - (0.7*edad)
    else:
        fcmax = 220-edad
    return fcmax

def main():
    edad = leer_int('¿Cuál es su edad?: ')
    es_activo = leer_booleano('¿Practica actividad física regularmente [S] [N]?: ')
    fcmax = esActivo(edad,es_activo)
    print(f'\nSu frecuencia cardiaca máxima es de {fcmax}')

main()




