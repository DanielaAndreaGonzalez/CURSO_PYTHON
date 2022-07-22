#Halla la división entera y el módulo entre dos números entre 1 y 1000

def leer_int(mensaje,minimo,maximo):
    seguir =True
    while seguir:
        numero = int(input(mensaje))
        if numero >= minimo and numero <= maximo:
            seguir = False
        else:
            print(f'\n¡Error! El dato debe estar entre {minimo} y {maximo}')
    return numero

def cociente_modulo(dividendo,divisor):
    cociente = dividendo // divisor
    modulo = dividendo % divisor
    return cociente,modulo

dividendo1 = leer_int('Ingrese divideno: ',1,1000)
divisor1 = leer_int('Ingrese divisor: ',1,1000)

cociente1,modulo1=cociente_modulo(dividendo1,divisor1)
print(f'\nEl cociente es: {cociente1}, el residuo es: {modulo1}')
