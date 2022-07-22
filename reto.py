
def sector(x,y):
    #Las siguientes lineas de código validan si está dentro de la antena celular
    if x ==2 and y==9 and y==3:
        resultado = ""    
    elif x == 8 and y == 9 and y==3:
        resultado = ""                
    elif x ==5 and y ==6:
        resultado = ""
    #La parte del else valida si comparte la linea con el otro sector
    else:
        if (x==5) and (y>=3) and (y<=5):
            resultado = "Deniska está entre el Sector 3 y 4"
        elif  (x>=2) and (x<=5) and y==6:
            resultado = "Deniska está entre el Sector 1 y 3"                  
        elif (x>=5) and (x<=8) and y==6:
            resultado = "Deniska está entre el sector 2 y 4"
        elif (x ==5) and (y>6) and (y<=9):
            resultado = "Deniska está entre el Sector 1 y 2"
        #Este else valida en que sector se encuentra
        else:                     
            if (x >2) and (x <=5) and (y>=6) and (y<=9):
                resultado = "S1"
            else:
                if (x>=5) and (x<=8) and (y>=6) and (y<=9):
                    resultado = "S2"
                else:
                    if (x>=2) and (x<=5) and (y>=3) and (y<=6):
                        resultado = "S3"
                    elif (x>=5) and (x<=8) and (y>=3) and (y<=6):
                        resultado = "S4"
                    #Finalmente este último else dice que si no cumple con lo anterior es porque
                    #Deniska ha escapado
                    else:
                        resultado = "Deniska ha escapado"
     
    return resultado


x = float(input("Ingrese coordenada de x: "))
y = float(input("Ingrese la coordenada y: "))
print(sector(x,y))
