''''12) Pedir al usuario que ingrese 8 números enteros y almacenarlos en una lista.
● Mostrar la lista original.
● Mostrar la lista ordenada de menor a mayor.
● Mostrar la lista ordenada de mayor a menor.
● Investigar el uso de sorted() y del parámetro reverse.
'''

lista = []
#Carga de nros
for num in range(8):
    numero = int(input("Ingrese un número entero: "))
    lista.append(numero)
print(f"La lista original es: {lista}")
lista_ordenada = sorted(lista)
print(f"La lista ordenada es: {lista_ordenada}")
lista_reversed = sorted(lista_ordenada, reverse=True)
print(f"La lista invertida es: {lista_reversed}")