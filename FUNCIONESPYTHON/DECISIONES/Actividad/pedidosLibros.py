#Programa que calcula el valor de un pedido


def leerInt(mensaje):
    cantidad = int(input(mensaje))
    return cantidad

def leerFloat(mensaje):
    cantidad = float(input(mensaje))
    return cantidad

def leerString(mensaje):
    cadena = input(mensaje)
    return cadena

def valor_libro(cantidad_lib,envio):
    if cantidad_lib>=1 and cantidad_lib <=3 and envio=='nacional' :
        costo = cantidad_lib * 4500
    elif cantidad_lib>=1 and cantidad_lib <=3 and envio=='importado':
        costo = cantidad_lib * 6000
    elif cantidad_lib>=4 and cantidad_lib <=6 and envio=='nacional':
        costo = cantidad_lib * 7000
    elif cantidad_lib>=4 and cantidad_lib <=6 and envio=='importado':
        costo = cantidad_lib * 12000
    elif cantidad_lib >=7 and envio == 'nacional':
        costo = cantidad_lib * 8500
    else: 
        costo = cantidad_lib * 15000
    return costo


def zonas(zona,valorLibros,envio):
    if zona == 'centro' and envio == 'nacional':
        valor = (0.02 * valorLibros) + valorLibros
    elif zona == 'norte' and envio == 'nacional':
        valor = (0.05 * valorLibros) + valorLibros
    elif zona == 'sur' and envio == 'nacional':
        valor = (0.07 * valorLibros) + valorLibros
    elif zona == 'oriente' or zona == 'occidente' and envio == 'nacional':
        valor = (0.04 * valorLibros) + valorLibros
    else:
        valor = valorLibros
    return valor

def entrega_in(envio,opc):
    if opc == 's' and envio == 'nacional':
        costo = 1300
    else:
        costo =0.0
    return costo

def calcularTotal(entrega,zona):
    total = entrega + zona
    return total

def main():
    cantidad = leerInt('Ingrese la cantidad de libros: ')
    envio = leerString('Ingrese a dónde es el envío: nacional o importado: ')
    zona = leerString('Ingrese la zona a la que pertenece: ')
    entrega = leerString('¿Desea entrega inmediata? \n[s]-[n]\n>>>')
    valor = valor_libro(cantidad, envio)
    pagar_zona = zonas(zona,valor,envio)
    entrega_inmediata= entrega_in(envio, entrega)
    total = calcularTotal(entrega_inmediata,pagar_zona)
    print('Valor libros: ',valor)
    print('Valor según la zona: ',pagar_zona)
    print('Valor entrega: $',entrega_inmediata)
    print('Total: ',total)
    


main()






