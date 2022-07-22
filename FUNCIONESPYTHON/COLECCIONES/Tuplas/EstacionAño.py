#Determina la estación del año,dependiendo del mes que se digite


def leer_int(mensaje,minimo,maximo):
    seguir = True
    while seguir:
        numero = int(input(mensaje))
        if numero >= minimo and numero <= maximo:
            seguir = False
        else:
            print(f'\n¡Error!El dato debe estar entre {minimo} y {maximo} \n')
    return numero

def definir_estacion(mes):
    estaciones = ('Invierno','Primavera','Verano','Otoño')
    meses=('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')
    if mes == 12 or mes == 1 or mes ==2:
        estacion = 0
    elif mes >=3 and mes <=5:
        estacion =1
    elif mes >=6 and mes <= 8:
        estacion = 2
    else:
        estacion =3
    
    mes = mes-1

    return (meses[mes],estaciones[estacion])

mes = leer_int('Escriba el número de un mes: ',1,12)
nombre_mes,estacion = definir_estacion(mes)
print(f'A {nombre_mes} le corresponde {estacion}')



