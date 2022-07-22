#Calcula el valor futuro de una cantidad en varios periodos de tiempo

def leerFloat(mensaje):
    cantidad = float(input(mensaje))
    return cantidad

def leerInt(mensaje):
    cantidad = int(input(mensaje))
    return cantidad

def valor_futuro(vp,i,n):
    vf = vp *(1 + i/100) **n
    return vf

def main():
    print('\nDigite los siguientes daots\n')
    vr_presente = leerFloat('Valor presente a invertir: ')
    interes = leerFloat('Tasa interés por período: ')
    periodo = leerInt('Cantidad de periodos: ')

    print('\n','Valor futuro por cada período'.center(50,'-'),'\n')

    per = 1

    while per <=periodo:
        vr_futuro = valor_futuro(vr_presente, interes, per)
        print(f'Período {per},valor futuro: {vr_futuro}')
        per +=1


main()





