from Reglas import definir_flota, definir_opciones, definir_tamano, definir_modo, definir_nivel_ordenador
from General import inicializar_tablero, mostrar_resultados, mostrar_tablero, prueba_fin, verificar_barco_tocado
from Flota_usuario import colocar_barcos, obtener_entero
from Flota_ordenador import colocar_barcos_aleatorios
from Tiro_ordenador import tiro_compu_estrategico, tiro_compu_azar, verificar_barco_hundido
from Tiro_usuario import tiro_usuario
from Juego import Jugar

def main():
    print()
    bienvenida = "Bienvenida en la batalla naval !\n"
    print(bienvenida.center(60))

    print("=> Para comenzar, elige el tamaño de la rejilla en la que jugarás.")
    tamaño = definir_tamano()

    print()
    print("\n=> Ahora vas a elegir los barcos que constituirán tu flota y la de tu adversario. Atención, esta elección puede ser estratégica...\n")
    opcion = definir_opciones(tamaño)

    flota_cantidad = definir_flota(tamaño, opcion)
    flota_tamaño = {'Portaaviones': 5, 'Buques': 4, 'Submarinos': 3, 'Cruceros': 2, 'Lanchas': 1}
    primeras_letras = [cle[0] for cle in flota_tamaño.keys()]
    tablero_usuario = inicializar_tablero(tamaño)
    tablero_ordenador = inicializar_tablero(tamaño)

    print()
    print("=> Ahora vas a colocar tus barcos en la rejilla.\n")
    ubicacion_barcos_usuario = colocar_barcos(tablero_usuario, flota_tamaño, flota_cantidad)
    ubicacion_barcos_ordenador = colocar_barcos_aleatorios(tablero_ordenador, flota_tamaño, flota_cantidad, tamaño)
    print()
    
    # Tres lineas que permiten testear toda la parte encima. Puede comentarlas 
    # mostrar_resultados(ubicacion_barcos_usuario) 
    # mostrar_resultados(ubicacion_barcos_ordenador)
    # mostrar_tablero(tablero_ordenador)

    tiros_anteriores = set()
    casillas_a_evitar = set()
    tiros_probables=[]
    tocado=[]

    # testos para verficar las funciones de tiros individualmente 
    """ USUARIO
    tiro_usuario(tablero_ordenador, ubicacion_barcos_ordenador, primeras_letras)  
    """

    """ COMPUTADORA ESTRATEGICA
    tiro_compu_estrategico(tablero_usuario, tamaño, flota_tamaño, ubicacion_barcos_usuario, tiros_anteriores, casillas_a_evitar, primeras_letras, tiros_probables, tocado):
    """

    """ COMPUTADORA AZAR
    tiro_compu_azar(tablero_usuario, tamaño, flota_tamaño, ubicacion_barcos_usuario, tiros_anteriores, primeras_letras)
    """

    nivel = definir_nivel_ordenador()

    modo = definir_modo()
    
    Jugar(tablero_ordenador, ubicacion_barcos_ordenador, primeras_letras, tablero_usuario, tamaño, flota_tamaño, ubicacion_barcos_usuario, tiros_anteriores, modo, nivel, casillas_a_evitar, tiros_probables, tocado)
        
if __name__ == "__main__":
    main()