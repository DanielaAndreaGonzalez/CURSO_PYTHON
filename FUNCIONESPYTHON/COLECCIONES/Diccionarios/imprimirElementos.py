

elementos = {"Cobre":"Cu","Oro":"Au","Helio":"He","Plata":"Ag","Oxígeno":"O"}
#Consulta en un elemento especifico
#print(elementos["Oro"])
#simbolo = elementos["Oro"]
#print(simbolo)
#Uso del método get con un solo parámetro
#Si no existe el resultado es de tipo None
#simbolo = elementos.get("Hidrogeno")
#print(simbolo)
#Uso del método get con dos parámetros
print(elementos.get("Hidrogeno","No registrado"))
