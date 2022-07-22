'''Se tienen una cantidad de dinero en dólares, determinar su equivalente en pesos 
colombianos. Tenga en cuenta la tasa de cambio actual. 
'''


pesos = lambda dolares: dolares*3762

dolar = float(input('Ingrese en dolares '))
conversion = pesos(dolar)
print(f'{dolar}USD equivalente a {conversion} pesos')