#opcion B (elif)

b = int(input('Ingrese el número: '))
if b < 0:
    R = 'negativo'
elif b == 0:
    R = 'neutro'
else:
    R = 'positivo'
print (' el número es : ', R)
