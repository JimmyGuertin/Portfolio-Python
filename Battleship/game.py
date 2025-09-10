from general import test_game_over, check_ship_hit, show_board
from user_fleet import get_integer
from computer_shot import strategic_computer_shot, random_computer_shot
from user_shot import user_shot

def Play(
    computer_board: list, 
    computer_ship_locations: dict, 
    first_letters: list, 
    user_board: list, 
    size: int, 
    fleet_size: dict, 
    user_ship_locations: dict, 
    previous_shots: set, 
    mode: int, 
    level: int, 
    cells_to_avoid: set, 
    probable_shots: list, 
    hit: list
):
    """
    Runs the Battleship game in alternating or continuous mode.

    Parameters
    ----------
    computer_board
        Grid representing the computer's ships.
    computer_ship_locations
        Coordinates of the computer's ships.
    first_letters
        First letters of all ship types.
    user_board
        Grid representing the user's ships.
    size
        Dimension of the game grid.
    fleet_size
        Dictionary mapping ship types to their size in cells.
    user_ship_locations
        Coordinates of the user's ships.
    previous_shots
        Coordinates of previous computer shots in strategic mode.
    mode
        Game mode (1 = alternating, 2 = continuous).
    level
        Computer shot type (1 = random, 2 = strategic).
    cells_to_avoid
        Cells for the computer to avoid in strategic mode.
    probable_shots
        List of cells with higher probability to contain a ship.
    hit
        Coordinates hit but not sunk in strategic mode.
    """
    if mode == 1:
        # Alternating mode
        print()
        turn_count = get_integer("Enter the number of shots per player: ")
        total_user_ships_sunk = 0
        total_user_ships_hit = 0
        total_computer_ships_sunk = 0
        total_computer_ships_hit = 0

        for turn in range(1, turn_count + 1):
            RED = "\033[31m"
            RESET = "\033[0m"
            print(RED + f"\nTurn {turn}:\n" + RESET)
            
            ships_sunk_user, ships_hit_user, board, x, y = user_shot(
                computer_board, computer_ship_locations, first_letters
            )
            total_user_ships_sunk += ships_sunk_user
            total_user_ships_hit += ships_hit_user

            print("_______________________________\n")
            print("It's the computer's turn!")
            if level == 1:
                ships_sunk_computer, ships_hit_computer, board, x, y = random_computer_shot(
                    user_board, size, fleet_size, user_ship_locations, previous_shots, first_letters
                )
            else:
                ships_sunk_computer, ships_hit_computer, board, x, y = strategic_computer_shot(
                    user_board, size, fleet_size, user_ship_locations, previous_shots, 
                    cells_to_avoid, first_letters, probable_shots, hit
                )
            total_computer_ships_sunk += ships_sunk_computer
            total_computer_ships_hit += ships_hit_computer
            
            print("\nYour grid with the computer's shots:")
            show_board(user_board)

        # Display final results
        print("\nFinal results:")
        print(f"Ships sunk by player: {total_user_ships_sunk}")
        print(f"Ships hit by player: {total_user_ships_hit}")
        print(f"Ships sunk by computer: {total_computer_ships_sunk}")
        print(f"Ships hit by computer: {total_computer_ships_hit}")

    elif mode == 2:
        # Continuous mode
        print()
        user_turn = True
        game_over = False
        total_user_ships_sunk = 0
        total_computer_ships_sunk = 0
        total_user_ships_hit = 0
        total_computer_ships_hit = 0
        
        while not game_over:
            if user_turn:
                print("_______________________________\n")
                print("Player's turn:\n")
                ships_sunk_user, ships_hit_user, user_shot_board, x, y = user_shot(
                    computer_board, computer_ship_locations, first_letters
                )
                total_user_ships_sunk += ships_sunk_user
                total_user_ships_hit += ships_hit_user
                
                if test_game_over(computer_board, first_letters):
                    print("\nCongratulations! You won. You sank all opponent ships.")
                    game_over = True
                elif check_ship_hit(user_shot_board, x, y):
                    user_turn = True
                else:
                    user_turn = False
            
            else:
                print("_______________________________\n")
                print("Computer's turn:\n")
                if level == 1:
                    ships_sunk_computer, ships_hit_computer, computer_shot_board, x, y = random_computer_shot(
                        user_board, size, fleet_size, user_ship_locations, previous_shots, first_letters
                    )
                else:
                    ships_sunk_computer, ships_hit_computer, computer_shot_board, x, y = strategic_computer_shot(
                        user_board, size, fleet_size, user_ship_locations, previous_shots, 
                        cells_to_avoid, first_letters, probable_shots, hit
                    )
                print("\nYour grid with the computer's shots:")
                show_board(user_board)

                total_computer_ships_sunk += ships_sunk_computer
                total_computer_ships_hit += ships_hit_computer
                
                if test_game_over(user_board, first_letters):
                    print("\nToo bad! The computer won. It sank all your ships.")
                    game_over = True
                elif check_ship_hit(computer_shot_board, x, y):
                    user_turn = False
                else:
                    user_turn = True
