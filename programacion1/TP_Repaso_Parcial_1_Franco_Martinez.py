'''Enunciado Una clínica desea administrar eficientemente las diferentes especialidades médicas que ofrece y la disponibilidad de cupos (espacios para citas) diarios para cada una. Se pide implementar un programa que utilice listas paralelas: una lista especialidades[] para almacenar los nombres de las especialidades (por ejemplo, "Cardiología", "Dermatología") y otra lista cupos[] para almacenar el número de cupos disponibles para cada especialidad en un día específico. Ambas listas deben compartir el mismo índice, de manera que el cupo en cupos[i] corresponda a la especialidad en especialidades[i]. El programa debe presentar un menú al usuario y utilizar un bucle while para permitirle realizar diferentes operaciones hasta que elija la opción "Salir".'''

especialidades = []
cupos = []


while True:

    # creacion del menú y ejecución del menú
    print(f"{30*'-'} \n Bienvenido usuario \n {30*'-'}")
    print("\n Menú. \n 1-Ingresar especialidad \n 2-Ingresar cupos disponibles \n 3-Mostrar Agenda \n 4-Consutar cupos de una especialidad \n 5-Listar especialidades sin cupo \n 6-Agregar especialidad \n 7-Actualizar cupos (reservar/cancelar) \n 8-Salir")

    opcion = input("Ingrese una opción: ")

    match opcion:
        case "1":
            cantidad = input("¿Cuántas especialidades desea ingresar?: ")

            while not cantidad.isdigit() or int(cantidad) <= 0:
                print("Error, Intente de nuevo.")
                cantidad = input("¿Cuántas especialidades desea ingresar?: ")

            cantidad = int(cantidad)
            especialidades = []
            cupos = []

            for puntero in range(cantidad):
                nueva_especialidad = input(f"Ingrese la especialidad {puntero + 1}: ")

                while nueva_especialidad == "" or nueva_especialidad in especialidades:
                    if nueva_especialidad == "":
                        print("Error, no puede estar vacío.")
                    else:
                        print("Error esa especialidad ya está cargada.")

                    nueva_especialidad = input(f"Ingrese la especialidad {puntero + 1}: ")

                especialidades.append(nueva_especialidad)
                cupos.append(0)
                print("Se añadió la especialidad.")

        case "2":
            if len(especialidades) == 0:
                print("No hay especialidades")
            else:
                print("Cargar cupos disponibles: ")

                for puntero in range(len(especialidades)):
                    cantidad_cupos = input(f"Ingrese cupos para {especialidades[puntero]}: ")

                    while not cantidad_cupos.isdigit():
                        print("Error, número inválido.")
                        cantidad_cupos = input(f"Ingrese cupos para {especialidades[puntero]}: ")

                    cupos[puntero] = int(cantidad_cupos)

                print("Se añadieron los cupos.")

        case "3":
            if len(especialidades) == 0:
                print("No se encontraron especialidades.")
            else:
                for puntero in range(len(especialidades)):
                    print(f"Especialidad: {especialidades[puntero]} "
                          f"Cupos: {cupos[puntero]}")

        case "4":
            print(especialidades)
            opcion_especialidad = input("Ingrese la especialidad a consultar: ")
            encontrada = False

            for puntero in range(len(especialidades)):
                if opcion_especialidad == especialidades[puntero]:
                    print(f"Especialidad: {especialidades[puntero]} "
                          f"Cupos: {cupos[puntero]}")
                    encontrada = True
                    break

            if encontrada == False:
                print("Error, no existe.")

        case "5":
            sin_cupos = False
            print("Especialidades sin cupos: ")

            for puntero in range(len(especialidades)):
                if cupos[puntero] == 0:
                    print(especialidades[puntero])
                    sin_cupos = True

            if sin_cupos == False:
                print("Hay cupos para todas las especialidades.")

        case "6":
            nueva_especialidad = input("Ingrese una nueva especialidad: ")

            while nueva_especialidad == "" or nueva_especialidad in especialidades:
                if nueva_especialidad == "":
                    print("Error, no ingresó nada.")
                else:
                    print(f"{nueva_especialidad} ya existe.")

                nueva_especialidad = input("Ingrese la nueva especialidad: ")

            nuevos_cupos = input("Ingrese los cupos iniciales: ")

            while not nuevos_cupos.isdigit():
                print("Error debe ser 0 o un número positivo.")
                nuevos_cupos = input("Ingrese los cupos iniciales: ")

            especialidades.append(nueva_especialidad)
            cupos.append(int(nuevos_cupos))

            print("Se agregó correctamente. ;D")

        case "7":
            print(especialidades)
            opcion_especialidad = input("Ingrese la especialidad: ")
            indice = -1

            for puntero in range(len(especialidades)):
                if opcion_especialidad == especialidades[puntero]:
                    indice = puntero
                    break

            if indice == -1:
                print("ERROR FATAL no existe")
            else:
                print(f"Cupos actuales: {cupos[indice]}")
                print("1-Reservar turno \n2-Cancelar turno")

                opcion_elegida = input("Seleccione una opcion: ")

                while opcion_elegida != "1" and opcion_elegida != "2":
                    print("Error debe elegir una opción válida.")
                    opcion_elegida = input("Seleccione una opcion: ")

                if opcion_elegida == "1":
                    if cupos[indice] > 0:
                        cupos[indice] = cupos[indice] - 1
                        print("Turno reservado")
                        print(f"Cupos restantes: {cupos[indice]}")
                    else:
                        print("No hay cupos disponibles. :C")

                else:
                    cupos[indice] = cupos[indice] + 1
                    print("Se canceló el turno")
                    print(f"Cupos disponibles: {cupos[indice]}")

        case "8":
            print("Saliendo...")
            break

        case _:
            print("Error mortal, elija entre 1 y 8.")