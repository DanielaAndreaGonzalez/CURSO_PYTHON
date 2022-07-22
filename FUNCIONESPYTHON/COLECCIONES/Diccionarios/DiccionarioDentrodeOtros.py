
elementos = {"Metales":{"Oro":{"O":"Au","I":"H","B":"Bg"},"Plata":"Ag","Zing":"Zn","Cobre":"Cu"},"Gas Noble":{"Helio":"He","Neon":"Ne","Argon":"Ar"},"No-metal":{"Oxigeno":"O","Bromo":"Br","Cloro":"Cl"}}

elementos["Metales"]["Cobres"] = "Co"
elementos["Metales"]["Cubierots"] = "Cubir" 
elementos["Metales"]["Oro"]["Esmeralda"] = "Es" 

elementos["Hola"] = "hola" 

elementos["Metales"]["Oro"]["Esmeralda"] = "Mr" 

lista = list(elementos.items())

#element = elementos.items()
#print(element)

for simbolo in elementos["Metales"]["Oro"].items():
    print(simbolo)
    

#('O', 'Au')
#('I', 'H')
#('B', 'Bg')
#('Esmeralda', 'Mr') 




#('O', 'Au','daniela')
#('I', 'H','daniela')
#('B', 'Bg','daniela')
#('Esmeralda', 'Mr','daniela') 

