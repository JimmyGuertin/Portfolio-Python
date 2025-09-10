"""
Objetivo : crear una rejilla de 0 hasta 'tamano' con '~' en cada casilla 
Entrada : tamano representa el numero de lineas y columnas que el ususario quiere para su rejilla
Salida : tablero es la rejilla inicializada para empezar el juego 
"""
def inicializar_tablero(tamaño):
    tablero = [['~' for _ in range(tamaño + 1)] for _ in range(tamaño + 1)]
    for i in range(1, tamaño + 1):
        tablero[0][i] = i-1
        tablero[i][0] = i-1
    return tablero


"""
Objetivo : Mostrar en la consola para que el usuario vea su tablero con sus barcos 
           y el tablero de sus tiros anteriores para saber donde tirar
Entrada : tablero es la rejilla inicializada para empezar el juego
Salida : el print del tablero bien disenado 
"""
def mostrar_tablero(tablero):
    for fila in tablero:
        print(' '.join(map(str, fila)))
    print()


"""
Objetivo : Verificar que el jugador (usuario o compu) puede 
           poner sus barcos en las coordenadas que elige 
Entradas : - tablero es la rejilla inicializada para empezar el juego,
           - flota_tamano es la composicion que elige el ususario para su flota y ella de la compu
           - barco es el barco del que queremos ver si la coordenadas estan validas 
           - (x,y) representan la casilla que tenemos que comprobar
           - direccion es la direccion horizontal o vertical que quiere el ususario para su posicionar su barco
Salida : un booleano que expresa si la posición es correcta o no
"""
def comprobar_posicion(tablero, flota_tamaño, barco, x, y, direccion):
    longitud_barco = flota_tamaño[barco]

    if direccion == 0:
        if y+1 + longitud_barco > len(tablero):
            print()
            return False

        for i in range(longitud_barco):
            if tablero[x+1][y+1 + i] != '~':
                print()
                return False
            if x+1 > 1 and tablero[x+1 - 1][y+1 + i] != '~':
                print()
                return False
            if x+1 < len(tablero) - 1 and tablero[x+1 + 1][y+1 + i] != '~':
                print()
                return False
        if y+1 > 1 and tablero[x+1][y+1 - 1] != '~':
            print()
            return False
        if y+1 + longitud_barco < len(tablero) - 1 and tablero[x+1][y+1 + longitud_barco] != '~':
            print()
            return False

    elif direccion == 1:
        if x+1 - longitud_barco + 1 < 1:
            print()
            return False

        for i in range(longitud_barco):
            if tablero[x+1 - i][y+1] != '~':
                print()
                return False
            if y+1 > 1 and tablero[x+1 - i][y+1 - 1] != '~':
                print()
                return False
            if y+1 < len(tablero) - 1 and tablero[x+1 - i][y+1 + 1] != '~':
                print()
                return False
        if x+1 - longitud_barco >= 1 and tablero[x+1 - longitud_barco][y+1] != '~':
            print()
            return False
        if x+1 < len(tablero) - 1 and tablero[x+1 + 1][y+1] != '~':
            print()
            return False

    print()
    return True


"""
Objetivo : Mostrar su tablero de los barcos al jugador con sus barcos a medida que los agrega
Entradas : - tablero es la rejilla inicializada para empezar el juego,
           - flota_tamano es la composicion que elige el ususario para su flota y ella de la compu
           - barco es el barco del que queremos ver si la coordenadas estan validas 
           - (x,y) representan la casilla que tenemos que comprobar
           - direccion es la direccion horizontal o vertical que quiere el ususario para su posicionar su barco
Salida : tablero es la rejilla inicializada y actualizada con los barcos del jugador
"""
def actualizar_tablero(tablero, flota_tamaño, barco, x, y, direccion):
    longitud_barco = flota_tamaño[barco]
    print()
    if direccion == 0:
        print()
        for i in range(longitud_barco):
            tablero[x+1][y+1 + i] = barco[0]
    elif direccion == 1:
        for i in range(longitud_barco):
            tablero[x+1 - i][y+1] = barco[0]
    return tablero


"""
Objetivo : Registrar las posiciones de los barcos del jugador (usuario y compu) para controlar despues el avance del juego
Entradas : - ubicacion_barcos es un diccionario para corresponder 'barcos' a 'flota_cantidad'
           - barco es el barco del que queremos ver si la coordenadas estan validas 
           - (x,y) representan la casilla que tenemos que comprobar
           - direccion es la direccion horizontal o vertical que quiere el ususario para su posicionar su barco
Salida : ubicacion barcos actualizado con los barcos anadidos por el jugador
"""
def registrar_posiciones(ubicacion_barcos, barco, x, y, direccion, longitud_barco):
    posiciones = []
    if direccion == 0:  # Horizontal
        for i in range(longitud_barco):
            posiciones.append((x, y + i))
    elif direccion == 1:  # Vertical
        for i in range(longitud_barco):
            posiciones.append((x - i, y))
    # Ajouter les positions pour le bateau spécifié
    if barco in ubicacion_barcos:
        ubicacion_barcos[barco] += [posiciones]
    else:
        ubicacion_barcos[barco] = posiciones


"""
Objetivo : Una funccion de prueba para verificar que los barcos estan bien posicionados 
Entradas : ubicacion barcos es el diccionario con todos los barcos del jugador (usuario o compu)
Salida : print para mostrar los tipos de barcos con sus coordenadas (ej : submarino (1,2))
"""
def mostrar_resultados(ubicacion_barcos):
    print("Ubicación de los barcos:")
    for barco, posiciones in ubicacion_barcos.items():
        print(f"{barco}: {posiciones}")


"""
Objetivo : Verificar si los barcos del jugador estan todos hundidos por el otro jugador 
Entradas : - tablero es la rejilla con los barcos del jugador 
           - letras_barcos representa la lista de la primera letra de cada tipo de barcos
Salida : un booleano que explica si la rejilla esta vacia de barcos es decir que el juego esta terminado o no
"""
def prueba_fin(tablero, letras_barcos):
    return all(cell not in letras_barcos for row in tablero for cell in row)


"""
Objetivo : Verificar si un barco es tocado duspues de un tiro
Entradas : - tablero es la rejilla con los barcos del jugador
           - (x,y) representan la casilla que tenemos que comprobar
Salidas : un booleano que expresa si la posición es correcta o no
"""
def verificar_barco_tocado(tablero,x,y):
    if tablero[x+1][y+1] == 'X':
        return True
    

"""
Objetivo : Entender si un barco fue hundido despues de un tiro 
Entradas : - tablero inicializado 
           - (x,y) es la pajera de coordenadas que fue tirada el en ultimo tiro
           - ubicacion_barcos_ordenador que es la rejilla (tablero) con todos los barcos del ordenador
           - primeras_letras son las claves que corresponden a cada tipo de barcos
Salidas : un booleano que nos dice si el barco fue totalmente hundido gracias al ultimo tiro del usuario
"""
def verificar_barco_hundido(tablero, x, y, ubicacion_barcos_ordenador, primeras_letras):
    for barco, posiciones_list in ubicacion_barcos_ordenador.items():
        for k in range (len(posiciones_list)):
            for posiciones in posiciones_list[k]:
                if (x, y) ==posiciones:
                    coule = True
                    for pos_x, pos_y in posiciones_list[k]: 
                        if tablero[pos_x+1][pos_y+1] in primeras_letras:
                            coule = False
                            break
                    if coule:
                        return True, posiciones_list[k]
    return False, None


"""
Objetivo : Marcar un barco si fue hundido despues de un tiro 
Entradas : - tablero inicializado 
           - tableroc es el tablero con los resulatdos de los tiros anteriores
           - posiciones_list son los coordenadas de los barcos del ordenador 
Salida : un 'O' en el tablero inicial y el de los resultados 
"""
def marcar_barco_hundido(tablero, tableroc, posiciones_list):
    for x, y in posiciones_list:
        tablero[x+1][y+1] = 'O'
        tableroc[x+1][y+1] = 'O'