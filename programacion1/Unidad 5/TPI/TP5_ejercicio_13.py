'''''13) Dada la siguiente lista de puntajes de un videojuego:
puntajes = [450, 1200, 875, 990, 300, 1500, 640]
● Mostrar el puntaje más alto y el más bajo.
● Mostrar la lista ordenada de mayor a menor (ranking).
● Indicar en qué posición del ranking se encuentra el puntaje 990'''

puntajes = [450, 1200, 875, 990, 300, 1500, 640]
puntos_maximos = 0
for puntos in puntajes:
    if puntos >= puntos_maximos:
        puntos_maximos = puntos
print("El puntaje máximo es: ",puntos_maximos)
print(f"990 está en la posición:{puntajes.index(990)}")
puntajes.sort()
print(f"Lista invertida",puntajes)