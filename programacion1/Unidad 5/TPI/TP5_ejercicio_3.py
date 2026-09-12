'''3) Generar una lista con 15 números enteros al azar entre 1 y 100.
● Crear una lista con los pares y otra con los impares.
● Mostrar cuántos números tiene cada lista.'''
import random
todos_los_numeros = []
numeros_par = []
numeros_impar = []
for i in range(15):
    numero_random = random.randint(1,100)
    todos_los_numeros.append(numero_random)
    if numero_random % 2 == 0:
        print(f"Este número es par: {numero_random}")
        numeros_par.append(numero_random)
    else:
        print(f"Este número es impar: {numero_random}")
        numeros_impar.append(numero_random)
print("La lista de 15 números random es:")
for i in range(len(todos_los_numeros)):
    print(f" {todos_los_numeros[i]}", end=" ")
print(f"\nLa lista de números pares contiene {len(numeros_par)}")
print(f"La lista de números impares contiene {len(numeros_impar)}")