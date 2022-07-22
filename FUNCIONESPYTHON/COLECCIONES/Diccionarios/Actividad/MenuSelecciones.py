#Programa que contiene el menú para las selecciones 

def leer_int(mensaje):
    while True:
        numero = input(mensaje)
        try:
            numero = float(numero)
            return numero
        except ValueError:
            print('La entrada es incorrecta, escribe un número ')
    

def leer_cadena(mensaje,minimo):
    siga=True
    while siga:
        cadena = input(mensaje)
        if len(cadena) >= minimo:
            siga = False
        else:
            print(f'¡Error! Debe digitar mínimo {minimo} caracteres')
    return cadena

def leer_booleano(mensaje):
    siga = True
    while siga:
        respuesta = input(mensaje).upper()
        if respuesta == "S" or respuesta == "N":
            siga = False
        else:
            print('¡Error! Solo S o N')
    return respuesta


def eliminar_seleccion(selecciones):
    print('\nBorrado de una selección')
    siga = "S"
    while siga == "S":
        anio = leer_int('\nAño:')
    
        equipo = selecciones.get(anio,"No")

        if equipo == "No":

            print('\nNo hay registro en esa fecha')
        else:
            print(f'\nSelección a borrar: {equipo}')
    
            seguro = leer_booleano('\n¿Desea proceder con el borrado [S][N]?: ')
            if seguro == "S":
                del selecciones[anio]
                print('\nSe ha realizado el borrado')
            else:
                print('\nNo se hizo borrado de la fecha seleccionada')
        siga = leer_booleano('\n¿Desea continuar borrando [S][N]?: ')

def crear_seleccion():
    selecciones = {}
    siga = "S"
    while siga == "S":
        print('Crear selección\n')
        anio = leer_int('\nAño: ')
        equipo = leer_cadena('Selección campeona ',3)

        selecciones[anio] = equipo

        siga=leer_booleano('\n¿Desea continuar adicionando [S][N]?: ')
    return selecciones


def modificar_seleccion(selecciones):
    
    print('\nModificar selección')
    siga = "S"
    while siga == "S":
        anio = leer_int('\nAño: ')
        equipo = selecciones.get(anio,"No")
        if equipo == "No":
            print('\n No hay registro en esa fecha')
        else:
            print(f'\nSelección a modificar: {equipo}')
            equipo = leer_cadena('\nNueva Selección: ',3)
            selecciones[anio] = equipo
            print('\nSe ha realizado el cambio satisfactoriamente')
            equipo = selecciones.get(anio)
            print(f'\nLa nueva selección para el año {anio} es: {equipo}')

        siga=input('\n¿Desea continuar modificando[S][N]?: ').upper()
    

def consultar_seleccion(selecciones):
    siga = "S"
    while siga == "S":
        anio = leer_int('\nAño: ')
        equipo = selecciones.get(anio,"No")
        if equipo == "No":
            print("No hay registro en esa fecha")
        else:
            print(f'La selección campeona en el {anio} fue {equipo}')
        siga = leer_booleano('\n¿Desea continuar consultando [S][N]?: ').upper()

def main():
    siga = "S"
    selecciones = {1994:"Brasil",1998:"Francia",2002:"Brasil",2006:"Italia",2010:"España",2014:"Alemania",2018:"Francia"}
    print('\nMenú selecciones: \n 1.Crear \n2.Consultar \n3.Modificar \n4.Eliminar \n5.Salir')
    
    while siga == "S":
        opcion = int(input("Ingrese la opción: "))
        if opcion == 1:
            selecciones = crear_seleccion()
        elif opcion == 2:
             consultar_seleccion(selecciones)
        elif opcion == 3:
            modificar_seleccion(selecciones)
        elif opcion == 4:
            eliminar_seleccion(selecciones)
        elif opcion ==5:
            exit()
        else:
            print('Opciones incorrectas')
        siga = leer_booleano('¿Desea continuar con el menú? [S][N]')



main()
    







    
