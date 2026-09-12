'''Ejercicio 1 Caja de kiosco'''

print('--- Caja del Kiosco ---')

nombre = input('Ingrese el nombre del cliente: ').strip().capitalize()

while nombre == '' or not nombre.isalpha():
    if nombre == '':
        print('El nombre no puede estar vacío.')
    else:
        print('El nombre solo puede contener letras.')
    nombre = input('Ingrese el nombre del cliente: ').strip().capitalize()


cantidad_str = input('Ingrese la cantidad de productos a comprar: ').strip()

while not cantidad_str.isdigit() or cantidad_str == '0':
    if not cantidad_str.isdigit():
        print('La cantidad debe ser un número entero positivo.')
    else:
        print('La cantidad debe ser mayor a 0.')
    cantidad_str = input('Ingrese la cantidad de productos a comprar: ').strip()

cantidad = int(cantidad_str)


total_sin_descuento = 0
total_con_descuento = 0.0


for i in range(cantidad):
    print(f'\n--- Producto {i + 1} ---')

    precio_str = input('Ingrese el precio del producto: ').strip()

    while not precio_str.isdigit():
        print('El precio debe ser un número entero.')
        precio_str = input('Ingrese el precio del producto: ').strip()

    precio = int(precio_str)

    descuento = input('¿Tiene descuento? S/N: ').strip().upper()

    while descuento != 'S' and descuento != 'N':
        print('Debe ingresar S o N.')
        descuento = input('¿Tiene descuento? S/N: ').strip().upper()

    total_sin_descuento += precio

    if descuento == 'S':
        precio_con_descuento = precio * 0.90
        total_con_descuento += precio_con_descuento
    else:
        total_con_descuento += precio


ahorro = total_sin_descuento - total_con_descuento
promedio = float(total_con_descuento) / cantidad


print('\n--- Resumen de la compra ---')
print(f'Cliente: {nombre}')
print(f'Total sin descuentos: ${total_sin_descuento}')
print(f'Total con descuentos: ${total_con_descuento:.2f}')
print(f'Ahorro total: ${ahorro:.2f}')
print(f'Promedio por producto: ${promedio:.2f}')