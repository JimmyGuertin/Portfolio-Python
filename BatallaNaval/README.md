# Presentacion del proyecto
Somos tres estudiantes franceses en intercambio: 
- Lise Le Guillou, 
- Jimmy, 
- Joseph

Hemos trabajado en funciones diferentes durante el proyecto para distribuir inteligentemente el trabajo.Vamos a presentar nuestro juego de batalla naval para que entiendan bien a qué corresponde cada página y cada función que hemos codificado.

# Funcionamiento global del codigo
En esta carpeta hemos diseñado varios archivos de Python para separar las funciones y organizar el código. A continuación, describiremos brevemente qué representa cada uno de los archivos y por qué utilizamos esta clasificación:

## Etapa 1 del proyecto
Reglas.py: Contiene funciones relacionadas con la definición de reglas del juego, como la configuración de la flota, opciones de juego, tamaño del tablero, nivel de dificultad del ordenador y modo de juego. Finalmente, contiene todo lo que el usuario debe elegir para configurar el juego expecto su flota.

General.py: Aquí se encuentran funciones generales utilizadas en todo el juego, como la inicialización del tablero, la visualización de resultados, la visualización del tablero durante el juego, la prueba de finalización del juego y la verificación de si un barco ha sido tocado. Asi son las funciones comunes para los tiros de la computadora como los del usuario.

Flota_usuario.py: Contiene funciones específicas para la interacción con el usuario, como la colocación de barcos por parte del jugador y la obtención de datos de entrada del usuario.

Flota_ordenador.py: Este archivo incluye funciones para que el ordenador coloque sus barcos de manera aleatoria.

## Etapa 2
Tiro_ordenador.py: Aquí se encuentran las funciones relacionadas con los tiros realizados por el ordenador, tanto de manera aleatoria como estratégica, y la verificación de si ha hundido un barco del jugador.

## Etapa 3
Tiro_usuario.py: Contiene las funciones relacionadas con los tiros realizados por el jugador, incluyendo la lógica para marcar aciertos, fallos y hundimientos de barcos en el tablero.

## Finalizacion
Juego.py : Este archivo incluye los dos modos posibles para jugar la batalla naval. Finalmente es la compilacion de los tiros de usuario y computadora para crear un partido. Elegimos dos modos para jugar a nuestra batalla naval. 
Primero, el modo alternativo donde los jugadores (computadora y usuario) se juegan uno tras otro hasta alcanzar un número de tiros cada uno que el usuario ingresó al inicio del juego.
Segundo, el modo continuo donde los jugadores disparan siempre que golpeen los barcos de su oponente. Si están en el agua, le corresponde al otro jugador disparar. Esta vez el juego termina cuando uno de los jugadores ha hundido toda la flota de su oponente.

Main.py : Contiene todas las funciones para configurar el juego, colocar los barcos del ususario y de la computadora y con eso, se juega tambien aca el partido. Por eso, es con este archivo que debe iniciar el juego.

# Funcionamiento de cada archivo
En cada archivo hemos comentado las funciones para entender qué parámetros reciben y qué retornan. Esto ayuda a comprender su importancia en el código global.
