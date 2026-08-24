"""''Punto de Venta (Fast Food) Creen un programa para gestionar los pedidos de un local de comida rápida. El programa debe tener un menú que le permita al cajero ir sumando productos a la cuenta de un cliente.
Menú principal: 1.
Agregar Hamburguesa ($4500)
2. Agregar Papas Fritas ($2000)
3. Agregar Bebida ($1500)
4. Pagar el pedido (Cierra el ticket)
5. Cancelar pedido y salir
Requisitos: • Cada vez que se elige la opción 1, 2 o 3, se debe sumar el precio al total y avisar por pantalla ("Hamburguesa agregada. Total actual: $..."). • Si se elige Pagar (Opción 4), el programa debe mostrar el total a pagar y pedirle al cajero que ingrese con cuánto efectivo paga el cliente.
• ¡Atención! Si el efectivo ingresado es menor al total, el programa debe usar un bucle while para seguir pidiendo dinero hasta que alcance o supere el total. Una vez que alcanza, debe mostrar el cambio (vuelto) a devolver al cliente, reiniciar el total a $0 y volver al menú principal para el siguiente cliente.
• La opción 5 finaliza el programa por completo."""

total = 0
cancelar = True
hamburguesa = 0
papaFritas = 0
bebida = 0
fondosSuficientes = True

while cancelar:
    print("#########################")
    print(
        "  ###  COMIDA EL PEPE  ###  \n 1- Agregar hamburguesa ($4500) \n 2- Agregar papas fritas ($2000) \n 3- Agregar bedida ($1500) \n 4- Pagar el pedido (cerrar el ticket) \n 5- Cancelar pedido y salir"
    )
    opcion = input("¿Qué opción desea: \n")
    while not opcion.isdigit():
        opcion = input("¿Qué opción desea: \n")
    match opcion:
        case "1":
            print("Agregar hamburguesa $4500")
            total += 4500
            hamburguesa = hamburguesa + 1
            print(f"Ustéd agregó Hamburguesa de $4500 \n total de hamburguesas: {hamburguesa}")
            print(f"Total del pedido ${total}")

        case "2":
            print("Agregar papa fritas $2000")
            total += 2000
            papaFritas = papaFritas + 1
            print(f"Ustéd agregó papa fritas de $2000 \n total de papa fritas: {papaFritas}")
            print(f"Total del pedido ${total}")

        case "3":
            print("Agregar bebida $1500")
            total += 2000
            bebida = bebida + 1
            print(f"Ustéd agregó bebida de $1500 \n total de bebida: {bebida}")
            print(f"Total del pedido ${total}")

        case "4":
            print("#########################")
            print("Cerrar el pedido")
            print(f"Ticket cerrado\n ### Resumen ### \n Total de hamburguesas {hamburguesa} ${hamburguesa * 4500} \n Total de papa fritas {papaFritas} ${papaFritas * 2000} \n Total de bebidas {bebida} ${bebida * 1500}")
            print(f"TOTAL: {total}")

            pago = int(input("¿Con cuánto desea pagar?\n Deseo pagar con: $"))
            while pago < total:
                print("No alcanza")
                agregarDinero = int(input("¿Cuánto dinero desea sumar? \n Deseo sumar: $"))
                pago += agregarDinero
            fondosSuficientes = False
            cambio = pago - total
            print(f"Ustéd pagará ${total} con ${pago} \n Su vuelto es: ${cambio}")
            print("######################### \n")

            total = 0
            hamburguesa = 0
            bebida = 0
            papaFritas = 0
          

        case "5":
            print("Pedido Cancelado, saliendo...")
            cancelar = False