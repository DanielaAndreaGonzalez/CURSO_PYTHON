#Modifica el nombre de una selección

selecciones = {1994:"Brasil",1998:"Francia",2002:"Brasil",2006:"Italia",2010:"España",2014:"Alemania",2018:"Francia"}

print('\nModificar selección')
siga = "S"
while siga == "S":
    anio = int(input('\nAño: '))

    equipo = selecciones.get(anio,"No")

    if equipo == "No":
        print('\nNo hay registro en esa fecha')
    else:
        print(f'\nSelección a modificar: {equipo}')
        equipo = input('\nNueva Selección: ')
        selecciones[anio]=equipo
        print('\nSe ha realizado el cambio satisfactoriamente')
        equipo = selecciones.get(anio)
        print(f'\nLa nueva selección para el año {anio} es: {equipo}')

        siga=input('\n¿Desea continuar [S][N]?: ').upper()


    