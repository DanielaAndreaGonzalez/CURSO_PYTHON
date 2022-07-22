#Indicar para que se utilizan las siguientes funciones con un ejemplo

#Función len
#Devuelve la longitud de una cadena de caracteres o el número de elementos de una lista
cadena = input('Nombre: ')
largo = len(cadena)
print(largo)

#append()
#Permit agregar registros a una lista 
cantidad = int(input('Digite la cantidad de elementos: '))

lista = []

for i in range(cantidad):
    numero = int(input(f'Elementos [{i}]: '))
    lista.append(numero)
for i in range(cantidad):
    print(lista[i],end=" ")   


#Count()
#Cuenta le número de veces que un elemento x aparece
contar= lista.count(1)
print('\nEn la lista aparece :',contar,'veces')




