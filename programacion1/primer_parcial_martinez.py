'''''Funcionalidades del Menú
El programa debe presentar un menú interactivo persistente con las siguientes opciones:
1. Carga Inicial de Herramientas: registrar los nombres de las herramientas que se pondrán a la venta.
Se debe preguntar al usuario la cantidad de herramientas a cargar y se debe usar una estructura
pertinente. En caso de nombre vacío o duplicado se debe seguir pidiendo hasta que sea correcto,
respetando la cantidad de herramientas que el usuario indicó antes de la carga.

2. Carga de Existencias: ingresar la cantidad de unidades para cada herramienta registrada
previamente, respetando el orden de ingreso. Cuando el usuario ingresa existencias, el sistema debe
mostrar por pantalla el nombre de la herramienta.

3. Visualización de Inventario: mostrar el listado completo de herramientas junto a su stock actual.

4. Consulta de Stock: buscar una herramienta por su nombre y mostrar cuántas unidades hay
disponibles.

5. Reporte de Agotados: listar únicamente aquellos productos cuyo stock sea igual a cero.

6. Alta de Nuevo Producto: permitir agregar solo una nueva herramienta al final de las listas con su
stock inicial. En caso de nombre vacío, nombre duplicado o valor de existencia negativo se debe
volver al menú principal mostrando por pantalla el motivo.

7. Actualización de Stock (Venta/Ingreso):

a) Venta: disminuir el stock tras validar que hay unidades suficientes.
b) Ingreso: aumentar el stock por reposición de mercadería.

8. Salir: finalizar la ejecución del sistema.'''

# herramientas = ["test","herramienta2","triplete","agotadooo","martillo2bolas"] #testeo
# stock = [67,0,5,7,0] #testeo

herramientas = []
stock = []

menu = True
#menu 
while menu == True:
    print()
    print("*"*30)
    print("Bienvenido usuario")
    print("*"*30)
    print("1.Carga inicial de herramientas.")
    print("2.Carga de existencias.")
    print("3.Visualización de inventario.")
    print("4.Consulta de stock.")
    print("5.Reporte de agotados.")
    print("6.Alta de nuevo producto.")
    print("7.Actualización de Stock(Venta/ingreso).")
    print("8.Salir del sistema.")

    #opcion del usuario en el menu:
    opcion_menu = input("Ingrese el número de lo que desea hacer: ")
    #Validación de opcion menu:
    while not opcion_menu.isdigit():
        print("Error, no ingresó un dato válido.")
        opcion_menu = input("Ingrese el número de lo que desea hacer: ")


    match opcion_menu:
        #Carga inicial de herramientas:
        case "1":
            print("### Carga inicial de herramientas ###")
            #Validación de cuántas herramientas ingresar:

            cantidad_herramientas = input("Ingrese la cantidad de herramientas que desea cargar: ")
            while not cantidad_herramientas.isdigit():
                print("Error, ingrese un número válido.")
                cantidad_herramientas = input("Ingrese la cantidad de herramientas que desea cargar: ")

                #Ciclo for de cantidad de herramientas a cargar 
            for i in range(int(cantidad_herramientas)):
                carga_herramientas = input("Ingrese la herramienta que desea cargar: ")
                while not carga_herramientas.isalpha():
                    print("Error ustéd no ingresó una herramienta, reintente.")
                    carga_herramientas = input("Ingrese la herramienta que desea cargar: ")   

                if carga_herramientas in herramientas:
                    print("Error esa herramienta ya se encuentra registrada.")
                    print("Reintente.")
                else:
                    herramientas.append(carga_herramientas)
                    print(f"Usted ingresó {carga_herramientas}")
                    print(f"El total de sus herramientas es: {herramientas}")

        #Ingreso de existencias por cada herramienta
        case "2":
            if len(herramientas) == 0:
                print("Error, aún no hay herramientas cargadas, intente cargar herramientas primero.")
            else:

                print("### Carga de existencias ###")
                for indice in range(len(herramientas)):
                    print(f"Cargaremos la cantidad de stock de {herramientas[indice]}")
                    existencia_herramienta = input(f"Ingrese la cantidad de existencia para:\n {herramientas[indice]} : ")
                    while not existencia_herramienta.isdigit():
                        print("Error no ingresó un número válido o no ingresó nada. Reintente.")
                        existencia_herramienta = input(f"Ingrese la cantidad de existencia para:\n {herramientas[indice]} : ")
                    stock.append(existencia_herramienta)
                    print(f"Se añadió:\n {stock[indice]} unidades: {herramientas[indice]}")

        #3. Visualización de Inventario: mostrar el listado completo de herramientas junto a su stock actual.
        case "3":
            if len(herramientas) != len(stock):
                print("Error, falta sincronización de herramientas y stock.")
            else: 
                print("#"*5, "Visualización de Inventario","#"*5 )
                print(f"El inventario actual es:\n")
                for indice in range(len(herramientas)):
                    print(f"Herramienta: {herramientas[indice]}",end="")
                    print(f" | Stock: {stock[indice]}")


        #4. Consulta de Stock: buscar una herramienta por su nombre y mostrar cuántas unidades hay disponibles.
        case "4":
            print("### Buscador de stock por nombre ###")
            nombre_herramienta = input("Ingrese el nombre de la herramienta para consultar su stock: ")
            while not nombre_herramienta.isalpha():
                print("Error, no ingresó un nombre válido. Reintente")
                nombre_herramienta = input("Ingrese el nombre de la herramienta para consultar su stock: ")
            if nombre_herramienta in herramientas: 
                indice_stock = herramientas.index(nombre_herramienta)
                print(f"Herramienta: {nombre_herramienta} | Stock: | {stock[indice_stock]} |")
            else:
                print(f"{nombre_herramienta} no está registrada.")


            #5. Reporte de Agotados: listar únicamente aquellos productos cuyo stock sea igual a cero.  
        case "5":
        
            print("###### REPORTE DE AGOTADOS ######")
            agotados = []
            contador_indice = 0
            for cantidad_stock in stock:
                if cantidad_stock == 0:
                    contador_indice += 1
                    agotados.append(herramientas[contador_indice])
                    print(agotados)
            if len(agotados) == 0:
                print("No hay productos agotados.")

    #6. Alta de Nuevo Producto: permitir agregar solo una nueva herramienta al final de las listas con su
    # stock inicial. En caso de nombre vacío, nombre duplicado o valor de existencia negativo se debe volver al menú principal mostrando por pantalla el motivo.

        case "6":
            print("###### Alta de nuevo producto y su stock #######")

            #Validación herramienta
            nueva_herramienta = input("Ingrese una nueva herramienta: ")
            while not nueva_herramienta.isalpha() or nueva_herramienta in herramientas:
                print("Error, ingresó un texto no válido o la herramienta ya está registrada. Reintente.")
                nueva_herramienta = input("Ingrese una nueva herramienta: ")

            #Validacion stock
            stock_nueva_herramienta = input(f"Ingrese el stock de la nueva herramienta {nueva_herramienta}: ")
            while not stock_nueva_herramienta.isdigit():
                print("Error, no ingresó un número de stock válido. Reintente.")
                stock_nueva_herramienta = input(f"Ingrese el stock de la nueva herramienta {nueva_herramienta}: ")
            print("Ustéd registrará")
            print(f"La herramienta: {nueva_herramienta} stock | {stock_nueva_herramienta}")
            herramientas.append(nueva_herramienta)
            stock.append(stock_nueva_herramienta)
            print(f"herramientas: {herramientas} y stock {stock}")


        case "7":

            print("###### Actualización de Stock(Venta/ingreso ######")
            opcion_actualizar = input("Seleccionar opción:\n [1] Vender\n [2]Ingresar:\n")
            while not opcion_actualizar.isdigit():
                print("Error, Ingrese 1 o 2.")
                opcion_actualizar = input("Seleccionar opción:\n [1] Vender\n [2]Ingresar:\n")
            match opcion_actualizar:
                case "1":
                    print("###### Vender ######")
                    print(f"Sus herramientas disponibles:\n {herramientas}")
                    venta = input("¿Qué herramienta desea vender?\n")
                    while not venta.isalpha() or venta not in herramientas:
                        print("Ingresó un dato erroneo o no ingresó una herramienta disponible. Reintente.")
                        venta = input("¿Qué herramienta desea vender?\n")

                        #Incompleto
                    indice_producto = herramientas.index(venta)
                    print(f"Usted vendió {venta}, el stock disminuyó a ")
                    # if stock[indice_producto] == 0:
                    #     print(f"En total queda: {stock[indice_producto]}")
                    # else:
                    #     stock[indice_producto] -= 1
                    disminucion_stock = stock[indice_stock] - 1
                    print(f"En total queda: {disminucion_stock}")
                    
                case "2":
                    acumulador = 0
                    print("###### Agregar stock (reposición) ######")
                    for herramienta in range(len(herramientas)):
                        print(f"La herramienta: {herramientas[herramienta]} | stock | {stock[herramienta]}")

                    print("¿Cuál herramienta desea reponer?")
                    reposicion = input("Ingrese la herramienta que desea reponer: ")
                    while not reposicion.isalpha or reposicion not in herramientas:
                        print("Error ustéd ingresó un dato erroneo o una herramienta que no existe.")
                        reposicion = input("Ingrese la herramienta que desea reponer: ")
                    for reposicion in range(len(herramientas)):
                        acumulador += 1
                        if reposicion == herramientas[reposicion]:
                            print(reposicion)
                            print("llegamoso aca")

        case "8":
            print("Saliendo...")
            menu = False