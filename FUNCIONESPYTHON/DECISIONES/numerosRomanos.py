#Programa números romanos

def leer_int(mensaje):
    cantidad = int(input(mensaje))
    return cantidad

def mirar(numero):
    if numero ==1:
        mensaje = 'I'
    else:
        if numero ==5:
            mensaje = 'V'
        else:
            if numero==10:
                mensaje = 'X'
            else:
                if numero ==50:
                    mensaje = 'L'
                else:
                    if numero == 100:
                        mensaje = 'C'
                    else:
                        if numero == 500:
                            mensaje = 'D'
                        else:
                            if numero == 1000:
                                mensaje = 'M'
                            else:
                                if numero <=0:
                                    mensaje = 'Es negativo,no existe en romano'
                                else:
                                    mensaje = 'No es válido'
    return mensaje

def main():
    numero = leer_int('Ingrese número: ')
    romano = mirar(numero)
    print(romano)

main()
