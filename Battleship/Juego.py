from General import prueba_fin, verificar_barco_tocado, mostrar_tablero
from Flota_usuario import obtener_entero
from Tiro_ordenador import tiro_compu_estrategico, tiro_compu_azar
from Tiro_usuario import tiro_usuario

"""
Objetivo : Construye el juego usando dos modos diferentes para que los jugadores puedan jugar juntos 
Entrada : - tablero_ordenador se refiere a los barcos del ordenador que estan ubicados en la rejilla 
          - ubicacion_barcos_ordenador representa la flota del ordenador (ubicaciones como pareja de coordenadas)
          - primeras_letras representan la primera letra de cada tipo de barcos
          - tablero_usuario se refiere a los barcos del usuario que estan ubicados en la rejilla 
          - tamaño, opcion que elegio el usuario en el Main : dimension de la rejilla de juego 
          - flota_tamaño, el dicionario de tipo de barcos a que coresponde un numero de casilla
          - ubicacion_barcos_usuario representa la flota del usuario (ubicaciones como pareja de coordenadas)
          - tiros_anteriores representa los tiros anteriores del ordenador en el nivel estrategico 
          - modo, opcion que elegio el usuario en el Main : manera de jugar que puede ser alternativa o continua (se explica despues)
          - nivel, opcion que elegio el usuario en el Main : tiro de la computadora que puede ser estrategico o con azar 
          - casillas_a_evitar es la lista que permite al ordenador estar estrategico
          - tiros_probables es una lista de las casillas donde hay mas probabilidad para tener un barco 
          - tocado representa las casillas que fueron tocadas en los tiros estrategicos de la computadora 
Salida : ninguna
"""
def Jugar(tablero_ordenador, ubicacion_barcos_ordenador, primeras_letras, tablero_usuario, tamaño, flota_tamaño, ubicacion_barcos_usuario, tiros_anteriores, modo, nivel, casillas_a_evitar, tiros_probables, tocado):

    # modo alternativo : 
    # los jugadores se juegan uno tras otro hasta alcanzar un número de tiros cada uno que el usuario ingresó al inicio del juego
    if modo == 1:
        print()
        numeros_turnos = obtener_entero("Ingrese el número de disparos por persona: ")
        total_barcos_hundidos_usuario = 0
        total_barcos_tocados_usuario = 0
        total_barcos_hundidos_compu = 0
        total_barcos_tocados_compu = 0

        for turno in range(1, numeros_turnos + 1):
            RED = "\033[31m"        
            RESET = "\033[0m"
            print(RED + f"\nTurno {turno}:\n" + RESET)
            barcos_hundidos_usuario, barcos_tocados_usuario, tablero, x, y = tiro_usuario(tablero_ordenador, ubicacion_barcos_ordenador, primeras_letras)
            total_barcos_hundidos_usuario += barcos_hundidos_usuario
            total_barcos_tocados_usuario += barcos_tocados_usuario

            print ("_______________________________")
            print()
            print("Es el turno de la compuatdora !")
            if nivel == 1:
                barcos_hundidos_compu, barcos_tocados_compu, tablero, x, y = tiro_compu_azar(tablero_usuario, tamaño, flota_tamaño, ubicacion_barcos_usuario, tiros_anteriores, primeras_letras)
            else: 
                barcos_hundidos_compu, barcos_tocados_compu, tablero, x, y = tiro_compu_estrategico(tablero_usuario, tamaño, flota_tamaño, ubicacion_barcos_usuario, tiros_anteriores, casillas_a_evitar, primeras_letras, tiros_probables, tocado)
            total_barcos_hundidos_compu += barcos_hundidos_compu
            total_barcos_tocados_compu += barcos_tocados_compu
            
            print("\nTu rejilla con los tiros de la computadora :")
            mostrar_tablero(tablero_usuario)

            print ("_______________________________")
            print()

        print("\nResultados finales:")
        print(f"Barcos hundidos por el jugador: {total_barcos_hundidos_usuario}")
        print(f"Barcos tocados por el jugador: {total_barcos_tocados_usuario}")
        print(f"Barcos hundidos por el ordenador: {total_barcos_hundidos_compu}")
        print(f"Barcos tocados por el ordenador: {total_barcos_tocados_compu}")

        if total_barcos_hundidos_usuario > total_barcos_hundidos_compu:
            print(f"\n¡Felicidades! Has ganado. Hundiste {total_barcos_hundidos_usuario} barco(s) de tu adversario contra {total_barcos_hundidos_compu}.")
        elif total_barcos_hundidos_usuario < total_barcos_hundidos_compu:
            print(f"\n¡Qué lástima! El ordenador ha ganado. Hundiste {total_barcos_hundidos_usuario} barco(s) de tu adversario contra {total_barcos_hundidos_compu}.")
        elif total_barcos_hundidos_usuario == total_barcos_hundidos_compu and total_barcos_tocados_usuario > total_barcos_tocados_compu:
            print(f"\n¡Felicidades! Has ganado. Tocaste {total_barcos_tocados_usuario} barco(s) de tu adversario contra {total_barcos_tocados_compu}.")
        elif total_barcos_hundidos_usuario == total_barcos_hundidos_compu and total_barcos_tocados_usuario < total_barcos_tocados_compu:
            print(f"\n¡Qué lástima! El ordenador ha ganado. Tocaste {total_barcos_tocados_usuario} barco(s) de tu adversario contra {total_barcos_tocados_compu}.")
        else:
            print(f"\nEs un empate. Hundiste {total_barcos_hundidos_usuario} barco(s) cada uno.")

    # modo continuo : 
    # los jugadores disparan siempre que golpeen los barcos de su oponente. 
    # Si están en el agua, le corresponde al otro jugador disparar. 
    # Esta vez el juego termina cuando uno de los jugadores ha hundido toda la flota de su oponente.
    elif modo == 2:
        print()
        turno_usuario = True # usuario que empieza
        juego_terminado = False # juego en curso mientras juego_terminado = False
        total_barcos_hundidos_usuario = 0 # inicialización del número de barcos hundidos de ambos lados
        total_barcos_hundidos_compu = 0
        total_barcos_tocados_usuario = 0
        total_barcos_tocados_compu = 0
        
        while not juego_terminado: # mientras el juego no ha terminado (es decir, ningún jugador ha hundido todos los barcos de su adversario)
            if turno_usuario: # el usuario juega si turno_usuario = True
                print ("_______________________________")
                print()
                print("\nTurno del jugador:\n")
                barcos_hundidos_usuario, barcos_tocados_usuario, tablero_tiros_usuario,x,y = tiro_usuario(tablero_ordenador, ubicacion_barcos_ordenador, primeras_letras) # un tiro para el usuario
                total_barcos_hundidos_usuario += barcos_hundidos_usuario # si un barco es hundido, se incrementa el número total de barcos hundidos
                total_barcos_tocados_usuario += barcos_tocados_usuario
                
                if prueba_fin(tablero_ordenador, primeras_letras): # si todos los barcos son hundidos, entonces el juego ha terminado
                    print("\n¡Felicidades! Has ganado. Has hundido todos los barcos de tu adversario.")
                    juego_terminado = True

                elif verificar_barco_tocado(tablero_tiros_usuario, x, y) :
                    turno_usuario = True
                
                else: # sino es el turno del ordenador
                    turno_usuario = False
            
            else:
                print ("_______________________________")
                print()
                print("\nTurno del ordenador:\n")
                if nivel == 1:
                    barcos_hundidos_compu, barcos_tocados_compu, tablero_tiros_ordenador, x, y = tiro_compu_azar(tablero_usuario, tamaño, flota_tamaño, ubicacion_barcos_usuario, tiros_anteriores, primeras_letras)
                else: 
                    barcos_hundidos_compu, barcos_tocados_compu, tablero_tiros_ordenador, x, y = tiro_compu_estrategico(tablero_usuario, tamaño, flota_tamaño, ubicacion_barcos_usuario, tiros_anteriores, casillas_a_evitar, primeras_letras, tiros_probables, tocado)
                print()
                print("Tu rejilla con los tiros de la computadora")
                mostrar_tablero(tablero_usuario)

                total_barcos_hundidos_compu += barcos_hundidos_compu
                total_barcos_tocados_compu += barcos_tocados_compu
                
                if prueba_fin(tablero_usuario, primeras_letras):
                    print("\n¡Qué lástima! El ordenador ha ganado. Ha hundido todos tus barcos.")
                    juego_terminado = True

                elif verificar_barco_tocado(tablero_tiros_ordenador, x, y) :
                    turno_usuario = False
                
                else: # sino es el turno del jugador
                    turno_usuario = True
