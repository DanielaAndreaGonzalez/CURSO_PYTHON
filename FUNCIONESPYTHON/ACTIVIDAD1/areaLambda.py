#Area de un triángulo usando la siguiente fórmula


area = lambda b,h:b*h/2


base = float(input('Ingrese la base: '))
altura = float(input('Ingrese la altura: '))
resultado = area(base,altura)
print(f'Area {resultado}')