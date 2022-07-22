#Programa muestra el uso y alcance de una variabe local y global

def funcion_uno():
    global var_ejemplo
    var_ejemplo = 'Soy local'
    print(var_ejemplo)

var_ejemplo = 'Soy global'
print(var_ejemplo)
funcion_uno()
print(var_ejemplo)