#Números perfectos
#Un número perfecto es un número natural que cumple que es igual a la suma de sus divisores propios

def leerInt(mensaje):
    cantidad = int(input(mensaje))
    return cantidad

def calcularPerfecto(n):
    num =0
    suma=0
    for i in range(1,n):
        num = n%i
        if num==0:
            #print(i)
            suma=suma + i
            print(suma)
    if suma == n:
        mensaje = 'Es perfecto'
    else:
        mensaje = 'No es perfecto'
    return mensaje

def main():
    n = leerInt('Número: ')
    calcular = calcularPerfecto(n)
    print(calcular)

main()

        
 #6  i
 # 6/1=6 
 # 6/2 = 3
 #6/3=2
 #6/4=1.5
 #6/5=1.2
 
 #1+2+3=6

