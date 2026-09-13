'''''8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
● Mostrar el promedio de cada estudiante.
● Mostrar el promedio de cada materia'''

estudiantes = [
    [4,7,10], #estudiante 1 
    [8,9,10], #estudiante 2
    [4,1,7], #estudiante 3
    [7,8,9], #estudiante 4
    [10,10,10], #estudiante 5
]
#col 1 matematicas
#col 2 lengua
#col 3 geografia

#Acumulador notas
contador = 0
for materias in estudiantes:
    acumulador = 0
    for notas in materias:
        acumulador += notas
    contador += 1
    print(f"El promedio del estudiante {contador} es: {acumulador / 3}")

#se podría realizar todo el ejercicio en el recorrido de las líneas de arriba pero voy hacerlo de nuevo para practicar

    acumulador_matematicas = 0
    acumulador_lengua = 0
    acumulador_geografia = 0
for notas in estudiantes:
    acumulador_matematicas += notas[0]
    acumulador_lengua += notas[1]
    acumulador_geografia += notas[2]
print("El promedio de matemáticas es:", acumulador_matematicas/5)
print("El promedio de lengua es:", acumulador_lengua/5)
print("El promedio de geografía es:", acumulador_geografia/5)