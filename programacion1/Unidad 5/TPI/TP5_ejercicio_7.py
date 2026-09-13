''''Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de
una semana.
● Calcular el promedio de las mínimas y el de las máximas.
● Mostrar en qué día se registró la mayor amplitud térmica.'''
temperatura_min = 0
temperatura_max = 0
acumulador_min = 0
acumulador_max = 0
amplitud_maxima = 0
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
semana = [
    [0,10], #lunes
    [1,30], #Martes
    [10,12], #Miercoles
    [12,31], #Jueves
    [18,21], #viernes
    [25,30], # sabado
    [1,5] # domingo
]

for temperatura in semana:
    temperatura_min = temperatura[0]
    temperatura_max = temperatura[1]
    acumulador_max += temperatura_max
    acumulador_min += temperatura_min  
    amplitud = temperatura[1] - temperatura[0]
    print(f"La temp max es: {temperatura_max}, la min es: {temperatura_min}")
    print(f"Amplitud del dia: {amplitud}")
    if amplitud > amplitud_maxima:
        amplitud_maxima = amplitud
        dia = semana.index(temperatura)
promedio_max = acumulador_max / len(semana)
promedio_min = acumulador_min / len(semana)
print(f"El minimo promedio es: {promedio_min:.3n}")
print(f"El máximo promedio es: {promedio_max:.3n}")
print(f"El día de mayor amplitud fue: {dias[dia]} con: {amplitud_maxima}°!")
print(dia)
#Tiene algunas inconsistencias con amplitud > amplitud máxima
