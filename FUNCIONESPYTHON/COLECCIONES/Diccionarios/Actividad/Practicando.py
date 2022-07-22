dic = {"nombres":["Kevin","Daniela","Andrea","Santiago"],"Apellidos":["Gonzalez","Henao","Narvaez","Vera"],"Dir":"Caicedonia"}


dic["Pais"] = 'Colombia'
print(dic)


dic['nombres'].append("Antonia")
dic["nombres"].append("Jesús")
dic["nombres"].append("Karla")
#for i,pos in range(len(dic["nombres"])):
 #   print(dic["nombres"][i])
    

for i,pos in enumerate(dic["nombres"]):
    print(i,dic["nombres"][i])



#Cómo agregar un nuveo valor a un lista de un valor de una llave de un diccionario      Ya
#Cómo agregar un valor nuevo a un diccionario dentro de un diccionario    Ya
#cómo recorrer un diccionario dentro de un diccionario  Ya