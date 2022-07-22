#Usando el for en una lista


i=0
lista = [1,2,3,4,5,6,7,8,9,10]
for numero in lista:
    print(f'{numero} ocupa la posición {i}')
    i +=1

#Otra forma

for i,numero in enumerate(lista):
    print(f'{numero} ocupa la posición {i}')
    