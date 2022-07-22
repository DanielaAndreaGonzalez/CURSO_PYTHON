#Programa que muestra si un espacio está ocupado o libre

ocupacion = [[False,False,False],
             [False,False,False],
             [False,False,False]]

puestos = {1:[0,0],2:[0,1],3:[0,2],
           4:[1,0],5:[1,1],6:[1,2],
           7:[2,0],8:[2,1],9:[2,2]}

def validar(puesto,ocupacion):
    
    for i in range(len(ocupacion)):
        for puesto in range(len(ocupacion)):
            if ocupacion[i][puesto] == False:
                cadena = 'Libre'    
            else:
                cadena = 'Ocupado'
                  
            #print(f'{ocupacion[i][j]:7d}',end = " ")
        #print()
    return cadena

def ocupar(puesto,ocupacion,validacion):
    
    if validacion == "Libre":
        for i in range(len(ocupacion)):
            for puesto in range(len(ocupacion[0])):
                ocupacion[i][puesto] = True
    
    return ocupacion

def liberar(puesto,ocupacion,validacion):
    
    if validacion == "Ocupado":
        for i in range(len(ocupacion)):
                for puesto in range(len(ocupacion[0])):
                    ocupacion[i][puesto] = False
    
    return ocupacion



validacion = validar(2,ocupacion)
print(validacion)
ocupacion = ocupar(2,ocupacion,validacion)
print(ocupacion[0][1])


validacion = validar(2,ocupacion)
print(validacion)
ocupacion = ocupar(2,ocupacion,validacion)
print(ocupacion[0][1])


validacion = validar(2,ocupacion)
print(validacion)
ocupacion = liberar(2,ocupacion,validacion)
print(ocupacion[0][1])

print('**********************')

validacion = validar(9,ocupacion)
print(validacion)
ocupacion = ocupar(9,ocupacion,validacion)
print(ocupacion[2][2])


validacion = validar(9,ocupacion)
print(validacion)
ocupacion = ocupar(9,ocupacion,validacion)
print(ocupacion[2][2])


validacion = validar(9,ocupacion)
print(validacion)
ocupacion = liberar(9,ocupacion,validacion)
print(ocupacion[2][2])



