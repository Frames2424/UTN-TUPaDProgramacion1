'''' Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha
(el último pasa a ser el primero).'''
#así sería con una lista nueva y rotando TODOS los números, es decir, haciendolá inversa.
lista = [1,2,35,4,5,6,7]
lista_rotada = []
for i in range(len(lista)):
    lista_rotada.insert(0,lista[i])
print(lista_rotada)

#Ahora sin otra lista, solo un auxiliar y cumpliendo la consigna.
lista = [1,2,35,4,5,6,7]
auxiliar = lista[0]
lista[0] = lista[-1]
lista[-1] = auxiliar
print(lista)