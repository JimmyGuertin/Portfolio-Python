from Flota_usuario import obtener_entero

def definir_tamano():
    while True:
        tamaño = obtener_entero('Puedes elegir entre 5 (rejilla de 5x5) o 10 (rejilla de 10x10): ')
        if tamaño in (5, 10):
            return tamaño
        else:
            print('Por favor, introduce un valor válido (5 o 10).')

def definir_opciones(tamaño):
    if tamaño == 5:
        opcion = obtener_entero('Opción 1: 1 busque, 1 submarino, 1 lancha\n'
                           'Opción 2: 1 submarino, 2 crucero\n'
                           'Opción 3: 2 cruceros, 2 lanchas\n'
                           '\nSelecciona una opción: ')
        while opcion not in (1, 2, 3):
            print('Por favor, introduce una opción válida (1, 2 o 3).')
            opcion = obtener_entero('Opción 1: 1 busque, 1 submarino, 1 lancha\n'
                           'Opción 2: 1 submarino, 2 crucero\n'
                           'Opción 3: 2 cruceros, 2 lanchas\n'
                           '\nSelecciona una opción: ')
        return opcion
    else:
        opcion = obtener_entero('Opción 1: 1 portaaviones, 2 buques, 3 submarinos, 4 cruceros\n'
                           'Opción 2: 1 portaaviones, 1 buque, 2 submarinos, 3 cruceros\n'
                           'Opción 3: 1 buque, 2 submarinos, 3 cruceros, 4 lanchas\n'
                           '\nSelecciona una opción: ')
        while opcion not in (1, 2, 3):
            print('Por favor, introduce una opción válida (1, 2 o 3).')
            opcion = obtener_entero('Opción 1: 1 portaaviones, 2 buques, 3 submarinos, 4 cruceros\n'
                           'Opción 2: 1 portaaviones, 1 buque, 2 submarinos, 3 cruceros\n'
                           'Opción 3: 1 buque, 2 submarinos, 3 cruceros, 4 lanchas\n'
                           '\nSelecciona una opción: ')
        return opcion

def definir_flota(tamaño, opcion):
    if tamaño == 5:
        if opcion == 1:
            return {'Portaaviones': 0, 'Buques': 1, 'Submarinos': 1, 'Cruceros': 0, 'Lanchas': 1}
        elif opcion == 2:
            return {'Portaaviones': 0, 'Buques': 0, 'Submarinos': 1, 'Cruceros': 2, 'Lanchas': 0}
        elif opcion == 3:
            return {'Portaaviones': 0, 'Buques': 0, 'Submarinos': 0, 'Cruceros': 2, 'Lanchas': 2}

    else:
        if opcion == 1:
            return {'Portaaviones': 1, 'Buques': 2, 'Submarinos': 3, 'Cruceros': 4, 'Lanchas': 0}
        elif opcion == 2:
            return {'Portaaviones': 1, 'Buques': 1, 'Submarinos': 2, 'Cruceros': 3, 'Lanchas': 0}
        elif opcion == 3:
            return {'Portaaviones': 0, 'Buques': 1, 'Submarinos': 2, 'Cruceros': 3, 'Lanchas': 4}

def definir_nivel_ordenador():
    print("\nElige el nivel de dificultad que quieras")
    print("\n1. La computadora elige de manera aleatoria ")
    print("2. La computadora elige de manera estrategica\n")
    nivel = obtener_entero("Ingresa 1 o 2 : ")
    return nivel

def definir_modo():
    print("\nElige un modo de juego :")
    print("\n1. Modo alternativo : los jugadores se juegan uno tras otro hasta alcanzar un número de tiros cada uno que el usuario ingresó al inicio del juego")
    print("2. Modo continuo : los jugadores disparan siempre que golpeen los barcos de su oponente. \nSi están en el agua, le corresponde al otro jugador disparar. \nEsta vez el juego termina cuando uno de los jugadores ha hundido toda la flota de su oponente.\n")
    modo = obtener_entero("Ingresa 1 o 2 : ")
    return modo

