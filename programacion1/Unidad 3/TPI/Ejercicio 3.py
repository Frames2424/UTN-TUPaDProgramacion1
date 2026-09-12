lunes1 = ''
lunes2 = ''
lunes3 = ''
lunes4 = ''

martes1 = ''
martes2 = ''
martes3 = ''


operador = input('Ingrese el nombre del operador: ').strip().capitalize()

while operador == '' or not operador.isalpha():
    print('El nombre del operador solo puede contener letras.')
    operador = input('Ingrese el nombre del operador: ').strip().capitalize()


opcion = ''

while opcion != '5':
    print('\n--- Agenda de Turnos ---')
    print(f'Operador: {operador}')
    print('1. Reservar turno')
    print('2. Cancelar turno')
    print('3. Ver agenda del día')
    print('4. Ver resumen general')
    print('5. Cerrar sistema')

    opcion = input('Elija una opción: ').strip()

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        if not opcion.isdigit():
            print('Error: debe ingresar un número.')
        else:
            print('Error: opción fuera de rango.')

        opcion = input('Elija una opción: ').strip()


    match opcion:

        case '1':
            print('\n--- Reservar turno ---')
            print('1. Lunes')
            print('2. Martes')

            dia = input('Seleccione el día: ').strip()

            while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
                print('Debe ingresar 1 para Lunes o 2 para Martes.')
                dia = input('Seleccione el día: ').strip()


            paciente = input('Ingrese el nombre del paciente: ').strip().capitalize()

            while paciente == '' or not paciente.isalpha():
                print('El nombre solo puede contener letras.')
                paciente = input('Ingrese el nombre del paciente: ').strip().capitalize()


            if dia == '1':

                if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                    print('El paciente ya tiene un turno reservado el lunes.')

                elif lunes1 == '':
                    lunes1 = paciente
                    print('Turno reservado correctamente.')
                    print('Turno asignado: Lunes - Turno 1')

                elif lunes2 == '':
                    lunes2 = paciente
                    print('Turno reservado correctamente.')
                    print('Turno asignado: Lunes - Turno 2')

                elif lunes3 == '':
                    lunes3 = paciente
                    print('Turno reservado correctamente.')
                    print('Turno asignado: Lunes - Turno 3')

                elif lunes4 == '':
                    lunes4 = paciente
                    print('Turno reservado correctamente.')
                    print('Turno asignado: Lunes - Turno 4')

                else:
                    print('No hay turnos disponibles para el lunes.')


            elif dia == '2':

                if paciente == martes1 or paciente == martes2 or paciente == martes3:
                    print('El paciente ya tiene un turno reservado el martes.')

                elif martes1 == '':
                    martes1 = paciente
                    print('Turno reservado correctamente.')
                    print('Turno asignado: Martes - Turno 1')

                elif martes2 == '':
                    martes2 = paciente
                    print('Turno reservado correctamente.')
                    print('Turno asignado: Martes - Turno 2')

                elif martes3 == '':
                    martes3 = paciente
                    print('Turno reservado correctamente.')
                    print('Turno asignado: Martes - Turno 3')

                else:
                    print('No hay turnos disponibles para el martes.')


        case '2':
            print('\n--- Cancelar turno ---')
            print('1. Lunes')
            print('2. Martes')

            dia = input('Seleccione el día: ').strip()

            while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
                print('Debe ingresar 1 para Lunes o 2 para Martes.')
                dia = input('Seleccione el día: ').strip()


            paciente = input('Ingrese el nombre del paciente: ').strip().capitalize()

            while paciente == '' or not paciente.isalpha():
                print('El nombre solo puede contener letras.')
                paciente = input('Ingrese el nombre del paciente: ').strip().capitalize()


            if dia == '1':

                if paciente == lunes1:
                    lunes1 = ''
                    print('Turno cancelado correctamente.')

                elif paciente == lunes2:
                    lunes2 = ''
                    print('Turno cancelado correctamente.')

                elif paciente == lunes3:
                    lunes3 = ''
                    print('Turno cancelado correctamente.')

                elif paciente == lunes4:
                    lunes4 = ''
                    print('Turno cancelado correctamente.')

                else:
                    print('El paciente no tiene turno el lunes.')


            elif dia == '2':

                if paciente == martes1:
                    martes1 = ''
                    print('Turno cancelado correctamente.')

                elif paciente == martes2:
                    martes2 = ''
                    print('Turno cancelado correctamente.')

                elif paciente == martes3:
                    martes3 = ''
                    print('Turno cancelado correctamente.')

                else:
                    print('El paciente no tiene turno el martes.')


        case '3':
            print('\n--- Ver agenda del día ---')
            print('1. Lunes')
            print('2. Martes')

            dia = input('Seleccione el día: ').strip()

            while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
                print('Debe ingresar 1 para Lunes o 2 para Martes.')
                dia = input('Seleccione el día: ').strip()


            if dia == '1':
                print('\n--- Agenda del Lunes ---')

                if lunes1 == '':
                    print('Turno 1: (libre)')
                else:
                    print(f'Turno 1: {lunes1}')

                if lunes2 == '':
                    print('Turno 2: (libre)')
                else:
                    print(f'Turno 2: {lunes2}')

                if lunes3 == '':
                    print('Turno 3: (libre)')
                else:
                    print(f'Turno 3: {lunes3}')

                if lunes4 == '':
                    print('Turno 4: (libre)')
                else:
                    print(f'Turno 4: {lunes4}')


            elif dia == '2':
                print('\n--- Agenda del Martes ---')

                if martes1 == '':
                    print('Turno 1: (libre)')
                else:
                    print(f'Turno 1: {martes1}')

                if martes2 == '':
                    print('Turno 2: (libre)')
                else:
                    print(f'Turno 2: {martes2}')

                if martes3 == '':
                    print('Turno 3: (libre)')
                else:
                    print(f'Turno 3: {martes3}')


        case '4':
            ocupados_lunes = 0
            ocupados_martes = 0


            if lunes1 != '':
                ocupados_lunes += 1

            if lunes2 != '':
                ocupados_lunes += 1

            if lunes3 != '':
                ocupados_lunes += 1

            if lunes4 != '':
                ocupados_lunes += 1


            if martes1 != '':
                ocupados_martes += 1

            if martes2 != '':
                ocupados_martes += 1

            if martes3 != '':
                ocupados_martes += 1


            disponibles_lunes = 4 - ocupados_lunes
            disponibles_martes = 3 - ocupados_martes


            print('\n--- Resumen General ---')
            print(f'Lunes: {ocupados_lunes} ocupados - {disponibles_lunes} disponibles')
            print(f'Martes: {ocupados_martes} ocupados - {disponibles_martes} disponibles')


            if ocupados_lunes > ocupados_martes:
                print('El lunes es el día con más turnos ocupados.')

            elif ocupados_martes > ocupados_lunes:
                print('El martes es el día con más turnos ocupados.')

            else:
                print('Ambos días tienen la misma cantidad de turnos ocupados.')


        case '5':
            print('Cerrando sistema...')