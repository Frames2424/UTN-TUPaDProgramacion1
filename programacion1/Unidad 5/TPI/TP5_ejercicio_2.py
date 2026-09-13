'''Pedir al usuario que cargue 5 productos en una lista.
● Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
● Preguntar al usuario qué producto desea eliminar y actualizar la lista.'''
#Iniciar carga de productos
print(f"{"#"*25}")
print("Bienvenido usuario")
print(f"{"#"*25}")
productos = []
for i in range(5):
    producto_carga = input("Ingrese un producto: ")
    while not producto_carga.isalpha() or producto_carga == "":
        print("Error reintente.")
        producto_carga = input("Ingrese un producto nuevamente: ")
    productos.append(producto_carga)
    print(f"Usted ingresó el producto {i}: {producto_carga}")
productos_ordenados = sorted(productos)
for i in range(len(productos_ordenados)):
    print(f"Producto {i}: {productos_ordenados[i]}")

opcion = input("¿Desea eliminar [1] o actualizar[2] un producto?: ")
while not opcion.isnumeric():
    print("Error, ingrese una opción válida. 1 o 2.")
    opcion = input("Opciones:\nEliminar [1]\nActualizar[2]\n Opción: ")

match opcion:
    case "1":
        print("Eliminar producto")
        opcion_eliminar = input("¿Qué producto desea eliminar?: ")
        while not opcion_eliminar.isalpha():
            print("Error ingrese un dato válido.")
            opcion_eliminar = input("Reintente.\n¿Qué producto desea eliminar?: ")
        if opcion_eliminar in productos_ordenados:
            print(f"Ustéd eliminó: {opcion_eliminar}")
            productos_ordenados.remove(opcion_eliminar)
            for i in range(len(productos_ordenados)):
                print(f"Producto {i}: {productos_ordenados[i]}")
                
        else:
            print("Error no existe.")
    case "2":
        print("Actualizar producto")
        print(f"Los productos son: {productos_ordenados}")
        opcion_actualizar = input("¿Qué producto desea actualizar?\n")
        while not opcion_actualizar.isalpha():
            print("Error, ingresó un dato inválido.")
            opcion_actualizar = input("¿Qué producto desea actualizar?\n")
        if opcion_actualizar in productos_ordenados:
            indice = productos_ordenados.index(opcion_actualizar)
            print(f"Usted actualizará el producto {opcion_actualizar}.")
            producto_nuevo = input("¿Que producto nuevo desea?")
            while not producto_nuevo.isalpha():
                print("Error, introduzca un producto válido.")
                producto_nuevo = input("¿Que producto nuevo desea?")           
            productos_ordenados[indice] = producto_nuevo
            print(f"{"#"*25}")
            for i in range(len(productos_ordenados)):
                print(f"Producto {i}: {productos_ordenados[i]}")
            print(f"{"#"*25}")