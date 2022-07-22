#Hallar el promedio de los elementos con funciones



def hallarPromedio():
    acu =0
    promedio = 0
    tupla = (34,43,56,5,345,23)
    for i in tupla:
        acu = acu+i
    promedio = acu / len(tupla)
    
    print(round(promedio,3))
    
print('Promedio: ')
hallarPromedio()

    