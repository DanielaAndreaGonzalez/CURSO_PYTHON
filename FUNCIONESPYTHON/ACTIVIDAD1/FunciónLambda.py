#Suma usando una función lambda


sumar = lambda num1,num2:num1+num2

numero1= float(input('Ingrese un número: '))
numero2 = float(input('Ingrese otro número: '))

resultado = sumar(numero1,numero2)
print(f'El resultado de l asuma es: {resultado}')