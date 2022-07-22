#OPCION A (IF -ELSE)
#verificar si un numero es positivo neutro o negativo

a = int(input('ingrese un numero: '))
if a < 0:
    R = 'negativo'
else:
    if a == 0:
        R = 'neutro'
    else:
        R = 'positivo'

print ('el número es : ', R)