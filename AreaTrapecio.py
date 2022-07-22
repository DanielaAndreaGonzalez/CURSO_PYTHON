'''
El área de un trapecio se obtiene, de la mitad de su altura por la suma de sus 
bases (base mayor y base menor). Lea los datos necesarios para calcular e 
informar su área. '''


def leerInt(mensaje):
    cantidad=int(input(mensaje))
    return cantidad


def calcularAreaTrapecio(h,baseMayor,baseMenor):
    area = (h/2)*(baseMayor+baseMenor);
    return area

def main():
    altura = leerInt('Ingrese la altura en metros: ')
    baseMayor = leerInt('Ingrese la base mayor en metro: ')
    baseMenor = leerInt('Ingrese la base menor en metros: ')
    area = calcularAreaTrapecio(altura, baseMayor, baseMenor)
    print(f'Area de trapecio es: {area} m2')

main()