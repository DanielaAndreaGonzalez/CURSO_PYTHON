#Crear un diccionario con las seleecciones campeonas mundiales de fútbol

print('\nCampeones mundiales de fútbol')

selecciones = {}
siga = "S"

while siga == "S":
    anio = int(input('\nAño: '))
    equipo = input("Selección campeona: ")

    selecciones[anio] = equipo

    siga = input("\n¿Desea continuar adicionando [S][N]?: ").upper()

print('\nEstas son las seleecciones campeonas que se registraron: ')
print(selecciones)