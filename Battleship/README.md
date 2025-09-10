# **Project Presentation**  
We worked on this project during our exchange semester in Argentina, which is why everything was originally written in Spanish. Currently, there is no English version. If you don’t speak Spanish, you will need to translate the content to understand the required parameters. We apologize for the inconvenience!  

# **Overall Code Structure**  
In this project, we organized several Python files to separate functions and structure the code clearly. Below is a summary of each file and its purpose:  

## **Phase 1 of the Project**  
- **rules.py**: Contains functions related to defining the game rules, such as fleet configuration, game options, board size, computer difficulty level, and game mode. This file includes everything the user needs to configure except their own fleet.  

- **general.py**: Stores general functions used throughout the game, including `initialize_board()`, `show_results()`, `show_board()`, `check_game_over()`, and `check_ship_hit()`. These functions are used for both the computer’s and the user’s shots.  

- **user_fleet.py**: Manages user interaction, including `place_ships()` and `get_integer()` to handle input.  

- **computer_fleet.py**: Contains functions for the computer to randomly place its ships, like `place_random_ships()`.  

## **Phase 2**  
- **computer_shot.py**: Handles the computer’s shots with `strategic_computer_shot()` and `random_computer_shot()`, and checks if it has sunk a player’s ship with `check_ship_sunk()`.  

## **Phase 3**  
- **user_shot.py**: Contains functions related to the player's shots, including `user_shot()` for marking hits, misses, and sunken ships on the board.  

## **Finalization**  
- **game.py**: Implements the two game modes for Battleship. It combines user and computer shots to create a full match.  
  1. **Alternative mode**: Players take turns shooting until they reach a set number of shots defined at the start.  
  2. **Continuous mode**: Players keep shooting as long as they hit opponent ships. If they miss, the other player takes a turn. The game ends when one player sinks the entire enemy fleet.  

- **main.py**: This is the main file that brings everything together. It sets up the game, places the user’s and computer’s ships, and runs the match. **To start the game, you must execute this file.**  

# **How Each File Works**  
Each file includes comments explaining the functions, their parameters, and what they return. This helps in understanding their role in the overall code.
