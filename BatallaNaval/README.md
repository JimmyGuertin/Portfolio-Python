# **Project Presentation**  
We worked on this project during our exchange semester in Argentina, which is why we kept everything in Spanish. For now, there is no English version. If you don’t speak Spanish, you will need to translate the content to understand the parameters required. Sorry for the inconvenience!  

# **Team Presentation**  
We are three French exchange students:  
- **Lise Le Guillou**  
- **Jimmy**  
- **Joseph**  

Each of us worked on different functions to distribute the workload efficiently. Here’s an overview of our Battleship game, including explanations of the files and functions we coded.  

# **Overall Code Structure**  
In this project, we organized several Python files to separate functions and structure the code clearly. Below is a summary of each file and its purpose:  

## **Phase 1 of the Project**  
- **Reglas.py**: Contains functions related to defining the game rules, such as fleet configuration, game options, board size, computer difficulty level, and game mode. This file includes everything the user needs to configure except for their fleet.  

- **General.py**: Stores general functions used throughout the game, including board initialization, displaying results, visualizing the board during gameplay, checking for game completion, and verifying if a ship has been hit. These functions apply to both the computer’s and the user’s shots.  

- **Flota_usuario.py**: Manages user interaction, including placing ships and collecting user input.  

- **Flota_ordenador.py**: Contains functions for the computer to randomly place its ships.  

## **Phase 2**  
- **Tiro_ordenador.py**: Handles the computer’s shots, both random and strategic, and checks if it has sunk one of the player’s ships.  

## **Phase 3**  
- **Tiro_usuario.py**: Contains functions related to the player's shots, including marking hits, misses, and sunken ships on the board.  

## **Finalization**  
- **Juego.py**: Implements the two game modes for Battleship. It combines user and computer shots to create a full match.  
  1. **Alternative mode**: Players (computer and user) take turns shooting until they reach a set number of shots defined by the user at the beginning.  
  2. **Continuous mode**: Players keep shooting as long as they hit their opponent's ships. If they miss, it’s the other player’s turn. The game ends when one player sinks the entire enemy fleet.  

- **Main.py**: This is the main file that brings everything together. It sets up the game, places the user’s and computer’s ships, and runs the match. To start the game, you must execute this file.  

# **How Each File Works**  
Each file includes comments explaining the functions, their parameters, and what they return. This helps in understanding their role in the overall code.  
