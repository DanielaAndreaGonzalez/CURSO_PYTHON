#Programa que calcula la suma de pares e impares 

def leerInt(mensaje):
    cantidad = int(input(mensaje))
    return cantidad

def calcularpares(num1,num2):
    total = 0
    
    sumpar=0
    sumimpar=0
    while num1 >total:
        if num1%2==0 or num2%2==0:
            sumpar = num1+num2
            mensaje = f'Pares: {sumpar} \nImpares {sumimpar}'
        else:
            sumimpar = num1+num2
            mensaje = f'Pares: {sumpar} \nImpares {sumimpar}'
        total +=1
        
    return mensaje

def main():
    num1 = leerInt('Num1: ')
    num2 = leerInt('Num2: ')
    
    calcular = calcularpares(num1,num2)
    print(calcular)

main()

