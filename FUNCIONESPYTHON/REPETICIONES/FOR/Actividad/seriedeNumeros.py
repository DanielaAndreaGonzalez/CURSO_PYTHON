#Programa que imprime serie de numeros

def leerInt(mensaje):
    cantidad = int(input(mensaje))
    return cantidad


n=leerInt('Número: ')


for i in range(1,n+1):
    if i%2==1:
        print(i)
    

for i in range(1,n+1,2):
    print(i)

