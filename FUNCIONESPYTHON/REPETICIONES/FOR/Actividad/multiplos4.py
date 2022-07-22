#Programa que imprime los números desde el -100 al 0, en múltiplos de 4

numeros = range(-100,1)


for i in numeros:
    if i%4==0:
        res = i
        print(res)
