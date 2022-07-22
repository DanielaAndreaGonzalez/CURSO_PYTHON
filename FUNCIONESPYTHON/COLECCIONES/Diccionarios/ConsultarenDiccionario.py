#Consultar una selección dentro del diccionario

def leerInt(mensaje):
    numero = int(input(mensaje))
    return numero



def main():
    selecciones = {1994:"Brasil",1998:"Francia",2002:"Brasil",2006:"Italia",2010:"España",2014:"Alemania",2018:"Francia"}

    siga = "S"
    while siga == "S":
        anio = leerInt('\n¿De cuál año desea conocer la selección campeona?: ')

        equipo = selecciones.get(anio,"No")

        if equipo == "No":
            print("No hay registro en esa fecha")
        else:
            print(f'La selección campeona en el {anio} fue {equipo}')
        siga = input('\n¿Ddesea continuar [S][N]?: ').upper()

main()
    
