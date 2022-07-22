#Convertir binario a decimal
def convertir():

    binario = (1,0,1,0,0,1,0,1,0,1,0,0,0,1,1,1,0)
    inver = len(binario) -1
    decimal = 0
    
    for i in binario:
        pote = int(i)
        multiplicacion = pote * 2 ** inver
        decimal = decimal + multiplicacion
        inver -=1
    print('Decimal',decimal)
    
    
convertir()
   

