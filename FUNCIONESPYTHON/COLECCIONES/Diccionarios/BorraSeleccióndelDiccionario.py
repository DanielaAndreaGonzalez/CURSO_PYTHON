#Borra una selección del diccionario

selecciones = {1994:"Brasil",1998:"Francia",2002:"Brasil",2006:"Italia",2010:"España",2014:"Alemania",2018:"Francia"}

print('\nBorrado de una selección')
siga = "S"
while siga == "S":
    anio = int(input('\nAño: '))

    equipo = selecciones.get(anio,"No")

    if equipo == "No":
        print('\nNo hay registro en esa fecha')
    else:
        print(f'\nSelección a borrar: {equipo}')
        seguro = input('\n¿Desea proceder con el borrado [S][N]?: ').upper()
        if seguro == "S":
            del selecciones[anio]
            print('\nSe ha realizado el borrado')
        else:
            print('\nNo se hizo borrado de la fecha seleccionada')

    siga = input('\n¿Desea continuar [S][N]?: ').upper()


