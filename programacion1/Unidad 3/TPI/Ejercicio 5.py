print('--- BIENVENIDO A LA ARENA ---')

nombre = input('Nombre del Gladiador: ').strip().capitalize()

while nombre == '' or not nombre.isalpha():
    print('Error: Solo se permiten letras.')
    nombre = input('Nombre del Gladiador: ').strip().capitalize()


vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_pesado = 15
danio_enemigo = 12
turno_gladiador = True
juego_activo = True


print('\n=== INICIO DEL COMBATE ===')


while vida_jugador > 0 and vida_enemigo > 0 and juego_activo == True:

    if turno_gladiador == True:

        print(f'\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}')

        print('\nElige acción:')
        print('1. Ataque Pesado')
        print('2. Ráfaga Veloz')
        print('3. Curar')

        opcion = input('Opción: ').strip()

        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
            if not opcion.isdigit():
                print('Error: Ingrese un número válido.')
            else:
                print('Error: La opción debe ser 1, 2 o 3.')

            opcion = input('Opción: ').strip()


        match opcion:

            case '1':
                danio_final = float(danio_pesado)

                if vida_enemigo < 20:
                    danio_final = danio_pesado * 1.5
                    print('¡Golpe Crítico!')

                vida_enemigo -= danio_final

                print(f'¡Atacaste al enemigo por {danio_final} puntos de daño!')


            case '2':
                print('>> ¡Inicias una ráfaga de golpes!')

                for i in range(3):
                    vida_enemigo -= 5
                    print('> Golpe conectado por 5 de daño')


            case '3':
                if pociones > 0:
                    vida_jugador += 30
                    pociones -= 1

                    print('Usaste una poción.')
                    print('Recuperaste 30 HP.')
                    print(f'Pociones restantes: {pociones}')

                else:
                    print('¡No quedan pociones!')


        turno_gladiador = False


    if turno_gladiador == False and vida_enemigo > 0:

        vida_jugador -= danio_enemigo

        print(f'¡El enemigo te atacó por {danio_enemigo} puntos de daño!')

        turno_gladiador = True

        if vida_jugador > 0:
            print('\n=== NUEVO TURNO ===')


print('\n=== FIN DEL COMBATE ===')

if vida_jugador > 0:
    print(f'GENIO! {nombre} ha ganado la batalla.')

else:
    print('MUELTO')