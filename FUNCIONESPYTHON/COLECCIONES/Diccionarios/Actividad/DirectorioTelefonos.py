#Construya un programa para gestionar un diccionario que almacene una agenda con el teléfono y nombre de sus contactos

def leerInt(mensaje,minimo,maximo):
    siga=True
    while True:
        try:
          while siga:
            numero = int(input(mensaje))        
            if len(str(numero)) >= minimo and len(str(numero)) <= maximo:
                siga=False
                return numero
            else:
                print(f'¡Error! El dato debe estar entre {minimo} y {maximo}')
        except ValueError:
             print('Debes escribir un número: ')
  
def leerCadena(mensaje,minimo):
    siga = True
    while siga:
        cadena = input(mensaje)
        if len(cadena) >= minimo:
            siga = False
        else:
            print(f'¡Error! Debe digitar mínimo {minimo} caracteres')
    return cadena

def leerBooleano(mensaje):
    siga = "S"
    while siga == "S":
        respuesta = input(mensaje).upper()
        if respuesta == 'S' or respuesta == 'N':
            siga = False
        else:
            print('¡Error! Solo S o N')
    return respuesta

def crearDirectorio():
    directorio = {}
    siga = "S"
    while siga == "S":
        print('Crear directorio\n')
        numero = leerInt('\n Número teléfono:  ',8,12)
        nombre = leerCadena('Nombre contacto: ',3)

        directorio[numero] = nombre
        siga = leerBooleano('\n¿Desea continuar adicionando contactos? [S][N]? ')

    
    return directorio

def consultarDirectorio(directorio):
    siga = "S"
    
    while siga == "S":
        numero = leerInt('\nNúmero: ',8,12)
        nombre = directorio.get(numero,"No")
        if nombre == "No":
            print("No hay registro en esa fecha")
        else:
            print(f'Número: {numero} Contacto: {nombre}')
        siga = leerBooleano('\n¿Desea continuar consultando [S][N]?: ').upper()
    return directorio


def modificarDirectorio(directorio):
    print('\nModificar selección')
    siga = "S"
    while siga == "S":
        numero = leerInt('\nNúmero: ',8,12)
        nombre = directorio.get(numero,"No")
        if nombre == "No":
            print('\n No hay registro de ese número')
        else:
            print(f'\nNombre a modificar: {nombre}')
            nombre = leerCadena('\nNuevo nombre: ',3)
            directorio[numero] = nombre
            print('\nSe ha realizado el cambio satisfactoriamente')
            nombre = directorio.get(numero)
            print(f'\nEl nuevo número {numero} es de {nombre}')

        siga=input('\n¿Desea continuar modificando[S][N]?: ').upper()
    return directorio

def eliminar_directorio(directorio):
    print('\nBorrado de un contacto')
    siga = "S"
    while siga == "S":
        numero = leerInt('\nNúmero',8,12)
    
        nombre = directorio.get(numero,"No")

        if nombre == "No":

            print('\nNo hay registro de ese contacto')
        else:
            print(f'\nContacto a borrar: {nombre}')
    
            seguro = leerBooleano('\n¿Desea proceder con el borrado [S][N]?: ')
            if seguro == "S":
                del directorio[numero]
                print('\nSe ha realizado el borrado')
            else:
                print('\nNo se hizo borrado del contacto seleccionado')
        siga = leerBooleano('\n¿Desea continuar borrando [S][N]?: ')
    return directorio

def imprimirAgenda(directorio):
    for elemento in directorio.items():
        print(elemento[0],elemento[1])


def main():
    siga = "S"
    agenda = crearDirectorio()
    while siga == "S":
        print('\nMenú selecciones: \n 1.Crear \n2.Consultar \n3.Modificar \n4.Eliminar \n5.Ver agenda \n6.Salir')
        opcion = int(input("Ingrese la opción: "))
        if opcion == 1:
            print('Agenda: \n')
            print(agenda)
        elif opcion == 2:
            mirar= consultarDirectorio(agenda)
            print('Agenda: \n')
            print(mirar)
        elif opcion == 3:
            modificar = modificarDirectorio(agenda)
            print(modificar)
        elif opcion == 4:
            eliminar = eliminar_directorio(agenda)
            print(eliminar)
        elif opcion ==5:
            imprimirAgenda(agenda)
        elif opcion==6:
            exit()
        else:
            print('Opciones incorrectas')
        siga = leerBooleano('¿Desea continuar con el menú? [S][N]? ')
    
main()

