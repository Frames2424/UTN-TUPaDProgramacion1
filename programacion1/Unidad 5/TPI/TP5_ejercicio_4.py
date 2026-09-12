''''Dada la lista datos = [1,3,5,3,7,1,9,5,3] crear una lista nueva sin los repetidos'''
sin_repetidos = []
datos = [1,3,5,3,7,1,9,5,3]

for numero in datos:
    if not numero in sin_repetidos:
        sin_repetidos.append(numero)
print("Forma linda coqueta y moderna de mostrar una lista:")
for i in range(len(sin_repetidos)):
    print(f" {sin_repetidos[i]} ", end="")