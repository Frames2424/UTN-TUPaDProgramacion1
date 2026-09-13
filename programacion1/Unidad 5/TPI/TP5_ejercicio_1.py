'''Práctico 5: Listas'''
'''1) Crear una lista con las notas de 10 estudiantes.
● Mostrar la lista completa.
● Calcular y mostrar el promedio.
● Indicar la nota más alta y la más baja'''

notas = [8,4,8,10,9,-1,10,8,9,3]
nota_min = notas[0]
nota_max = notas[0]
acumulador = 0
for i in range(len(notas)):
    if notas[i] < nota_min:
        nota_min = notas[i]
    if notas[i] > nota_max:
        nota_max = notas[i]
    acumulador += notas[i]

promedio = acumulador / len(notas)
print(f"El promedio de notas es {promedio}")
print("Las notas son:", end="")
for i in range(len(notas)):
    print(f" {notas[i]}", end=" ")
print(f"\nLa nota más alta es {nota_max} y la más baja es {nota_min}")
