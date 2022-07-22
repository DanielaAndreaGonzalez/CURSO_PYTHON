#Determinar clase de triángulo

def leerFloat(mensaje):
    cantidad = float(input(mensaje))
    return cantidad


def clasificarTriangulo(angulo_interno,an2,an3):
    if angulo_interno <90 and an2<90 and an3<90:
        mensaje = 'ácutangulo'.upper()
    elif angulo_interno ==90 and an2<90 and an3 <90:
        mensaje = 'rectángulo'.upper()
    elif angulo_interno >90 and an2<90 and an3 <90:
        mensaje = 'obtusángulo'.upper()
    else:
        mensaje = 'No cumple'
    return mensaje

def main():
    an_interno = leerFloat('Ángulo interior: ')
    an_2 = leerFloat('Ángulo 2: ')
    an_3 = leerFloat('Ángulo 3: ')
    clasificar = clasificarTriangulo(an_interno, an_2, an_3)
    print(clasificar)

main()