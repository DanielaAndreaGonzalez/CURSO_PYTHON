#Programa que determina cuánto números hay en la tuplas


binario = (1,0,1,0,0,1,0,1,0,1,0,0,0,1,1,1,0)


unos= binario.count(1)
ceros = binario.count(0)

print('cantidad de 1s: ',unos,'cantidad de ceros: ',ceros)