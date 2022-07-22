#ciclo for

#for i in 'numero':
 #   print(i)

 #calcular el numero de vocales de una frase 
frase = str(input('ingrese una frase'))
vocales = 'aeiouAEIOU'
contador = 0
for i in frase:
    if i in vocales:
        contador = contador + 1
print('El número de vocales es: ',contador )