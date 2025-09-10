import random
from General import mostrar_tablero, comprobar_posicion, actualizar_tablero, registrar_posiciones

"""
Objetivo : Generar coordenadas aleatorias para colocar los barcos del ordenador despues
Entrada : - tamano es la dimension de la rejilla 
          - barco es el barco que va a posicionar 
          - direccion es la direccion aleatoria 
          - flota_tamano es la composicion que elige el ususario para su flota y ella de la compu
Salida : (x,y) la pareja de coordenadas elegida aletoriamente para posicionar el barco
"""
def generar_coordenadas_aleatorias(tamaño,barco,direccion,flota_tamaño):
    tamaño_barco=flota_tamaño[barco]
    if direccion==0:
        x = random.randint(0, tamaño-tamaño_barco)
        y = random.randint(0, tamaño-1)
    else:
        x = random.randint(1, tamaño-1)
        y = random.randint(0, tamaño-tamaño_barco)
    return x, y


"""
Objetivo : Generar direccion aleatorias para colocar los barcos del ordenador despues
Entrada : ninguna
Salida : 0 o 1 de manera aleatoria
"""
def generar_direccion_aleatoria():
    return random.randint(0, 1)


"""
Objetivo : colocar cada barco de la flota de la computadora
Entrada : - tablero inicializado 
          - flota_tamano es la composicion que elige el ususario para su flota y ella de la compu
          - flota_cantidad es la cantidad de cada tipo de barcos que contiene la flota del usuario
          - tamano es la dimension de la rejilla 
Salida : ubicacion_barcos que contiene todos los barcos del ordenador
"""
def colocar_barcos_aleatorios(tablero, flota_tamaño, flota_cantidad, tamaño):
    ubicacion_barcos = {barco: [] for barco in flota_cantidad}

    for barco in flota_cantidad.keys():
        for num in range(flota_cantidad[barco]):
            sig = False
            while not sig:
                direccion = generar_direccion_aleatoria() if barco != 'Lanchas' else 0
                x, y = generar_coordenadas_aleatorias(tamaño,barco,direccion,flota_tamaño)
                

                if comprobar_posicion(tablero, flota_tamaño, barco, x, y, direccion):
                    tablero = actualizar_tablero(tablero, flota_tamaño, barco, x, y, direccion)
                    registrar_posiciones(ubicacion_barcos, barco, x, y, direccion, flota_tamaño[barco])
                    sig = True
                    # mostrar_tablero(tablero) # para verificar si los barcos se posicionan bien                 
    return ubicacion_barcos
