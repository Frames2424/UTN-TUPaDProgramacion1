"""'10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
• Mostrar el total vendido por cada producto.
• Mostrar el día con mayores ventas totales.
• Indicar cuál fue el producto más vendido en la semana."""

# Una anidada de 4x7, el 4 son las filas y el 7 las columnas.
ventas = [
    [10, 233, 15, 0, 3, 21, 28],  # producto 1
    [0, 2, 3, 4, 25, 72, 34],  # producto 2
    [2, 34, 22, 19, 23, 45, 11],  # producto 3
    [10, 9, 0, 23, 44, 83, 100],  # producto 4
]

producto_mas_vendido = 0
venta_max = 0
for i in range(len(ventas)):
    suma_venta = sum(ventas[i])
    print(
        f"El total de producto {i+1} vendidos es: {sum(ventas[i])}"
    )  # acá podría imprimir suma_ventas pero lo puse así para practicar

    if suma_venta > venta_max:
        venta_max = suma_venta
        producto_mas_vendido = i
print(f"EL producto más vendido es: {producto_mas_vendido + 1}")

# Dia de mayor venta total:
mayor_venta_dia = 0
dia_ganador = 0

# Recorremos los 7 días (columnas)
for j in range(7):
    suma_dia = 0
    # Por cada día, sumamos lo que vendió cada uno de los 4 productos
    for i in range(4):
        suma_dia += ventas[i][j]

    print(f"Total día {j+1}: {suma_dia}")  # Opcional, para ver los totales

    if suma_dia > mayor_venta_dia:
        mayor_venta_dia = suma_dia
        dia_ganador = j + 1
print(
    f"\nEl día con mayores ventas fue el día {dia_ganador} con un total de {mayor_venta_dia}"
)
