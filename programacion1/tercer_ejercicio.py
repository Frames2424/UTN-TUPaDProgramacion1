while True:
    registro = input("Registre la temperatura ('FIN' para salir): ").strip()
    if registro == "FIN":
        print("Cerrando registro del horno...")
        break
    es_valido = True

    if registro == "" or registro == ".":
        es_valido = False
    elif registro.count(".") > 1:
        es_valido = False
    else:
        sin_punto = registro.replace(".", "", 1)
        if not sin_punto.isdigit():
            es_valido = False
    if not es_valido:
        print("Error: Ingrese un valor numérico válido.")
        continue
    temperatura = float(registro)
    print(f"Temperatura registrada: {temperatura}°C")
    if temperatura < 100.0 or temperatura > 500.0:
        print("¡ADVERTENCIA! Temperatura fuera de rango")