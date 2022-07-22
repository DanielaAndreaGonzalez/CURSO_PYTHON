#Crear un diccionario con las selecciones campeonas mundiales de fútbol

def crear_selecciones():
    print('\nCampeones mundiales de fútbol: ')

    selecciones = {}
    siga = "S"
    while siga == "S":
        anio = leer_int('\nAño: ',1930,2018)
        equipo = leer_cadena('Selección campeona: ',3)

        selecciones[anio] = equipo

        siga = leer_booleano('\n¿Desea continuar adicionando [S][N]?: ')

    return selecciones

def leer_int(mensaje,minimo,maximo):
    siga=True
    while siga:
        numero = int(input(mensaje))
        if numero >= minimo and numero <= maximo:
            siga=False
        else:
            print(f'¡Error! El dato debe estar entre {minimo} y {maximo}')
    return numero

def leer_cadena(mensaje,minimo):
    siga=True
    while siga:
        cadena = input(mensaje)
        if len(cadena) >= minimo:
            siga=False
        else:
            print(f'¡Error! Debe digitar mínimo {minimo} caracter')
    return cadena

def leer_booleano(mensaje):
    siga=True
    while siga:
        respuesta = input(mensaje).upper()
        if respuesta == "S" or respuesta == "N":
            siga = False
        else:
            print(f'¡Error! Debe digitar S o N')
    return respuesta

selecciones = crear_selecciones()
print('\nEstas son las selecciones campeonas que se registraron: ')
print(selecciones)
