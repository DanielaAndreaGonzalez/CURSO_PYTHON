#mostra los n primeros numeros en forma descendiente
#for i in range (n,0,-1):
   # print(i)
   #La suma de los primeros n numeros
n=int(input('Ingrese un numero: '))
suma = 0
for i in range(1,n +1):
    suma = suma + i
print('La suma de los n numero hasta',n, 'es: ', suma)

