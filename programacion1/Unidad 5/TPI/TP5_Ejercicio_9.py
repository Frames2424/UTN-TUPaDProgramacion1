'''''9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
● Inicializarlo con guiones "-" representando casillas vacías.
● Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
● Mostrar el tablero después de cada jugada'''
tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]
turno_jugador = 0
# terminador = 0
print(tablero[0])
print(tablero[1])
print(tablero[2])


while True:
    if turno_jugador == 0:
        print("Es el turno del jugador (X)")
        puntero_fila = int(input("En cuál fila deseas marcar: "))
        puntero_col = int(input("En cuál columna deseas marcar: "))
        tablero[puntero_fila - 1][puntero_col - 1] = "x"
        print(tablero[0])
        print(tablero[1])
        print(tablero[2])
        turno_jugador = 1
        # terminador += 1
    else:
        print("Es el turno del jugador (O)")
        puntero_fila = int(input("En cuál fila deseas marcar: "))
        puntero_col = int(input("En cuál columna deseas marcar: "))
        tablero[puntero_fila - 1][puntero_col - 1] = "O"
        print(tablero[0])
        print(tablero[1])
        print(tablero[2])
        turno_jugador = 0
