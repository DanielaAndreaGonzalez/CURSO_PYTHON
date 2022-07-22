#CALIFICACION DE NOTAS
#DATOS:
# N : NOTAS
# R : RESPUESTA

N = float(input('Ingrese su nota: '))
if N <= 50:
    R = 'REPROBADO'
elif N <= 80:
    R = 'APROBACION'
elif N <= 90:
    R = 'SOBRESALIENTE'
else:
    R = 'EXCELENTE'

print ('Su nota ',N,R)
