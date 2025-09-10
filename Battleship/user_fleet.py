from General import mostrar_tablero,comprobar_posicion, actualizar_tablero, registrar_posiciones

"""
Objetivo : Verificar que los entradas del usuarios son enteros cuando elige los parametros del partido
Entrada : mensaje es la entrada del usuario
Salida : valor es lo que el usuario entra o print con mensaje de error para intentar de nuevo
"""
def obtener_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Por favor, introduce un valor entero válido.")


"""
Objetivo : Pedir al usuario donde quiere colocar cada barco de su flota 
Entrada : - tablero inicializado 
          - flota_tamano es la composicion que elige el ususario para su flota y ella de la compu
          - flota_cantidad es la cantidad de cada tipo de barcos que contiene la flota del usuario
Salida : ubicacion_barcos que representa los barcos del usuario con sus posiciones
"""
def colocar_barcos(tablero, flota_tamaño, flota_cantidad):
    ubicacion_barcos = {barco: [] for barco in flota_cantidad}

    for barco in flota_cantidad.keys():
        for num in range(flota_cantidad[barco]):
            sig = False
            while not sig:
                print(f"Colocar {barco} número {num + 1} :")
                mostrar_tablero(tablero) 
                n = len(tablero)

                x = obtener_entero(f"¿Dónde colocar las coordenadas de la fila de origen (0-{n-1})?: ")
                y = obtener_entero(f"¿Dónde colocar las coordenadas de la columna de origen (0-{n-1})?: ")

                if x < 0 or x >= len(tablero) or y < 0 or y >= len(tablero):
                    print('Valores incorrectos. Las coordenadas deben estar entre 0 y 9. Vuelve a intentarlo.')
                    print()
                    continue

                direccion = 0  
                if barco != 'Lanchas':
                    direccion = obtener_entero('Dirección horizontal (hasta derecha) (0) / vertical (hasta arriba) (1): ')

                    if direccion not in [0, 1]:
                        print('Valor incorrecto para la dirección. Debe ser 0 (horizontal) o 1 (vertical). Vuelve a intentarlo.')
                        print()  
                        continue

                if comprobar_posicion(tablero, flota_tamaño, barco, x, y, direccion):
                    tablero = actualizar_tablero(tablero, flota_tamaño, barco, x, y, direccion)
                    registrar_posiciones(ubicacion_barcos, barco, x, y, direccion, flota_tamaño[barco])
                    sig = True
                else:
                    print('No hay espacio para el barco.')
                    print()  
    
    return ubicacion_barcos
