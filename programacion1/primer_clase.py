"""El Cajero Automático Desarrollen un simulador de cajero automático. El usuario comenzará con un saldo inicial de $50,000. El programa debe mostrar un menú que se repita hasta que el usuario decida salir:
1. Consultar saldo.
2. Ingresar dinero.
3. Retirar dinero.
4. Salir.
Reglas de negocio:
• No se pueden ingresar cantidades negativas. • No se puede retirar más dinero del que hay en el saldo, ni cantidades negativas. Si el usuario intenta retirar de más, mostrar un mensaje de "Fondos insuficientes".
• Usar match-case para manejar las opciones del menú."""

saldo = 50000
saliendo = True
while saliendo:
    print(
        "### Cajero automático ### \n 1. Consultar saldo. \n 2. Ingresar dinero. \n 3. Retirar dinero. \n 4. Salir. \n"
    )
    opcion = input("Que opción desea elegir: ")
    match opcion:
        case "1":
            print("Consultar saldo.")
            print(f"Su saldo es {saldo}")
        case "2":
            print("Ingresar dinero")
            ingresoDinero = input("¿Cuánto dinero deseas ingresar? \n")
            while not ingresoDinero.isdigit():
                ingresoDinero = input("¿Cuánto dinero deseas ingresar? \n")
            ingresoDinero = float(ingresoDinero)
            if ingresoDinero > 0:
                saldo = ingresoDinero + saldo
            print(f"Usted ingresó {ingresoDinero} y ahora su saldo es: \n {saldo}")
        case "3":
            print("Retirar dinero")
            extraerDinero = input("¿Cuánto dinero desea extraer? \n")
            while not extraerDinero.isdigit():
                extraerDinero = input("¿Cuánto dinero desea extraer? \n")
            extraerDinero = float(extraerDinero)
            if saldo > 0 and saldo < extraerDinero:
                print("Fondos Insuficientes.")
            else:
                print(
                    f"Usted extrajo {extraerDinero} y tu saldo actual es {saldo - extraerDinero}"
                )
                saldo = saldo - extraerDinero
        case "4":
            print("Saliendo...")
            saliendo = False
