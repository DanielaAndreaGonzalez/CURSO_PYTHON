#serie A B A B A B A.....

# w = interruptor

n = int(input('Ingrese un número: '))

w = 0
for i in range(1,n+1):
    if w==0:
        print('A')
        w = 1
    else:
        print('B')
        w = 0