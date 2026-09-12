usuario_correcto = 'alumno'
clave_correcta = 'python123'

intentos = 0
acceso_concedido = False

print('--- Acceso al Campus ---')

while intentos < 3 and acceso_concedido == False:
    print(f'\nIntento {intentos + 1}/3')

    usuario = input('Usuario: ').strip()
    clave = input('Clave: ').strip()

    if usuario == usuario_correcto and clave == clave_correcta:
        print('Acceso concedido.')
        acceso_concedido = True
    else:
        print('Error: credenciales inválidas.')
        intentos += 1


if acceso_concedido == False:
    print('Cuenta bloqueada.')

else:
    opcion = ''

    while opcion != '4':
        print('\n--- Menú Campus ---')
        print('1. Ver estado de inscripción')
        print('2. Cambiar clave')
        print('3. Mostrar mensaje motivacional')
        print('4. Salir')

        opcion = input('Opción: ').strip()

        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
            if not opcion.isdigit():
                print('Error: ingrese un número válido.')
            else:
                print('Error: opción fuera de rango.')

            opcion = input('Opción: ').strip()

        match opcion:
            case '1':
                print('Estado de inscripción: Inscripto.')

            case '2':
                nueva_clave = input('Ingrese la nueva clave: ').strip()

                while len(nueva_clave) < 6:
                    print('Error: mínimo 6 caracteres.')
                    nueva_clave = input('Ingrese la nueva clave: ').strip()

                confirmar_clave = input('Confirme la nueva clave: ').strip()

                while confirmar_clave != nueva_clave:
                    print('Error: las claves no coinciden.')
                    confirmar_clave = input('Confirme la nueva clave: ').strip()

                clave_correcta = nueva_clave
                print('Clave modificada correctamente.')

            case '3':
                print('Cada error es una oportunidad para aprender.')

            case '4':
                print('Saliendo del sistema...')