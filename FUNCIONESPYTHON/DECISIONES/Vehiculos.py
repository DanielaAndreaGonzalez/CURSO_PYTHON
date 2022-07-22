#Alquiler de vehículos según su tipo y su recorrido 


def leerFloat(mensaje):
    cantidad = float(input(mensaje))
    return cantidad


def leerInt(mensaje):
    cantidad = int(input(mensaje))
    return cantidad


def leerString(mensaje):
    cadena = input(mensaje)
    return cadena


def valor_incremento(vehi,kms):
    if vehi==1:
        if kms >=0.0 and kms <20.0:
            incremento = kms * 500
        elif kms >=20.1 and kms<=40.0:
            incremento = kms * 600
        elif kms >=40.1 and kms <=60.0:
            incremento = kms * 700
        else:
            incremento = kms * 800
    else:
        if kms >= 0.0 and kms <=20.0:
            incremento = kms * 700
        elif kms >= 20.1 and kms <=40.0:
            incremento = kms * 800
        elif kms >=40.1 and kms <=60.0:
            incremento = kms * 1000
        else:
            incremento = kms * 1200
    return incremento


def valor_descuento(kms,valor_bruto):
    if kms >80:
        porcentaje_descuento = 0.10
    else:
        porcentaje_descuento = 0.0

    return valor_bruto * porcentaje_descuento


def calcularValor_neto(descuento,valor_bruto):
    neto = valor_bruto - descuento
    return neto


def main():
    print('Digite los siguientes datos: ')
    vehiculo = leerString('\nTipo de vehículo \n[1] Automóvil \n[2] Camioneta\n>>>')
    horas = leerInt('Horas de alquiler: ')
    kms = leerFloat('Kilómetros recorridos: ')

    incremento = valor_incremento(vehiculo, kms)
    valor_bruto = horas * 10000 + incremento
    descuento = valor_descuento(kms, valor_bruto)
    valor_neto = calcularValor_neto(descuento, valor_bruto)

    print(f'El valor a pagar antes de descuento es: {valor_bruto}')
    print(f'El valor del descuento es: {descuento}')
    print(f'El valor a pagar es: {valor_neto}')

main()