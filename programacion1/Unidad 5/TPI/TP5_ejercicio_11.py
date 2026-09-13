'''''11) Crear una lista con los nombres de 10 estudiantes.
● Solicitar al usuario que ingrese un nombre a buscar.
● Indicar si el nombre se encuentra en la lista.
● Mostrar la posición en la que aparece.
● Si no se encuentra, informar que no está en la lista'''

estudiantes = ["pancarcho","milaneso","salamino","ismael","ismaella","juanpan","tuntunsaur","franco","ariel","peppapig",]
print(estudiantes) #fines prácticos
nombre = input("Ingrese que estudiante quiere buscar:").strip()

if nombre in estudiantes:
    print(f"{nombre} está en la lista en la posición {estudiantes.index(nombre)}")
else:
    print("No existe ese alumno.")