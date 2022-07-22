#Muestra los números entre 0 y 99 en cifras y en palabras


def convertir(valor):
    unidades = ('Cero','Uno','Dos','Tres','Cuatro','Cinco','Seis','Siete','Ocho',
                'Nueve','Diez','Once','Doce','Trece','Catorce','Quince',
                'Dieciséis','Diecisiete','Dieciocho','Diecinueve','Veinte')

    decenas = ('Veinti','Treinta','Cuarenta','Cincuenta',
                'Sesenta','Setenta','Ochenta','Noventa')
        
    if valor >= 0 and valor <=20:
            letras = unidades[valor]
    else:
        decena = valor //10-2
        unidad = valor %10

        if valor >=21 and valor <= 29:
            letras_decenas = decenas[decena]
            letras_unidades = unidades[unidad].lower()

            letras = letras_decenas + letras_unidades
        else:
            if valor >=30 and valor <= 99:
                letras = decenas[decena]
                if unidad >0:
                    letras = letras + 'y' + unidades[unidad].lower()
    return(letras)


print('\nNúmeros del 0 al 99\n')
for i in range(0,100):
    print(f'{i} ---> {convertir(i)}')
