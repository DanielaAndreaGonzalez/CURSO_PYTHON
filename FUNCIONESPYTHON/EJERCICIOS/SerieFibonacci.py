#Serie fibonacci
#Ejemplo
'''
w1 + w2 = s
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
3 + 5 = 8 
5 + 8 = 13
8 + 13 = 21

'''

n = int(input('Ingrese un numero: '))
w1 = 1
w2 = 1
s = 0
c = 0 

if n <= 0:
    print('error')
elif n== 1:
    print(w1)
else:
    while c < n:
        print(w1)
        s = w1 + w2
        #Actualizar los datos 
        w1 = w2
        w2 =  s
        c += 1
        

