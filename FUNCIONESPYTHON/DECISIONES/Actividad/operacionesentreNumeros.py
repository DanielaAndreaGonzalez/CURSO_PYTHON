#Programa que lee dos números y una operación
#básica.

def leerInt(mensaje):
    cantidad = int(input(mensaje))
    return cantidad

def leerFloat(mensaje):
    cantidad = float(input(mensaje))
    return cantidad

def leerString(mensaje):
    cadena = input(mensaje)
    return cadena

def calcular_operaciones(numero1,numero2,operacion):
    if operacion == '+':
        resultado = numero1 + numero2
    elif operacion == '-':
        resultado = numero1 - numero2
    elif operacion == '.' or operacion == 'x':
        resultado = numero1 * numero2
    elif operacion == '/':
        if  numero2 >0:
            resultado = numero1 / numero2
        else:
            resultado = 'Error'
    else:
        resultado = 'Operación inválida'
    return resultado

def main():
     operacion = leerString('Ingrese la operación: \n[+]Suma\n[-]Resta\n[.][x]Multiplicación\n[/]División\n>>>')
     num1 = leerInt('Ingrese número1 :')
     num2 = leerInt('Ingrese número2: ')
     resultado = calcular_operaciones(num1, num2, operacion)
     print(resultado)


main()