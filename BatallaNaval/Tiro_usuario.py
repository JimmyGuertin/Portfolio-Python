from General import mostrar_tablero, verificar_barco_hundido, marcar_barco_hundido

"""
Objetivo : Hacer un tiro del usuario
Entradas : - tablero inicializado
           - ubicacio_barcos_ordenador es todos los barcos de la computadora
           - primeras_letras son las claves que corresponden a cada tipo de barcos
Salidas :  - barcos_hundidos para contar el total de los barcos hundidos por el usuario al fin de la parte
           - barcos_tocados para contar el total de los barcos tocados por el usuario al fin de la parte
           - tablero es para verificar si, en el modo 2 de juego, un barco fue tocado en el ultimo tiro
           - (x,y) es la pareja de las coordenadas correspondante a donde tiro el usuario 
"""
def tiro_usuario(tablero, ubicacion_barcos_ordenador, primeras_letras):
    n = len(tablero)
    tableroc = [[tablero[x][y] for y in range(n)] for x in range(n)]
    for x in range(1, n):
        for y in range(1, n):
            if tablero[x][y] == '.' or tablero[x][y] == 'X' or tablero[x][y] == 'O':
                tableroc[x][y] = tablero[x][y]
            else:
                tableroc[x][y] = '~'
    
    mostrar_tablero(tableroc)
    print("¡Es tu turno de jugar!")
    
    while True:
        try:
            x = int(input("Ingrese la coordenada x (entre 0 y {}): ".format(n - 2)))
            y = int(input("Ingrese la coordenada y (entre 0 y {}): ".format(n - 2)))
            if 0 <= x < n - 1 and 0 <= y < n - 1:
                break
            else:
                print("Coordenadas fuera de rango. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Inténtalo de nuevo.")
    
    barcos_hundidos = 0
    barcos_tocados = 0
    
    if tablero[x + 1][y + 1] == '~':
        print("\n¡Fallaste, era agua!\n")
        tablero[x + 1][y + 1] = '.'
        tableroc[x + 1][y + 1] = '.'
    else:
        print(f"\n¡Bien hecho, has tocado en ({x}, {y})!\n")
        tablero[x + 1][y + 1] = 'X'
        tableroc[x + 1][y + 1] = 'X'
        barcos_tocados += 1

        barco_hundido, positions = verificar_barco_hundido(tablero, x, y, ubicacion_barcos_ordenador, primeras_letras)

        if barco_hundido:
            print("\n¡Increíble, has hundido un barco!\n")
            marcar_barco_hundido(tablero, tableroc, positions)
            barcos_hundidos += 1

    mostrar_tablero(tableroc)
    
    return barcos_hundidos, barcos_tocados, tablero, x, y

