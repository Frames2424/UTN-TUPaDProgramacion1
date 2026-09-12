''''Ejercicio 4 La boveda, de nuevo.'''
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ''

forzar_seguidas = 0
bloqueado = False


print('--- Escape Room: La Bóveda ---')

nombre_agente = input('Ingrese el nombre del agente: ').strip().capitalize()

while nombre_agente == '' or not nombre_agente.isalpha():
    print('El nombre solo puede contener letras.')
    nombre_agente = input('Ingrese el nombre del agente: ').strip().capitalize()


while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and bloqueado == False:

    print('\n--- Estado actual ---')
    print(f'Agente: {nombre_agente}')
    print(f'Energía: {energia}')
    print(f'Tiempo: {tiempo}')
    print(f'Cerraduras abiertas: {cerraduras_abiertas}/3')

    if alarma == True:
        print('Alarma: ACTIVADA')
    else:
        print('Alarma: desactivada')

    print('\n--- Acciones ---')
    print('1. Forzar cerradura')
    print('2. Hackear panel')
    print('3. Descansar')

    opcion = input('Elija una opción: ').strip()

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        if not opcion.isdigit():
            print('Error: debe ingresar un número.')
        else:
            print('Error: opción fuera de rango.')

        opcion = input('Elija una opción: ').strip()


    match opcion:

        case '1':
            energia -= 20
            tiempo -= 2
            forzar_seguidas += 1

            print('\nIntentando forzar la cerradura...')

            if forzar_seguidas == 3:
                alarma = True
                print('Forzaste la cerradura 3 veces seguidas.')
                print('La cerradura se trabó y se activó la alarma.')
                print('No se abrió ninguna cerradura.')

            else:
                if energia < 40:
                    print('Tu energía está por debajo de 40.')
                    print('Hay riesgo de activar la alarma.')

                    numero = input('Ingrese un número del 1 al 3: ').strip()

                    while not numero.isdigit() or int(numero) < 1 or int(numero) > 3:
                        print('Debe ingresar un número entre 1 y 3.')
                        numero = input('Ingrese un número del 1 al 3: ').strip()

                    if numero == '3':
                        alarma = True
                        print('¡Se activó la alarma!')

                if alarma == False:
                    cerraduras_abiertas += 1
                    print('¡Cerradura abierta correctamente!')
                else:
                    print('No se pudo abrir la cerradura debido a la alarma.')


        case '2':
            energia -= 10
            tiempo -= 3
            forzar_seguidas = 0

            print('\nHackeando panel...')

            for i in range(4):
                codigo_parcial += 'A'
                print(f'Paso {i + 1}/4 - Código parcial: {codigo_parcial}')

            if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print('El código alcanzó la longitud necesaria.')
                print('¡Se abrió automáticamente una cerradura!')
            else:
                print('Hackeo realizado, pero todavía no alcanza para abrir una cerradura.')


        case '3':
            tiempo -= 1
            forzar_seguidas = 0

            energia += 15

            if energia > 100:
                energia = 100

            print('\nDescansaste y recuperaste energía.')

            if alarma == True:
                energia -= 10
                print('La alarma está activa. Perdiste 10 puntos de energía extra.')

            print(f'Energía actual: {energia}')


    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueado = True
        print('\nLa alarma está activa y queda muy poco tiempo.')
        print('El sistema de la bóveda se bloqueó.')


print('\n--- Fin del juego ---')

if cerraduras_abiertas == 3:
    print(f'¡VICTORIA! {nombre_agente} abrió las 3 cerraduras.')

elif bloqueado == True:
    print('DERROTA. La bóveda se bloqueó por la alarma.')

elif energia <= 0:
    print('DERROTA. Te quedaste sin energía.')

elif tiempo <= 0:
    print('DERROTA. Te quedaste sin tiempo.')
