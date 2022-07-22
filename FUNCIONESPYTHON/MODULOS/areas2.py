#Ejemplo del módulo 2


import leer
import areas



calcular  = leer.leer_float('Ingrese para calcular: ')

base= leer.leer_float('Ingrese la base del triángulo: ')
altura =  leer.leer_float('Ingrese la altura del triángulo: ')
lado = leer.leer_int('Ingrese lado del cuadrado: ')

baseTri = leer.leer_float('Ingrese la base del rectángulo: ')
alturaTri = leer.leer_float('Ingrese la altura del rectángulo: ')

cadena = leer.leer_cadena('\nÁREAS:\n Triángulo,cuadrado,rectágulo ')



#Probando
#potencia = areas.potencia(4, 2)

triangulo = areas.triangulo(base, altura)
cuadrado = areas.cuadrado(lado)
rectangulo = areas.rectangulo(baseTri, alturaTri)
#print(potencia)
print(cadena,f'El area del triángulo es:{triangulo}\nEl área del rectángulo es: {rectangulo}\nEl área del cuadrado es: {cuadrado} ')
