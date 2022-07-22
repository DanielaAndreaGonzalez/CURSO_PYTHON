'''
Tres hermanos forman una sociedad para comprar una propiedad. Cada uno de 
ellos invierte una suma diferente de dinero. Se necesita conocer el porcentaje 
que cada uno invirtió con relación al total de dinero invertido'''

def leerFloat(mensaje):
    cantidad=float(input(mensaje))
    return cantidad

def calcularTotal(cant1,cant2,cant3):
    total = cant1+cant2+cant3;
    return total
    
def definirPorcentaje(cant1,cant2,cant3,total):
    porcentaje1 = (cant1 / total)*100;
    porcentaje2 = (cant2 / total)*100;
    porcentaje3 = (cant3 / total)*100;
    salida = f'El porcentaje que cada persona dio es \n{cant1}: {porcentaje1}% \n{cant2} : {porcentaje2}%\n{cant3} : {porcentaje3}%'
    return salida

def main():
    cant1 = leerFloat('Ingrese la suma1: ')
    cant2 = leerFloat('Ingrese la suma2: ')
    cant3 = leerFloat('Ingrese la suma3: ')
    total = calcularTotal(cant1, cant2, cant3)
    porcentaje = definirPorcentaje(cant1, cant2, cant3, total)
    print('Total dinero invertido: $',total,'Porcentajes: \n',porcentaje)

main()