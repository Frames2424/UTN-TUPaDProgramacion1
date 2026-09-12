''''5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
● Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
● Mostrar la lista final actualizada.
'''

alumnos = ["jorge","Juan","Jeremi","Luca","CarloMagno","Franco","ElPequeñoj"]

opcion = input("\nQuiere ingresar un estudiante o eliminar:\n [1]Eliminar \n [2]Actualizar \n Opción: ")
match opcion:
    case "1":
        for i in range(len(alumnos)):
            print(alumnos[i], end="\n")
        eliminar_alumno = input("\n¿Qué alumno desea exterminar?: ")
        while not eliminar_alumno.isalpha():
            print("Error, reintente.")
            eliminar_alumno = input("¿Qué alumno desea exterminar?")
        if eliminar_alumno in alumnos:
            alumnos.remove(eliminar_alumno) #elimina por valor ejemplo "franco" --> no por índice, índice no lo está usando para nada... 
            print(alumnos)
    case "2":
        agregar_alumno = input("Escriba del nombre del alumno que desea agregar: ")
        while not agregar_alumno.isalpha():
            print("Error, reintente.")
            agregar_alumno = input("¿Qué alumno desea agregar?")
        alumnos.append(agregar_alumno)
        print(f"Agregó a {agregar_alumno}\nLos alumnos son:")
        for i in range(len(alumnos)):
            print(alumnos[i], end=" ")