import random
from General import verificar_barco_hundido, marcar_barco_hundido

"""
Objetivo : Generar coordenadas aleatorias para tirar despues
Entrada : tamano es la dimension de la rejilla 
Salida : x , una coordenada elegida aletoriamente 
"""
def generar_coordenada_aleatoria(tamaño):
    return random.randint(0, tamaño - 1), random.randint(0, tamaño - 1)


"""
Objetivo : Sirve en el tiro estrategico del ordenador porque sabemos que dos barcos no se pueden pegar 
Entradas : - (x,y) pareja de coordenadas del ultimo tiro cuando hundio el barco
           - posiciones se refiere a la ubicacion de los barcos en la rejilla 
           - casillas_a_evitar es la lista de las casillas a evitar para los proximos tiros porque sabemos que es agua o barcos ya hundidos 
Salida : Agregacion casillas para evitar a la lista ya existente
"""
def marcar_areas_cerca_hundido(x, y, posiciones, casillas_a_evitar):
    if len(posiciones)==1:
        casillas_a_evitar.add((x+1,y),(x-1,y),(x,y+1),(x,y-1))
        casillas_a_evitar.add((x-1,y))
        casillas_a_evitar.add((x,y+1))
        casillas_a_evitar.add((x,y-1))
    else:
        if posiciones[0][0]!=posiciones[1][0]:
            casillas_a_evitar.add((posiciones[0][0]+1,y))
            casillas_a_evitar.add((posiciones[-1][0]-1,y))
            for k in range (len(posiciones)):
                casillas_a_evitar.add((posiciones[k][0],y-1))
                casillas_a_evitar.add((posiciones[k][0],y+1))
        else:
            casillas_a_evitar.add((x,posiciones[0][1]-1))
            casillas_a_evitar.add((x,posiciones[-1][1]+1))
            for k in range (len(posiciones)):
                casillas_a_evitar.add((x-1,posiciones[k][1]))
                casillas_a_evitar.add((x+1,posiciones[k][1]))


"""
Objetivo : a lo largo de los tiros, tener una lista de los casillas más probables para que la computadora pueda elegir entre estos casillas
Entradas : - probabilidades la lista de casillas donde es más probable que haya un barco
           - (tir_x,tir_y) es el tiro anterior que toco en un barco
           - tamano es la dimension de la rejilla 
Salidas : actualiza la lista de las casillas más probables
"""
def actualizar_probabilidades(probabilidades, tir_x, tir_y, tamaño):
    nuevas_coordenadas = [(tir_x + 1, tir_y), (tir_x - 1, tir_y), (tir_x, tir_y + 1), (tir_x, tir_y - 1)]
    probabilidades.extend([coord for coord in nuevas_coordenadas if 0 <= coord[0] < tamaño and 0 <= coord[1] < tamaño])


"""
Objetivo : eliminar casillas probables asociadas con el barco que acaba de hundirse
Entradas : - probabilidades la lista de casillas donde es más probable que haya un barco
           - posiciones son las del barco hundido
Salidas : eliminar las casillas donde ya no es probable que haya un barco
"""
def eliminar_probabilidades_asociadas(probabilidades, posiciones):
    for pos in posiciones:
        if pos in probabilidades:
            probabilidades.remove(pos)


"""
Objetivo : ver en qué dirección se ve afectado el barco
Entradas : - probabilidades la lista de casillas donde es más probable que haya un barco
           - (tir_x,tir_y) es el tiro anterior que toco en un barco
           - direction es horizontal o vertical
           - tamano es la dimension de la rejilla 
Salidas : actualiza la lista de las casillas más probables
"""
def priorizar_direccion(probabilidades, tir_x, tir_y, direction, tamaño):
    if direction == "horizontal":
        probabilidades.extend([(tir_x, tir_y - 1), (tir_x, tir_y + 1)])
    elif direction == "vertical":
        probabilidades.extend([(tir_x - 1, tir_y), (tir_x + 1, tir_y)])
    probabilidades[:] = [coord for coord in probabilidades if 0 <= coord[0] < tamaño and 0 <= coord[1] < tamaño]

"""
Objetivo : Hacer un tiro de la computadora de manera estrategica es decir que usamos probabilidades para que haya un barco
Entradas : - tablero inicializado
           - tamaño es la dimension de la rejilla del partido
           - flota_tamaño es la composicion que elige el ususario para su flota y ella de la compu
           - ubicacion_barcos representa los barcos del usuario con sus posiciones
           - tiros_anteriores es la lista de los tiros anteriores para no tirar en la misma casilla dos veces 
           - primeras_letras son las claves que corresponden a cada tipo de barcos
           - casillas_a_evitar es una lista que anade las casillas donde no hay barcos seguramente (como no puede tener dos barcos que se tocan)
           - probabilidades 
           - tocado
Salidas :  - barcos_hundidos para contar el total de los barcos hundidos por el ordenador al fin de la parte
           - barcos_tocados para contar el total de los barcos tocados por el ordenador al fin de la parte
           - tablero es para verificar si, en el modo 2 de juego, un barco fue tocado en el ultimo tiro
           - (x,y) es la pareja de las coordenadas correspondante a donde tiro el ordenador 
"""
def tiro_compu_estrategico(tablero, tamaño, flota_tamaño, ubicacion_barcos, tiros_anteriores, casillas_a_evitar, primeras_letras, probabilidades, tocado):
    barcos_hundidos = 0
    barcos_tocados = 0
    if probabilidades:
        x, y = probabilidades.pop(0)
    else:
        x, y = generar_coordenada_aleatoria(tamaño)
        
    while (x, y) in tiros_anteriores or (x, y) in casillas_a_evitar:
        if probabilidades:
            x, y = probabilidades.pop(0)
        else:
            x, y = generar_coordenada_aleatoria(tamaño)
            
    tiros_anteriores.add((x, y))
    
    if tablero[x + 1][y + 1] in primeras_letras:
        print(f"Touché en ({x}, {y}) !")
        tablero[x + 1][y + 1] = 'X'
        tocado.append((x, y))
        barco_hundido, posiciones = verificar_barco_hundido(tablero, x, y, ubicacion_barcos, primeras_letras)
        barcos_tocados += 1
        if barco_hundido:
            print("Coulé !")
            barcos_hundidos += 1
            marcar_barco_hundido(tablero, posiciones)
            marcar_areas_cerca_hundido(x, y, posiciones, casillas_a_evitar)
            eliminar_probabilidades_asociadas(probabilidades, posiciones)
            tocado.clear()
        else:
            if len(tocado) > 1:
                direction = "horizontal" if tocado[-1][0] == tocado[-2][0] else "vertical"
                priorizar_direccion(probabilidades, x, y, direction, tamaño)
            else:
                actualizar_probabilidades(probabilidades, x, y, tamaño)
    else:
        print(f"À l'eau en ({x}, {y}) !")
        tablero[x + 1][y + 1] = '.'

    return barcos_hundidos, barcos_tocados, tablero, x, y


"""
Objetivo : Hacer un tiro de la computadora de manera aleatoria
Entradas : - tablero inicializado
           - tamaño es la dimension de la rejilla del partido
           - flota_tamaño es la composicion que elige el ususario para su flota y ella de la compu
           - ubicacion_barcos representa los barcos del usuario con sus posiciones
           - tiros_anteriores es la lista de los tiros anteriores para no tirar en la misma casilla dos veces 
           - primeras_letras son las claves que corresponden a cada tipo de barcos
Salidas :  - barcos_hundidos para contar el total de los barcos hundidos por el ordenador al fin de la parte
           - barcos_tocados para contar el total de los barcos tocados por el ordenador al fin de la parte
           - tablero es para verificar si, en el modo 2 de juego, un barco fue tocado en el ultimo tiro
           - (x,y) es la pareja de las coordenadas correspondante a donde tiro el ordenador 
"""
def tiro_compu_azar(tablero, tamaño, flota_tamaño, ubicacion_barcos, tiros_anteriores, primeras_letras):
    tir_réussi = False
    barcos_hundidos = 0
    barcos_tocados = 0
    
    while not tir_réussi:
        x, y = generar_coordenada_aleatoria(tamaño)
        if (x, y) not in tiros_anteriores:
            tir_réussi = True
            tiros_anteriores.add((x, y))
            if tablero[x+1][y+1] in primeras_letras:  # Vérifier si la case contient une des premières lettres
                print(f"Touché en ({x}, {y}) !")
                tablero[x+1][y+1] = 'X'  # 'X' représente une case touchée avec un bateau
                barco_hundido, posiciones = verificar_barco_hundido(tablero, x, y, ubicacion_barcos, primeras_letras)
                if barco_hundido:
                    print("Coulé !")
                    marcar_barco_hundido(tablero, posiciones)
                    barcos_hundidos += 1
                else:
                    barcos_tocados += 1
            else:
                print(f"À l'eau en ({x}, {y}) !")
                tablero[x+1][y+1] = '.'  # '.' représente une case touchée sans bateau

    return barcos_hundidos, barcos_tocados, tablero, x, y